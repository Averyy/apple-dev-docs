# TVTopShelfItem.ImageTraits

**Framework**: TV Services  
**Kind**: struct  
**Role**: Structure

Constants describing the image format.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
struct ImageTraits
```

```c
enum TVTopShelfItemImageTraits : NSUInteger;
```

## Topics

### Image Traits
- [static var screenScale1x: TVTopShelfItem.ImageTraits](./imagetraits/screenscale1x.md)
  An image to display on devices running in a 1x resolution mode.
- [static var screenScale2x: TVTopShelfItem.ImageTraits](./imagetraits/screenscale2x.md)
  A high-resolution image to display on devices running in a 2x resolution mode.
### Initializers
- [init(rawValue: UInt)](./imagetraits/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Providing an Image for the Item
- [func imageURL(for: TVTopShelfItem.ImageTraits) -> URL?](./imageurl%28for%29.md)
  Returns an image associated with the current item.
- [func setImageURL(URL?, for: TVTopShelfItem.ImageTraits)](./setimageurl%28_,for%29.md)
  Associates an image with the current item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfitem/imagetraits)*