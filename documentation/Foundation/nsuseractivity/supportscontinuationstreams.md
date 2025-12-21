# supportsContinuationStreams

**Framework**: Foundation  
**Kind**: property

A Boolean value that determines whether the continuing app can request streams to be opened back to the originating app.

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
var supportsContinuationStreams: Bool { get set }
```

#### Discussion

If the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the continuing app can connect back to the originating app for more information using streams. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false). It can dynamically be set to [`true`](https://developer.apple.com/documentation/Swift/true) to selectively support continuation streams based on the state of the user activity.

## See Also

- [func getContinuationStreams(completionHandler: (InputStream?, OutputStream?, (any Error)?) -> Void)](nsuseractivity/getcontinuationstreams(completionhandler:).md)
  Requests streams back to the originating app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/supportscontinuationstreams)*