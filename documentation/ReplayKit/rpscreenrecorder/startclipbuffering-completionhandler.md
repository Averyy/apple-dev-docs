# startClipBuffering(completionHandler:)

**Framework**: ReplayKit  
**Kind**: method

Starts buffering a clip recording.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.2+
- visionOS 1.0+

## Declaration

```swift
func startClipBuffering() async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func startClipBuffering() async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `completionHandler`: The system invokes this closure when recording starts. The system passes an error object to the closure if it encountered a problem.

## See Also

- [func stopClipBuffering(completionHandler: (((any Error)?) -> Void)?)](rpscreenrecorder/stopclipbuffering(completionhandler:).md)
  Stops buffering a clip recording.
- [func exportClip(to: URL, duration: TimeInterval, completionHandler: (((any Error)?) -> Void)?)](rpscreenrecorder/exportclip(to:duration:completionhandler:).md)
  Exports a clip recording to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpscreenrecorder/startclipbuffering(completionhandler:))*