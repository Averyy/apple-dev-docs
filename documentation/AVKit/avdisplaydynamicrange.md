# AVDisplayDynamicRange

**Framework**: AVKit  
**Kind**: enum

Describes how High Dynamic Range (HDR) video content renders.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
enum AVDisplayDynamicRange
```

## Topics

### Enumeration Cases
- [AVDisplayDynamicRange.automatic](avdisplaydynamicrange/automatic.md)
  Defines an automatic dynamic range. Indicates that the dynamic range will be set automatically.
- [AVDisplayDynamicRange.constrainedHigh](avdisplaydynamicrange/constrainedhigh.md)
  Defines a constrained high dynamic range. Allows for constrained High Dynamic Range (HDR) video content which is useful for mixing HDR and Standard Dynamic Range (SDR) content.
- [AVDisplayDynamicRange.high](avdisplaydynamicrange/high.md)
  Defines a high dynamic range. Allows video content to use extended dynamic range if it has dynamic range content.
- [AVDisplayDynamicRange.standard](avdisplaydynamicrange/standard.md)
  Defines a standard dynamic range. Restricts the video content dynamic range to the standard range regardless of the actual range of the video content.
### Initializers
- [init?(rawValue: Int)](avdisplaydynamicrange/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var preferredDisplayDynamicRange: AVDisplayDynamicRange](avplayerview/preferreddisplaydynamicrange.md)
  Describes how High Dynamic Range (HDR) video content renders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avdisplaydynamicrange)*