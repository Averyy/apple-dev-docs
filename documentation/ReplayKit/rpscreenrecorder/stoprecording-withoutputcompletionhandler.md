# stopRecording(withOutput:completionHandler:)

**Framework**: ReplayKit  
**Kind**: method

Stops the current recording and writes the movie to the specified output URL.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func stopRecording(withOutput url: URL) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func stopRecording(withOutput url: URL) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `url`: The output URL.
- `completionHandler`: The completion handler the system calls when the movie is written to the specified output URL. If an error occured, the system passes the completion handler an   that indicates the reason the operation failed.

## See Also

- [func startRecording(handler: (((any Error)?) -> Void)?)](rpscreenrecorder/startrecording(handler:).md)
  Starts recording the app display.
- [func stopRecording(handler: ((RPPreviewViewController?, (any Error)?) -> Void)?)](rpscreenrecorder/stoprecording(handler:).md)
  Stops the current recording.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/stoprecording(withoutput:completionhandler:))*