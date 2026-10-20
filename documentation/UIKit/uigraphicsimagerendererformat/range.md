# UIGraphicsImageRendererFormat.Range

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the color range of the image renderer context.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
enum Range
```

```c
enum UIGraphicsImageRendererFormatRange : NSInteger;
```

## Topics

### Constants
- [UIGraphicsImageRendererFormat.Range.automatic](./range/automatic.md)
  The system automatically chooses the image renderer context’s pixel format according to the color range of its content.
- [UIGraphicsImageRendererFormat.Range.extended](./range/extended.md)
  The image renderer context supports wide color.
- [UIGraphicsImageRendererFormat.Range.standard](./range/standard.md)
  The image renderer context doesn’t support extended colors.
- [UIGraphicsImageRendererFormat.Range.unspecified](./range/unspecified.md)
  The image renderer context doesn’t specify a color range.
### Initializers
- [init?(rawValue: Int)](./range/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the renderer attributes
- [var opaque: Bool](./opaque.md)
  A Boolean value that indicates whether the underlying Core Graphics context has an alpha channel.
- [var scale: CGFloat](./scale.md)
  The display scale of the image renderer context.
- [var preferredRange: UIGraphicsImageRendererFormat.Range](./preferredrange.md)
  The preferred color range of the image renderer context.
- [var prefersExtendedRange: Bool](./prefersextendedrange.md)
  A Boolean value that specifies whether the bitmap context uses extended color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/range)*