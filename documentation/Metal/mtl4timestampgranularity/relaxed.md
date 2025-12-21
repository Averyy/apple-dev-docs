# MTL4TimestampGranularity.relaxed

**Framework**: Metal  
**Kind**: case

A minimally-invasive timestamp which may be less precise.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case relaxed
```

#### Discussion

Using this granularity incurs in the lowest overhead, at the cost of precision. For example, it may sample at command encoder boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4timestampgranularity/relaxed)*