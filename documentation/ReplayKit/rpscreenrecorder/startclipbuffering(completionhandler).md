# startClipBuffering(completionHandler:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Starts buffering a clip recording.

**Availability**:
- iOS 15.0+ - Deprecated in 27.0
- iPadOS 15.0+ - Deprecated in 27.0
- Mac Catalyst 15.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.0
- tvOS 15.2+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use ScreenCaptureKit SCStream with SCClipBufferingOutput instead

## Declaration

```swift
func startClipBuffering(completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func startClipBuffering() async throws
```

```objc
- (void) startClipBufferingWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func startClipBuffering() async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `completionHandler`: The system invokes this closure when recording starts. The system passes an error object to the closure if it encountered a problem.

## See Also

### Performing Clip Recording
- [func stopClipBuffering(completionHandler: (((any Error)?) -> Void)?)](./stopclipbuffering%28completionhandler%29.md)
  Stops buffering a clip recording.
- [func exportClip(to: URL, duration: TimeInterval, completionHandler: (((any Error)?) -> Void)?)](./exportclip%28to,duration,completionhandler%29.md)
  Exports a clip recording to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/startclipbuffering(completionhandler:))*