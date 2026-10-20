# supportsContinuationStreams

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property BOOL supportsContinuationStreams;
```

#### Discussion

If the value of this property is [`true`](../../Swift/true.md), the continuing app can connect back to the originating app for more information using streams. The default value of this property is [`false`](../../Swift/false.md). It can dynamically be set to [`true`](../../Swift/true.md) to selectively support continuation streams based on the state of the user activity.

## See Also

### Working with continuation streams
- [func getContinuationStreams(completionHandler: (InputStream?, OutputStream?, (any Error)?) -> Void)](./getcontinuationstreams%28completionhandler%29.md)
  Requests streams back to the originating app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/supportscontinuationstreams)*