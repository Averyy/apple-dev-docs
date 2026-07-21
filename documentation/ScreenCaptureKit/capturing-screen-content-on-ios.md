# Capturing screen content on iOS

**Framework**: ScreenCaptureKit

Record and share screen captures on iOS by presenting the system content-sharing picker.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

This sample shows how to capture screen content on iOS using [`ScreenCaptureKit`](ScreenCaptureKit.md). ScreenCaptureKit supports screen streaming and mirroring on all available platforms. You present the system content-sharing picker to let a person choose between capturing the entire display or content from within the sample, then stream that content with fine-grained control over audio, recording, and the camera.

You use the sample to record the screen to a file, to buffer up to 15 seconds of rolling video and export a clip on demand, and to show a live camera preview during in-app captures. When a recording finishes, the sample saves the file to Photos and offers it through the standard share sheet.

> **Note**: This sample requires a device running iOS 27 or later. The sample requests camera and photo library access at runtime.

#### Configure the Sample Code Project

The sample declares two background modes so ScreenCaptureKit continues to run while the app isn’t frontmost:

- `screen-capture` in [`UIBackgroundModes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/UIBackgroundModes), so the stream survives backgrounding for full-display capture.
- `audio`, so the microphone tap keeps producing samples.

The Info property list also declares [`NSCameraUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSCameraUsageDescription) and [`NSPhotoLibraryAddUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSPhotoLibraryAddUsageDescription). Verify both prompts appear the first time you exercise the in-app capture and recording flows.

#### Present the Content Sharing Picker

The sample offers two entry points into the system picker: a full-display capture and an in-app capture. Both configure the shared [`SCContentSharingPicker`](sccontentsharingpicker.md) and register an observer before presenting the picker, so the app receives the resulting [`SCContentFilter`](sccontentfilter.md) regardless of which mode the person chooses.

For full-display capture, the sample calls [`present()`](sccontentsharingpicker/present().md). For in-app capture, it calls [`presentForCurrentApplication()`](sccontentsharingpicker/presentforcurrentapplication().md), which limits the picker to windows and layers owned by the running app.

```swift
func presentFullDisplayPicker() {
    picker.defaultConfiguration = fullDisplayPickerConfiguration
    activatePicker()
    captureMode = .fullDisplay
    picker.present()
}

func presentInAppPicker() {
    picker.defaultConfiguration = inAppPickerConfiguration
    activatePicker()
    captureMode = .inApp
    picker.presentForCurrentApplication()
}
```

Activating the picker registers the sample’s [`SCContentSharingPickerObserver`](sccontentsharingpickerobserver.md), so the app receives the selected filter through [`contentSharingPicker(_:didUpdateWith:for:)`](sccontentsharingpickerobserver/contentsharingpicker(_:didupdatewith:for:).md) and starts the stream from that callback.

#### Configure the Pickers Controls

The sample uses two [`SCContentSharingPickerConfiguration`](sccontentsharingpickerconfiguration-c.class.md) instances so it can tailor the picker to each capture mode. Both configurations allow toggling the microphone; only the in-app configuration enables the camera toggle, because ScreenCaptureKit doesn’t support a camera overlay for full-display captures.

```swift
var fullDisplayPickerConfiguration: SCContentSharingPickerConfiguration {
    var config = SCContentSharingPickerConfiguration()
    config.showsMicrophoneControl = showsMicrophoneControl
    return config
}

var inAppPickerConfiguration: SCContentSharingPickerConfiguration {
    var config = SCContentSharingPickerConfiguration()
    config.showsMicrophoneControl = showsMicrophoneControl
    config.showsCameraControl = showsCameraControl
    return config
}
```

The picker records the person’s choices in the returned filter’s [`isMicrophoneEnabled`](sccontentfilter/ismicrophoneenabled.md) and [`isCameraEnabled`](sccontentfilter/iscameraenabled.md) properties, which the sample checks when it attaches stream outputs.

#### Start a Stream From the Filter

Once the picker returns a filter, the sample tears down any prior stream and builds a fresh [`SCStream`](scstream.md) with a new [`SCStreamConfiguration`](scstreamconfiguration.md). Screen frames flow through an output attached with the [`SCStreamOutputType.screen`](scstreamoutputtype/screen.md) type. The sample attaches a microphone output only when the filter’s [`isMicrophoneEnabled`](sccontentfilter/ismicrophoneenabled.md) is `true`, mirroring the person’s selection in the picker.

```swift
let newStream = SCStream(filter: filter,
                         configuration: config,
                         delegate: self)
// Add screen stream output for every new stream.
try newStream.addStreamOutput(self, type: .screen,
                              sampleHandlerQueue: .main)
if filter.isMicrophoneEnabled {
    try newStream.addStreamOutput(self, type: .microphone,
                                  sampleHandlerQueue: .main)
}
...
try await newStream.startCapture()
```

Before starting a full-display capture, the sample activates an [`AVAudioSession`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession) in the [`playAndRecord`](https://developer.apple.com/documentation/AVFAudio/AVAudioSession/Category-swift.struct/playAndRecord) category so the microphone tap keeps producing samples while the app runs in the background.

#### Record the Stream to a File

The sample uses [`SCRecordingOutput`](screcordingoutput.md) to encode the stream directly to an MP4 file, so the code doesn’t need to handle sample buffers manually. It configures an output URL in the temporary directory through [`SCRecordingOutputConfiguration`](screcordingoutputconfiguration.md), adds the output to the running stream, and lets ScreenCaptureKit encode the file in place.

```swift
let config = SCRecordingOutputConfiguration()
config.outputURL = outputURL
...
let output = SCRecordingOutput(configuration: config,
                               delegate: delegate)
try stream.addRecordingOutput(output)
```

When the person stops the recording, the sample removes the output and awaits its finalization through a [`CheckedContinuation`](https://developer.apple.com/documentation/Swift/CheckedContinuation). The delegate’s [`recordingOutputDidFinishRecording(_:)`](screcordingoutputdelegate/recordingoutputdidfinishrecording(_:).md) callback resumes the continuation, at which point the sample hands the file to Photos. The Recent tab later reads [`recordedDuration`](screcordingoutput/recordedduration.md) and [`recordedFileSize`](screcordingoutput/recordedfilesize.md) from the finished `SCRecordingOutput` to display the recording’s duration and size.

#### Save Clips From a Rolling Buffer

For quick clips, the sample attaches an [`SCClipBufferingOutput`](scclipbufferingoutput.md) to the same stream. The buffering output holds up to 15 seconds of rolling capture in memory without writing anything to disk. When the person taps Export Current Clip, the sample asks the output to write the most recent N seconds to a file.

```swift
let output = SCClipBufferingOutput(delegate: delegate)
try stream.addClipBufferingOutput(output)
...
// Later, in response to a user action:
output.exportClip(to: clipURL, duration: duration) { [weak self] error in
    ...
    // Save the clip to Photos on success.
    await self?.saveClipToPhotos(url: clipURL)
    ...
}
```

Exporting a clip doesn’t interrupt buffering, so the person can capture overlapping clips while the buffer continues to accumulate new frames.

#### Preview the Camera During Capture

In-app capture mode supports an overlay of the device’s camera. When the filter’s [`isCameraEnabled`](sccontentfilter/iscameraenabled.md) is `true`, the sample attaches an [`SCVideoEffectOutput`](scvideoeffectoutput.md) and stores the [`UIView`](https://developer.apple.com/documentation/UIKit/UIView) the output vends. A [`UIViewRepresentable`](https://developer.apple.com/documentation/SwiftUI/UIViewRepresentable) wrapper embeds that view in the SwiftUI hierarchy so it renders as a floating rounded rectangle anchored to the bottom-trailing corner of the app.

```swift
if captureMode == .inApp && filter.isCameraEnabled,
    let device = AVCaptureDevice.default(.builtInWideAngleCamera,
                                         for: .video,
                                         position: .front) {
    let effectOutput = SCVideoEffectOutput(cameraDevice: device)
    try newStream.addVideoEffectOutput(effectOutput)
    videoEffectOutput = effectOutput
}
```

The sample re-attaches the preview when the app returns to the foreground, because the camera view’s underlying capture session pauses on backgrounding.

#### Save Recordings to Photos

When a recording or clip finishes, the sample writes it to Photos through [`PHPhotoLibrary`](https://developer.apple.com/documentation/Photos/PHPhotoLibrary). Because the sample only writes to Photos, it requests the narrower [`PHAccessLevel.addOnly`](https://developer.apple.com/documentation/Photos/PHAccessLevel/addOnly) authorization scope rather than full library access — the data-minimization pattern of requesting only what the feature needs. The sample hands the file off with [`shouldMoveFile`](https://developer.apple.com/documentation/Photos/PHAssetResourceCreationOptions/shouldMoveFile) set to `true` so the temporary file doesn’t linger on disk.

```swift
let status = await PHPhotoLibrary.requestAuthorization(for: .addOnly)
guard status == .authorized || status == .limited else { return }
...
try await PHPhotoLibrary.shared().performChanges {
    let options = PHAssetResourceCreationOptions()
    options.shouldMoveFile = true
    let request = PHAssetCreationRequest.forAsset()
    request.addResource(with: .video, fileURL: url, options: options)
}
```

The Recent tab surfaces the last saved recording and clip and exposes both through [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink), so the person can pass a file to another app without leaving the sample.

## See Also

- [ScreenCaptureKit updates](../Updates/ScreenCaptureKit.md)
  Learn about important changes to ScreenCaptureKit.
- [Persistent Content Capture](../BundleResources/Entitlements/com.apple.developer.persistent-content-capture.md)
  A Boolean value that indicates whether a Virtual Network Computing (VNC) app needs persistent access to screen capture.
- [Capturing screen content in macOS](capturing-screen-content-in-macos.md)
  Stream desktop content like displays, apps, and windows by adopting screen capture in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/capturing-screen-content-on-ios)*