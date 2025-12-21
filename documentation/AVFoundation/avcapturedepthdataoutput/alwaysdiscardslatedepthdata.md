# alwaysDiscardsLateDepthData

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that determines whether the capture output should discard any depth data that is not processed before the next depth data is captured.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var alwaysDiscardsLateDepthData: Bool { get set }
```

#### Discussion

If the [`delegateCallbackQueue`](avcapturedepthdataoutput/delegatecallbackqueue.md) dispatch queue is blocked when new depth data is captured, this property determines whether the capture output allows your delegate object more time to process old depth data. If this property’s value is [`false`](https://developer.apple.com/documentation/Swift/false), the capture output delivers old data to your delegate as soon as possible, but application memory usage may increase as a result. The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var isFilteringEnabled: Bool](avcapturedepthdataoutput/isfilteringenabled.md)
  A Boolean value that determines whether the depth data output should filter depth data to smooth out noise and fill invalid values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedepthdataoutput/alwaysdiscardslatedepthdata)*