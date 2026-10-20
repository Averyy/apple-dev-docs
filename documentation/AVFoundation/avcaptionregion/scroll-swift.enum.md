# AVCaptionRegion.Scroll

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the scrolling effects the system applies to a region.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
enum Scroll
```

```c
enum AVCaptionRegionScroll : NSInteger;
```

## Topics

### Scroll values
- [AVCaptionRegion.Scroll.none](./scroll-swift.enum/none.md)
  A type that indicates no scrolling.
- [AVCaptionRegion.Scroll.rollUp](./scroll-swift.enum/rollup.md)
  A type that indicates a roll-up scroll effect.
### Initializers
- [init?(rawValue: Int)](./scroll-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the scroll mode
- [var scroll: AVCaptionRegion.Scroll](./scroll-swift.property.md)
  The scroll mode of the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionregion/scroll-swift.enum)*