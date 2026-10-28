# startCapture(handler:completionHandler:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Starts screen and audio capture.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use ScreenCaptureKit SCStream with SCStreamOutput instead

## Declaration

```swift
func startCapture(handler captureHandler: ((CMSampleBuffer, RPSampleBufferType, (any Error)?) -> Void)?, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func startCapture(handler captureHandler: ((CMSampleBuffer, RPSampleBufferType, (any Error)?) -> Void)?) async throws
```

```objc
- (void) startCaptureWithHandler:(void (^)(CMSampleBufferRef sampleBuffer, RPSampleBufferType bufferType, NSError *error)) captureHandler completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func startCapture(handler captureHandler: ((CMSampleBuffer, RPSampleBufferType, Error?) -> Void)?) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `captureHandler`: A block that is called continuously during screen capture.

  - **sampleBuffer**: A [CMSampleBuffer](../../CoreMedia/cmsamplebuffer-api.md) object containing either audio or video data.
  - **bufferType**: An [`RPSampleBufferType`](../rpsamplebuffertype.md) identifying the media type of the recorded sample.
  - **error**: Contains an error code if screen capture failed to start. Otherwise, the value of this parameter is `nil`.
- `completionHandler`: A block that is called when screen capture has started.

  - **error**: If an error occurred, this parameter holds an object that explains the error. Otherwise, the value of this parameter is `nil`. See [`RPRecordingErrorCode`](../rprecordingerrorcode.md) for a list of error codes to ReplayKit.

## See Also

### Controlling App Recording
- [func startRecording(handler: (((any Error)?) -> Void)?)](./startrecording%28handler%29.md)
  Starts recording the app display.
- [func stopRecording(handler: ((RPPreviewViewController?, (any Error)?) -> Void)?)](./stoprecording%28handler%29.md)
  Stops the current recording.
- [func stopRecording(withOutput: URL, completionHandler: (((any Error)?) -> Void)?)](./stoprecording%28withoutput,completionhandler%29.md)
  Stops the current recording and writes the movie to the specified output URL.
- [enum RPSampleBufferType](../rpsamplebuffertype.md)
  The type of media clip sample being buffered.
- [func stopCapture(handler: (((any Error)?) -> Void)?)](./stopcapture%28handler%29.md)
  Stops screen capture
- [func discardRecording(handler: () -> Void)](./discardrecording%28handler%29.md)
  Discards the current recording.
- [func startRecording(withMicrophoneEnabled: Bool, handler: (((any Error)?) -> Void)?)](./startrecording%28withmicrophoneenabled,handler%29.md)
  Starts recording the app’s audio and video.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/startcapture(handler:completionhandler:))*