# startCapture(handler:completionHandler:)

**Framework**: ReplayKit  
**Kind**: method

Starts screen and audio capture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func startCapture(handler captureHandler: ((CMSampleBuffer, RPSampleBufferType, (any Error)?) -> Void)?) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func startCapture(handler captureHandler: ((CMSampleBuffer, RPSampleBufferType, Error?) -> Void)?) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func startCapture(handler captureHandler: ((CMSampleBuffer, RPSampleBufferType, Error?) -> Void)?) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `captureHandler`: A block that is called continuously during screen capture.
- `completionHandler`: A block that is called when screen capture has started.

## See Also

- [func startRecording(handler: (((any Error)?) -> Void)?)](rpscreenrecorder/startrecording(handler:).md)
  Starts recording the app display.
- [func stopRecording(handler: ((RPPreviewViewController?, (any Error)?) -> Void)?)](rpscreenrecorder/stoprecording(handler:).md)
  Stops the current recording.
- [func stopRecording(withOutput: URL, completionHandler: (((any Error)?) -> Void)?)](rpscreenrecorder/stoprecording(withoutput:completionhandler:).md)
  Stops the current recording and writes the movie to the specified output URL.
- [enum RPSampleBufferType](rpsamplebuffertype.md)
  The type of media clip sample being buffered.
- [func stopCapture(handler: (((any Error)?) -> Void)?)](rpscreenrecorder/stopcapture(handler:).md)
  Stops screen capture
- [func discardRecording(handler: () -> Void)](rpscreenrecorder/discardrecording(handler:).md)
  Discards the current recording.
- [func startRecording(withMicrophoneEnabled: Bool, handler: (((any Error)?) -> Void)?)](rpscreenrecorder/startrecording(withmicrophoneenabled:handler:).md)
  Starts recording the app’s audio and video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/startcapture(handler:completionhandler:))*