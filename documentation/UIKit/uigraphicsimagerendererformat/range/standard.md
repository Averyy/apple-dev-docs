# UIGraphicsImageRendererFormat.Range.standard

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

The image renderer context doesn’t support extended colors.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
case standard
```

```c
UIGraphicsImageRendererFormatRangeStandard
```

#### Discussion

If you draw wide-color content into an image renderer context that uses the standard color range, you may lose color information. The system matches the colors to the standard range of their corresponding color space.

## See Also

### Constants
- [UIGraphicsImageRendererFormat.Range.automatic](./automatic.md)
  The system automatically chooses the image renderer context’s pixel format according to the color range of its content.
- [UIGraphicsImageRendererFormat.Range.extended](./extended.md)
  The image renderer context supports wide color.
- [UIGraphicsImageRendererFormat.Range.unspecified](./unspecified.md)
  The image renderer context doesn’t specify a color range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/range/standard)*