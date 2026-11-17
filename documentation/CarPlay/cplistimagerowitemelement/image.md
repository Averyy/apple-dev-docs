# image

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The image associated with the element.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@NSCopying
var image: UIImage { get set }
```

```objc
@property (nonatomic, copy) UIImage * image;
```

## Discussion

The image in this property constitutes the element’s primary content. If the image originates from an asset catalog, CarPlay manages the light and dark variants of your image and switches them when needed. If the image is smaller or larger than the dimensions in the [`maximumImageSize`](./maximumimagesize.md) property, CarPlay scales the image as needed to fit the space. Don’t specify an image object with an animated sequence of images.

## See Also

### Getting the element’s content
- [class var maximumImageSize: CGSize](./maximumimagesize.md)
  The maximum dimensions for the element’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemelement/image)*