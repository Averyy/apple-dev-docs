# TVImageType

**Framework**: TVMLKit  
**Kind**: enum

The type of image.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
enum TVImageType
```

## Topics

### Constants
- [TVImageType.image](tvimagetype/image.md)
  The image is presented in its actual size.
- [TVImageType.fullscreen](tvimagetype/fullscreen.md)
  The image occupies the entire screen.
- [TVImageType.decoration](tvimagetype/decoration.md)
  The image is a decoration image, which is used to display an image inside of another image.
- [TVImageType.hero](tvimagetype/hero.md)
  The image is a hero image, which is used to display a product image.
### Initializers
- [init?(rawValue: Int)](tvimagetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var url: URL?](tvimageelement/url.md)
  A URL that points to the location of the image.
- [var imageType: TVImageType](tvimageelement/imagetype.md)
  The type of image.
- [var srcset: [String : URL]?](tvimageelement/srcset.md)
  A dictionary specifying versions of the same image for different resolutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvimagetype)*