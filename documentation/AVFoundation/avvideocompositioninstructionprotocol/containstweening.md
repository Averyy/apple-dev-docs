# containsTweening

**Framework**: AVFoundation  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether the composition contains tweening.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var containsTweening: Bool { get }
```

#### Discussion

A value of [`true`](https://developer.apple.com/documentation/Swift/true) indicates that rendering a frame from the same source buffers and the same composition instruction at two different [`compositionTime`](avasynchronousvideocompositionrequest/compositiontime.md) values may yield different output frames. A value of [`false`](https://developer.apple.com/documentation/Swift/false) indicates that two compositions yield the same frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avvideocompositioninstructionprotocol/containstweening)*