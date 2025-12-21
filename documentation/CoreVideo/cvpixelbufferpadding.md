# CVPixelBufferPadding

**Framework**: Core Video  
**Kind**: struct

Padding pixels around the CVPixelBuffer

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@frozen
struct CVPixelBufferPadding
```

## Topics

### Initializers
- [init(left: Int, right: Int, top: Int, bottom: Int)](cvpixelbufferpadding/init(left:right:top:bottom:).md)
### Instance Properties
- [var bottom: Int](cvpixelbufferpadding/bottom.md)
  Pixel row padding at the bottom
- [var left: Int](cvpixelbufferpadding/left.md)
  Pixel column padding to the left
- [var right: Int](cvpixelbufferpadding/right.md)
  Pixel column padding to the right
- [var top: Int](cvpixelbufferpadding/top.md)
  Pixel row padding at the top
### Type Properties
- [static let zero: CVPixelBufferPadding](cvpixelbufferpadding/zero.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferpadding)*