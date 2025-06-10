# TVContentItemImageTrait

**Framework**: TV Services  
**Kind**: struct

Traits describing the type of image you want.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
struct TVContentItemImageTrait
```

## Topics

### Traits
- [static var screenScale1x: TVContentItemImageTrait](tvcontentitemimagetrait/screenscale1x.md)
  An image meant for a regular display.
- [static var screenScale2x: TVContentItemImageTrait](tvcontentitemimagetrait/screenscale2x.md)
  An image meant for a Retina display.
- [static var userInterfaceStyleDark: TVContentItemImageTrait](tvcontentitemimagetrait/userinterfacestyledark.md)
  An image meant for a dark user interface.
- [static var userInterfaceStyleLight: TVContentItemImageTrait](tvcontentitemimagetrait/userinterfacestylelight.md)
  An image meant for a light user interface.
### Initializers
- [init(rawValue: UInt)](tvcontentitemimagetrait/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var imageURL: URL?](tvcontentitem/imageurl.md)
  A URL giving the location of the image to be displayed for this content item.
- [func imageURL(forTraits: TVContentItemImageTrait) -> URL?](tvcontentitem/imageurl(fortraits:).md)
  Retrieve the URL for the image that best matches the specified traits.
- [func setImageURL(URL?, forTraits: TVContentItemImageTrait)](tvcontentitem/setimageurl(_:fortraits:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitemimagetrait)*