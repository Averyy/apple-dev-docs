# getContinuationStreams(completionHandler:)

**Framework**: Foundation  
**Kind**: method

Requests streams back to the originating app.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func continuationStreams() async throws -> (InputStream, OutputStream)
```

#### Discussion

When an app is launched for a continuation event, it can request streams back to the originating app. Streams can be successfully retrieved only from the [`NSUserActivity`](nsuseractivity.md) object in the [`NSApplication`](https://developer.apple.com/documentation/AppKit/NSApplication) or [`UIApplication`](https://developer.apple.com/documentation/UIKit/UIApplication) delegate that is called for a continuation event. The streams are provided by the completion handler in an unopened state, and the delegate should open them immediately to start communicating with the continuing side.

Continuation streams are an optional feature of Handoff, and most user activities do not need them for successful continuation. When streams are needed, a simple request from the continuing app accompanied by a response from the originating app is enough for most continuation events.

## Parameters

- `completionHandler`: The block takes three arguments:

## See Also

- [var supportsContinuationStreams: Bool](nsuseractivity/supportscontinuationstreams.md)
  A Boolean value that determines whether the continuing app can request streams to be opened back to the originating app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/getcontinuationstreams(completionhandler:))*