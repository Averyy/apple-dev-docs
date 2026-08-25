# Building a responsive camera app that launches quickly

**Framework**: AVFoundation

Show a camera preview sooner by deferring capture output setup and postponing noncritical interface elements.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

Someone who opens your camera app wants to see a preview immediately. A capture session takes time to configure, because it prepares every output you add before it starts delivering data. Showing a preview requires almost none of that work, so it can appear while the session finishes the rest.

AVCam adopts deferred start in `CaptureService`, the actor that manages its capture pipeline, so the preview doesn’t wait for the photo and movie outputs to start. The app postpones part of its interface for the same reason: controls that depend on a running session stay hidden until one is running.

The same smoothness matters when the app returns from the background. A preview that isn’t covered on the way out comes back holding a stale frame, and covering it after frames stop arriving is too late. AVCam covers the preview as the app leaves, then fades the cover away as live frames resume. For more information about the app’s design, see [`AVCam: Building a camera app`](avcam-building-a-camera-app.md).

> **Note**: This sample code project is associated with WWDC26 session 303: [`Build a responsive camera app that launches quickly`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc26/303/).

#### Configure the Sample Code Project

Because Simulator doesn’t have access to device cameras, run the sample on a device. To build and run it, you need the following:

- Xcode 27 or later
- A device running iOS or iPadOS 26 or later

#### Defer Starting Noncritical Outputs

Preparing capture outputs is one of the more expensive parts of starting a capture session, and rendering a preview requires none of them. A photo or movie output matters only the moment someone takes a picture or starts recording, which is always later than the moment the preview appears. Deferred start separates those two events: the session brings up the preview path first, then prepares the remaining outputs after the preview is onscreen.

Linking the iOS 26 SDK enables both halves of this behavior by default: the session runs deferred start automatically, and a photo output or a file output defers its start whenever it supports deferral. Every other output type stays undeferred, so an output that feeds preview keeps working as it always has. AVCam sets both values explicitly, so the code shows which properties control the behavior.

The `CaptureService` actor makes the assignments while configuring the session:

```swift
// Configure the session preset based on the current capture mode.
captureSession.sessionPreset = captureMode == .photo ? .photo : .high

// Deferred start brings up the preview first, and prepares the capture outputs a moment
// later. An app that links the iOS 26 SDK gets this behavior by default; these
// assignments show the properties that control it.
captureSession.automaticallyRunsDeferredStart = true

// Add the photo capture output as the default output type.
photoCapture.output.isDeferredStartEnabled = photoCapture.output.isDeferredStartSupported
try addOutput(photoCapture.output)
// If the capture mode is set to `video`, add a movie capture output.
if captureMode == .video {
    // Add the movie output as the default output type.
    movieCapture.output.isDeferredStartEnabled = movieCapture.output.isDeferredStartSupported
    try addOutput(movieCapture.output)
    setHDRVideoEnabled(isHDRVideoEnabled)
}
```

Each output tests [`isDeferredStartSupported`](avcaptureoutput/isdeferredstartsupported.md) before enabling [`isDeferredStartEnabled`](avcaptureoutput/isdeferredstartenabled.md), because enabling it on an output that doesn’t support deferral throws an exception. Because the property defers starting an output, not adding one, the sample still adds the movie output only in video mode. The code doesn’t touch [`AVCaptureVideoPreviewLayer`](avcapturevideopreviewlayer.md), which defaults to not deferring because its job is to display preview.

AVCam uses automatic mode, in which the session chooses when to start the deferred outputs. The preview layer is the only client the app doesn’t defer. The session runs the deferred start shortly after the layer displays its first frame. An app that leaves a data-providing output undeferred waits longer, because the session waits for that output’s first frame instead. An app that draws camera frames itself, such as one rendering [`AVCaptureVideoDataOutput`](avcapturevideodataoutput.md) buffers into a `CAMetalLayer`, knows that moment when the session can’t. It sets [`automaticallyRunsDeferredStart`](avcapturesession/automaticallyrunsdeferredstart.md) to `false` and calls [`runDeferredStartWhenNeeded()`](avcapturesession/rundeferredstartwhenneeded().md) instead.

#### Hide Controls Until the Session Runs

A mode picker, a thumbnail of the last capture, and a camera-switching button all depend on a running session, so showing them before one exists puts controls onscreen that can’t do anything. AVCam keeps them hidden until the session runs, which also leaves the preview alone onscreen as it appears.

AVCam defines a view modifier for that condition. In the following code example, `hidden(until:)` fades a view in and out as the session’s state changes:

```swift
extension View {
    /// Hides this view until the capture session is running.
    func hidden(until isRunning: Bool) -> some View {
        opacity(isRunning ? 1 : 0)
            .animation(.easeIn(duration: 0.3), value: isRunning)
    }
}
```

Fading opacity rather than adding and removing the views keeps the layout fixed, so controls don’t shift position as the session comes up.

The main toolbar applies the modifier to the controls that depend on the session, and deliberately doesn’t apply it to one of them:

```swift
var body: some View {
    HStack {
        ThumbnailButton(camera: camera)
            .hidden(until: camera.status == .running)
        Spacer()
        // The capture button stays visible, because a capture that arrives before
        // the deferred start finishes is still honored.
        CaptureButton(camera: camera)
        Spacer()
        SwitchCameraButton(camera: camera)
            .hidden(until: camera.status == .running)
    }
}
```

The capture button stays onscreen throughout. When a shutter press arrives before the deferred outputs finish starting, the session runs the deferred start on the app’s behalf to service it. The photo output also enables responsive capture, which lets more than one press queue before that start completes.

#### Cover the Preview in the Background

A preview that isn’t covered can reappear holding the last frame it rendered before the app entered the background. Covering it after frames stop arriving is too late. Instead, the app covers the preview on its way out and reveals it when it’s active again.

In the following code example, `PreviewContainer` observes the scene phase and sets the opacity of a black overlay from it:

```swift
var previewView: some View {
    content
        .blur(radius: blurRadius, opaque: true)
        .overlay(Color.black.opacity(coverOpacity))
        .onChange(of: camera.isSwitchingModes, updateBlurRadius(_:_:))
        .onChange(of: camera.isSwitchingVideoDevices, updateBlurRadius(_:_:))
        .onChange(of: scenePhase, updateCoverOpacity(_:_:))
}

/// Cover the preview as the app enters the background, and reveal it on return.
func updateCoverOpacity(_: ScenePhase, _ phase: ScenePhase) {
    switch phase {
    case .background:
        coverOpacity = 1
    case .active:
        withAnimation(.easeIn(duration: 0.3)) {
            coverOpacity = 0
        }
    default:
        break
    }
}
```

The cover appears without animation, because the app doesn’t have time to animate as it enters the background. On return, the app fades the cover out instead of immediately removing it, which smooths the return to a live preview without needing a signal that frames have resumed.

## See Also

- [Setting up a capture session](setting-up-a-capture-session.md)
  Configure input devices, output media, preview views, and basic settings before capturing photos or video.
- [Accessing the camera while multitasking on iPad](../avkit/accessing-the-camera-while-multitasking-on-ipad.md)
  Operate the camera in Split View, Slide Over, Picture in Picture, and Stage Manager modes.
- [AVCam: Building a camera app](avcam-building-a-camera-app.md)
  Capture photos and record video using the front and rear iPhone and iPad cameras.
- [Capturing Cinematic video](capturing-cinematic-video.md)
  Capture video with an adjustable depth of field and focus points.
- [Supporting Center Stage front camera in your iOS app](supporting-center-stage-front-camera-in-your-ios-app.md)
  Enable Center Stage for photos and videos on the iPhone front camera.
- [AVMultiCamPiP: Capturing from Multiple Cameras](avmulticampip-capturing-from-multiple-cameras.md)
  Simultaneously record the output from the front and back cameras into a single movie file by using a multi-camera capture session.
- [AVCamBarcode: detecting barcodes and faces](avcambarcode-detecting-barcodes-and-faces.md)
  Identify machine readable codes or faces by using the camera.
- [class AVCaptureSession](avcapturesession.md)
  An object that configures capture behavior and coordinates the flow of data from input devices to capture outputs.
- [class AVCaptureMultiCamSession](avcapturemulticamsession.md)
  A capture session that supports simultaneous capture from multiple inputs of the same media type.
- [class AVCaptureInput](avcaptureinput.md)
  An abstract superclass for objects that provide input data to a capture session.
- [class AVCaptureOutput](avcaptureoutput.md)
  An abstract superclass for objects that provide media output destinations for a capture session.
- [class AVCaptureConnection](avcaptureconnection.md)
  An object that represents a connection from a capture input to a capture output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/building-a-responsive-camera-app-that-launches-quickly)*