# imageURL(forTraits:)

**Framework**: TV Services  
**Kind**: method

Retrieve the URL for the image that best matches the specified traits.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
func imageURL(forTraits traits: TVContentItemImageTrait) -> URL?
```

#### Return Value

The URL for the image asset, or `nil` if an image with the specified traits was not found.

#### Discussion

The image URL can be an absolute path on the local device or an HTTP path. The preferred file format for this image is a layered image file that provides the proper 3d effects. For more information, see [`App Programming Guide for tvOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/AppleTV_PG/index.html#//apple_ref/doc/uid/TP40015241).

## Parameters

- `traits`: The traits for the image you want. For example, you might ask specifically for the variant of the image that supports a dark interface.

## See Also

- [var imageURL: URL?](tvcontentitem/imageurl.md)
  A URL giving the location of the image to be displayed for this content item.
- [func setImageURL(URL?, forTraits: TVContentItemImageTrait)](tvcontentitem/setimageurl(_:fortraits:).md)
- [struct TVContentItemImageTrait](tvcontentitemimagetrait.md)
  Traits describing the type of image you want.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/imageurl(fortraits:))*