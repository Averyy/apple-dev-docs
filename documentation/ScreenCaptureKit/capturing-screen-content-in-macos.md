# Capturing screen content in macOS

**Framework**: ScreenCaptureKit

Stream desktop content like displays, apps, and windows by adopting screen capture in your app.

**Availability**:
- macOS 15.0+
- Xcode 16.0+

#### Overview

This sample shows how to add high-performance screen capture to your Mac app by using [`ScreenCaptureKit`](ScreenCaptureKit.md). The sample explores how to create content filters to capture the displays, apps, and windows you choose. It then shows how to configure your stream output, retrieve video frames and audio samples, and update a running stream.

> **Note**: This sample code project is associated with WWDC24 session 10088: [`Capture HDR content with ScreenCaptureKit`](https://developer.apple.comhttps://developer.apple.com/wwdc24/10088/).

##### Configure the Sample Code Project

To run this sample app, you’ll need the following:

- A Mac with macOS 15 or later
- Xcode 16 or later

The first time you run this sample, the system prompts you to grant the app Screen Recording permission. After you grant permission, you need to restart the app to enable capture.

##### Create a Content Filter

Displays, running apps, and windows are the shareable content on a device. The sample uses the [`SCShareableContent`](scshareablecontent.md) class to retrieve the items in the form of [`SCDisplay`](scdisplay.md), [`SCRunningApplication`](scrunningapplication.md), and [`SCWindow`](scwindow.md) objects respectively.

```swift
// Retrieve the available screen content to capture.
let availableContent = try await SCShareableContent.excludingDesktopWindows(false,
                                                                            onScreenWindowsOnly: true)
```

Before the sample begins capture, it creates an [`SCContentFilter`](sccontentfilter.md) object to specify the content to capture. The sample provides two options that allow for capturing either a single window or an entire display. When the capture type is set to capture a window, the app creates a content filter that only includes that window.

```swift
// Create a content filter that includes a single window.
filter = SCContentFilter(desktopIndependentWindow: window)
```

When a user specifies to capture the entire display, the sample creates a filter to capture only content from the main display. To illustrate filtering a running app, the sample contains a toggle to specify whether to exclude the sample app from the stream.

```swift
var excludedApps = [SCRunningApplication]()
// If a user chooses to exclude the app from the stream,
// exclude it by matching its bundle identifier.
if isAppExcluded {
    excludedApps = availableApps.filter { app in
        Bundle.main.bundleIdentifier == app.bundleIdentifier
    }
}
// Create a content filter with excluded apps.
filter = SCContentFilter(display: display,
                         excludingApplications: excludedApps,
                         exceptingWindows: [])
```

##### Create a Stream Configuration

An [`SCStreamConfiguration`](scstreamconfiguration.md) object provides properties to configure the stream’s output size, pixel format, audio capture settings, and more. The app’s configuration throttles frame updates to 60 fps, and configures the number of frames to keep in the queue at 5. Specifying more frames uses more memory, but may allow for processing frame data without stalling the display stream. The default value is 3 and shouldn’t exceed 8 frames.

```swift
var streamConfig = SCStreamConfiguration()

if let dynamicRangePreset = selectedDynamicRangePreset?.scDynamicRangePreset {
    streamConfig = SCStreamConfiguration(preset: dynamicRangePreset)
}

// Configure audio capture.
streamConfig.capturesAudio = isAudioCaptureEnabled
streamConfig.excludesCurrentProcessAudio = isAppAudioExcluded
streamConfig.captureMicrophone = isMicCaptureEnabled

// Configure the display content width and height.
if captureType == .display, let display = selectedDisplay {
    streamConfig.width = display.width * scaleFactor
    streamConfig.height = display.height * scaleFactor
}

// Configure the window content width and height.
if captureType == .window, let window = selectedWindow {
    streamConfig.width = Int(window.frame.width) * 2
    streamConfig.height = Int(window.frame.height) * 2
}

// Set the capture interval at 60 fps.
streamConfig.minimumFrameInterval = CMTime(value: 1, timescale: 60)

// Increase the depth of the frame queue to ensure high fps at the expense of increasing
// the memory footprint of WindowServer.
streamConfig.queueDepth = 5
```

##### Start the Capture Session

The sample uses the content filter and stream configuration to initialize a new instance of [`SCStream`](scstream.md). To retrieve audio and video sample data, the app adds stream outputs that capture media of the specified type. When the stream captures new sample buffers, it delivers them to its stream output object on the indicated dispatch queues.

```swift
stream = SCStream(filter: filter, configuration: configuration, delegate: streamOutput)

// Add a stream output to capture screen content.
try stream?.addStreamOutput(streamOutput, type: .screen, sampleHandlerQueue: videoSampleBufferQueue)
try stream?.addStreamOutput(streamOutput, type: .audio, sampleHandlerQueue: audioSampleBufferQueue)
try stream?.addStreamOutput(streamOutput, type: .microphone, sampleHandlerQueue: micSampleBufferQueue)
stream?.startCapture()
```

After the stream starts, further changes to its configuration and content filter don’t require restarting it. Instead, after you update the capture configuration in the user interface, the sample creates new stream configuration and content filter objects and applies them to the running stream to update its state.

```swift
try await stream?.updateConfiguration(configuration)
try await stream?.updateContentFilter(filter)
```

##### Process the Output

When a stream captures a new audio or video sample buffer, it calls the stream output’s [`stream(_:didOutputSampleBuffer:of:)`](scstreamoutput/stream(_:didoutputsamplebuffer:of:).md) method, passing it the captured data and an indicator of its type. The stream output evaluates and processes the sample buffer as shown below.

```swift
func stream(_ stream: SCStream, didOutputSampleBuffer sampleBuffer: CMSampleBuffer, of outputType: SCStreamOutputType) {
    
    // Return early if the sample buffer is invalid.
    guard sampleBuffer.isValid else { return }
    
    // Determine which type of data the sample buffer contains.
    switch outputType {
    case .screen:
		// Process the screen content.
    case .audio:
		// Process the audio content.
    }
}
```

##### Process a Video Sample Buffer

If the sample buffer contains video data, it retrieves the sample buffer attachments that describe the output video frame.

```swift
// Retrieve the array of metadata attachments from the sample buffer.
guard let attachmentsArray = CMSampleBufferGetSampleAttachmentsArray(sampleBuffer,
                                                                     createIfNecessary: false) as? [[SCStreamFrameInfo: Any]],
      let attachments = attachmentsArray.first else { return nil }
```

An [`SCStreamFrameInfo`](scstreamframeinfo.md) structure defines dictionary keys that the sample uses to retrieve metadata attached to a sample buffer. Metadata includes information about the frame’s display time, scale factor, status, and more. To determine whether a frame is available for processing, the sample inspects the status for [`SCFrameStatus.complete`](scframestatus/complete.md).

```swift
// Validate the status of the frame. If it isn't `.complete`, return nil.
guard let statusRawValue = attachments[SCStreamFrameInfo.status] as? Int,
      let status = SCFrameStatus(rawValue: statusRawValue),
      status == .complete else { return nil }
```

The sample buffer wraps a [`CVPixelBuffer`](https://developer.apple.comhttps://developer.apple.com/documentation/corevideo/cvpixelbuffer) that’s backed by an [`IOSurface`](https://developer.apple.comhttps://developer.apple.com/documentation/iosurface). The sample casts the surface reference to an `IOSurface` that it later sets as the layer content of an [`NSView`](https://developer.apple.comhttps://developer.apple.com/documentation/appkit/nsview).

```swift
// Get the pixel buffer that contains the image data.
guard let pixelBuffer = sampleBuffer.imageBuffer else { return nil }

// Get the backing IOSurface.
guard let surfaceRef = CVPixelBufferGetIOSurface(pixelBuffer)?.takeUnretainedValue() else { return nil }
let surface = unsafeBitCast(surfaceRef, to: IOSurface.self)

// swiftlint:disable force_cast
// Retrieve the content rectangle, scale, and scale factor.
guard let contentRectDict = attachments[.contentRect],
      let contentRect = CGRect(dictionaryRepresentation: contentRectDict as! CFDictionary),
      let contentScale = attachments[.contentScale] as? CGFloat,
      let scaleFactor = attachments[.scaleFactor] as? CGFloat else { return nil }

// Create a new frame with the relevant data.
let frame = CapturedFrame(surface: surface,
                          contentRect: contentRect,
                          contentScale: contentScale,
                          scaleFactor: scaleFactor)
```

##### Process an Audio Sample Buffer

If the sample buffer contains audio, it retrieves the data as an [`AudioBufferList`](https://developer.apple.comhttps://developer.apple.com/documentation/coreaudiotypes/audiobufferlist) as shown below.

```swift
private func handleAudio(for buffer: CMSampleBuffer) -> Void? {
    // Create an AVAudioPCMBuffer from an audio sample buffer.
    try? buffer.withAudioBufferList { audioBufferList, blockBuffer in
        guard let description = buffer.formatDescription?.audioStreamBasicDescription,
              let format = AVAudioFormat(standardFormatWithSampleRate: description.mSampleRate, channels: description.mChannelsPerFrame),
              let samples = AVAudioPCMBuffer(pcmFormat: format, bufferListNoCopy: audioBufferList.unsafePointer)
        else { return }
        pcmBufferHandler?(samples)
    }
}
```

The app retrieves the audio stream basic description that it uses to create an [`AVAudioFormat`](https://developer.apple.comhttps://developer.apple.com/documentation/avfaudio/avaudioformat). It then uses the format and the audio buffer list to create a new instance of [`AVAudioPCMBuffer`](https://developer.apple.comhttps://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer). If you enable audio capture in the user interface, the sample uses the buffer to calculate average levels for the captured audio to display in a simple level meter.

## See Also

- [ScreenCaptureKit updates](../Updates/ScreenCaptureKit.md)
  Learn about important changes to ScreenCaptureKit.
- [Persistent Content Capture](../BundleResources/Entitlements/com.apple.developer.persistent-content-capture.md)
  A Boolean value that indicates whether a Virtual Network Computing (VNC) app needs persistent access to screen capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/capturing-screen-content-in-macos)*