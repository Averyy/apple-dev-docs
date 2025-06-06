# RPScreenRecorder

**Framework**: ReplayKit  
**Kind**: class

The shared recorder object that provides the ability to record audio and video of your app.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class RPScreenRecorder
```

#### Overview

Apps on a user’s device can share the recording function, with each app having its own instance of  `RPScreenRecorder`. Your app can record the audio and video inside of the app, along with user commentary through the microphone. You get a reference to the recorder through the [`shared()`](rpscreenrecorder/shared().md) function and use it to implement start-and-stop recording functionality. You can present a user interface (view controller) where a user can trim and preview recordings, and share them with other users. Only one app at a time can use the recorder on the user’s device. Your app can’t record video from [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer).

## Topics

### Accessing the Shared Recorder
- [class func shared() -> RPScreenRecorder](rpscreenrecorder/shared.md)
  Returns an app’s instance of the shared screen recorder.
### Inspecting a Screen Recorder
- [var isAvailable: Bool](rpscreenrecorder/isavailable.md)
  A Boolean value that indicates whether the screen recorder is available for recording.
- [var isRecording: Bool](rpscreenrecorder/isrecording.md)
  A Boolean value that indicates whether the app is currently recording.
- [var isMicrophoneEnabled: Bool](rpscreenrecorder/ismicrophoneenabled.md)
  A Boolean value that indicates whether the microphone is currently enabled.
- [var isCameraEnabled: Bool](rpscreenrecorder/iscameraenabled.md)
  A Boolean value that indicates whether the camera is currently enabled.
- [var cameraPreviewView: UIView?](rpscreenrecorder/camerapreviewview.md)
  A view containing the contents of the front-facing camera.
- [var cameraPosition: RPCameraPosition](rpscreenrecorder/cameraposition.md)
  The camera position to use.
- [enum RPCameraPosition](rpcameraposition.md)
  The position of the camera being accessed.
- [var delegate: (any RPScreenRecorderDelegate)?](rpscreenrecorder/delegate.md)
  The delegate for the screen recorder.
- [protocol RPScreenRecorderDelegate](rpscreenrecorderdelegate.md)
  The protocol you implement to receive notifications from the screen recorder.
### Controlling App Recording
- [func startRecording(handler: (((any Error)?) -> Void)?)](rpscreenrecorder/startrecording(handler:).md)
  Starts recording the app display.
- [func stopRecording(handler: ((RPPreviewViewController?, (any Error)?) -> Void)?)](rpscreenrecorder/stoprecording(handler:).md)
  Stops the current recording.
- [func stopRecording(withOutput: URL, completionHandler: (((any Error)?) -> Void)?)](rpscreenrecorder/stoprecording(withoutput:completionhandler:).md)
  Stops the current recording and writes the movie to the specified output URL.
- [func startCapture(handler: ((CMSampleBuffer, RPSampleBufferType, (any Error)?) -> Void)?, completionHandler: (((any Error)?) -> Void)?)](rpscreenrecorder/startcapture(handler:completionhandler:).md)
  Starts screen and audio capture.
- [enum RPSampleBufferType](rpsamplebuffertype.md)
  The type of media clip sample being buffered.
- [func stopCapture(handler: (((any Error)?) -> Void)?)](rpscreenrecorder/stopcapture(handler:).md)
  Stops screen capture
- [func discardRecording(handler: () -> Void)](rpscreenrecorder/discardrecording(handler:).md)
  Discards the current recording.
- [func startRecording(withMicrophoneEnabled: Bool, handler: (((any Error)?) -> Void)?)](rpscreenrecorder/startrecording(withmicrophoneenabled:handler:).md)
  Starts recording the app’s audio and video.
### Performing Clip Recording
- [func startClipBuffering(completionHandler: (((any Error)?) -> Void)?)](rpscreenrecorder/startclipbuffering(completionhandler:).md)
  Starts buffering a clip recording.
- [func stopClipBuffering(completionHandler: (((any Error)?) -> Void)?)](rpscreenrecorder/stopclipbuffering(completionhandler:).md)
  Stops buffering a clip recording.
- [func exportClip(to: URL, duration: TimeInterval, completionHandler: (((any Error)?) -> Void)?)](rpscreenrecorder/exportclip(to:duration:completionhandler:).md)
  Exports a clip recording to a file.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Recording and Streaming Your macOS App](recording-and-streaming-your-macos-app.md)
  Share screen recordings, or broadcast live audio and video of your app, by adding ReplayKit to your macOS apps and games.
- [class RPPreviewViewController](rppreviewviewcontroller.md)
  An object that displays a user interface where users preview and edit a screen recording that you create with ReplayKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder)*