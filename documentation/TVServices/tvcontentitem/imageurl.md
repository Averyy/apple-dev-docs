# imageURL

**Framework**: TV Services  
**Kind**: property

A URL giving the location of the image to be displayed for this content item.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var imageURL: URL? { get set }
```

#### Discussion

The image URL can be an absolute path on the local device or an HTTP path. The preferred file format for this image is a layered image file that provides the proper 3d effects. For more information, see [`App Programming Guide for tvOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/AppleTV_PG/index.html#//apple_ref/doc/uid/TP40015241).

## See Also

- [func imageURL(forTraits: TVContentItemImageTrait) -> URL?](tvcontentitem/imageurl(fortraits:).md)
  Retrieve the URL for the image that best matches the specified traits.
- [func setImageURL(URL?, forTraits: TVContentItemImageTrait)](tvcontentitem/setimageurl(_:fortraits:).md)
- [struct TVContentItemImageTrait](tvcontentitemimagetrait.md)
  Traits describing the type of image you want.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/imageurl)*