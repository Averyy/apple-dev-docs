# TVContentItemImageTrait

**Framework**: TV Services  
**Kind**: struct  
**Role**: Structure

Traits describing the type of image you want.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
struct TVContentItemImageTrait
```

```c
enum TVContentItemImageTrait : NSUInteger;
```

## Topics

### Traits
- [static var screenScale1x: TVContentItemImageTrait](./tvcontentitemimagetrait/screenscale1x.md)
  An image meant for a regular display.
- [static var screenScale2x: TVContentItemImageTrait](./tvcontentitemimagetrait/screenscale2x.md)
  An image meant for a Retina display.
- [static var userInterfaceStyleDark: TVContentItemImageTrait](./tvcontentitemimagetrait/userinterfacestyledark.md)
  An image meant for a dark user interface.
- [static var userInterfaceStyleLight: TVContentItemImageTrait](./tvcontentitemimagetrait/userinterfacestylelight.md)
  An image meant for a light user interface.
### Initializers
- [init(rawValue: UInt)](./tvcontentitemimagetrait/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Accessing Image Resources
- [var imageURL: URL?](./tvcontentitem/imageurl.md)
  A URL giving the location of the image to be displayed for this content item.
- [func imageURL(forTraits: TVContentItemImageTrait) -> URL?](./tvcontentitem/imageurl%28fortraits%29.md)
  Retrieve the URL for the image that best matches the specified traits.
- [func setImageURL(URL?, forTraits: TVContentItemImageTrait)](./tvcontentitem/setimageurl%28_,fortraits%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitemimagetrait)*