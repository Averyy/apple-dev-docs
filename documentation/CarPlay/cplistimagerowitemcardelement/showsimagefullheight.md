# showsImageFullHeight

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to use a full-height image for the card.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var showsImageFullHeight: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL showsImageFullHeight;
```

## Discussion

When the value of this property is `true`, the element scales its image to fill the entire card. A card with a full-height image doesn’t draw a background color, and it layers the title and subtitle text over a portion of the image. When the value of this property is `false`, the card fills the background with the tint color and scales the image to fit only a portion of the total space.

The value in this property affects the maximum dimensions you use for your images. When the value is `true`, use the dimensions in the [`maximumFullHeightImageSize`](./maximumfullheightimagesize.md) property. When the value is `false`, use the dimensions in the [`maximumImageSize`](./maximumimagesize.md) property.

## See Also

### Getting the image behavior
- [var thumbnail: CPThumbnailImage?](./thumbnail.md)
  The thumbnail object that provides the image content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcardelement/showsimagefullheight)*