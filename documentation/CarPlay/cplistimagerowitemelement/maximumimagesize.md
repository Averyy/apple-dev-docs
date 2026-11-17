# maximumImageSize

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The maximum dimensions for the element’s image.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class var maximumImageSize: CGSize { get }
```

```objc
@property (class, nonatomic, readonly) CGSize maximumImageSize;
```

## Discussion

Use this property to retrieve the standard maximum image dimensions for images. Card elements define an additional set of dimensions for images that fill the content.

When the [`showsImageFullHeight`](../cplistimagerowitemcardelement/showsimagefullheight.md) property is `false`, this property defines the maximum size for images. When creating images, adjust the size of your image based on the current maximum value.

## See Also

### Getting the element’s content
- [var image: UIImage](./image.md)
  The image associated with the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemelement/maximumimagesize)*