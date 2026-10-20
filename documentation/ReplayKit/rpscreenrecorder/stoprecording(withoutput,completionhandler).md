# stopRecording(withOutput:completionHandler:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Stops the current recording and writes the movie to the specified output URL.

**Availability**:
- iOS 14.0+ - Deprecated in 27.0
- iPadOS 14.0+ - Deprecated in 27.0
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 14.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use ScreenCaptureKit SCStream with SCRecordingOutput instead

## Declaration

```swift
func stopRecording(withOutput url: URL, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func stopRecording(withOutput url: URL) async throws
```

```objc
- (void) stopRecordingWithOutputURL:(NSURL *) url completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func stopRecording(withOutput url: URL) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `url`: The output URL.
- `completionHandler`: The completion handler the system calls when the movie is written to the specified output URL. If an error occured, the system passes the completion handler an [`NSError`](../../Foundation/nserror.md) that indicates the reason the operation failed.

## See Also

### Controlling App Recording
- [func startRecording(handler: (((any Error)?) -> Void)?)](./startrecording%28handler%29.md)
  Starts recording the app display.
- [func stopRecording(handler: ((RPPreviewViewController?, (any Error)?) -> Void)?)](./stoprecording%28handler%29.md)
  Stops the current recording.
- [func startCapture(handler: ((CMSampleBuffer, RPSampleBufferType, (any Error)?) -> Void)?, completionHandler: (((any Error)?) -> Void)?)](./startcapture%28handler,completionhandler%29.md)
  Starts screen and audio capture.
- [enum RPSampleBufferType](../rpsamplebuffertype.md)
  The type of media clip sample being buffered.
- [func stopCapture(handler: (((any Error)?) -> Void)?)](./stopcapture%28handler%29.md)
  Stops screen capture
- [func discardRecording(handler: () -> Void)](./discardrecording%28handler%29.md)
  Discards the current recording.
- [func startRecording(withMicrophoneEnabled: Bool, handler: (((any Error)?) -> Void)?)](./startrecording%28withmicrophoneenabled,handler%29.md)
  Starts recording the app’s audio and video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/stoprecording(withoutput:completionhandler:))*