# exportClip(to:duration:completionHandler:)

**Framework**: ReplayKit  
**Kind**: method  
**Role**: Instance Method

Exports a clip recording to a file.

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
func exportClip(to url: URL, duration: TimeInterval, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func exportClip(to url: URL, duration: TimeInterval) async throws
```

```objc
- (void) exportClipToURL:(NSURL *) url duration:(NSTimeInterval) duration completionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func exportClip(to url: URL, duration: TimeInterval) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `url`: The URL of the destination file.
- `duration`: The duration for clip recording, in seconds. The system caps the duration at to the elapsed time, or a maximum of 15 seconds, whichever is shorter.
- `completionHandler`: A closure the system calls after it finishes exporting the clip. The system passes an error object to the closure if it encountered a problem writing the clip to disk.

## See Also

### Performing Clip Recording
- [func startClipBuffering(completionHandler: (((any Error)?) -> Void)?)](./startclipbuffering%28completionhandler%29.md)
  Starts buffering a clip recording.
- [func stopClipBuffering(completionHandler: (((any Error)?) -> Void)?)](./stopclipbuffering%28completionhandler%29.md)
  Stops buffering a clip recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/exportclip(to:duration:completionhandler:))*