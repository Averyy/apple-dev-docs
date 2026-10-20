# setImageURL(_:forTraits:)

**Framework**: TV Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- tvOS 11.0+ - Deprecated in 13.0

## Declaration

```swift
func setImageURL(_ aURL: URL?, forTraits traits: TVContentItemImageTrait)
```

```objc
- (void) setImageURL:(NSURL *) aURL forTraits:(TVContentItemImageTrait) traits;
```

#### Discussion

The preferred file format for this image is a layered image file that provides the proper 3d effects. For more information, see [App Programming Guide for tvOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/AppleTV_PG/index.html#//apple_ref/doc/uid/TP40015241).

## Parameters

- `aURL`: The URL corresponding to the image location. This parameter can be an absolute path on the local device or an HTTP path. Specify `nil` to remove the image associated with the given traits.
- `traits`: The traits to associate with the image. For example, you might specify that the image applies only to dark interfaces.

## See Also

### Accessing Image Resources
- [var imageURL: URL?](./imageurl.md)
  A URL giving the location of the image to be displayed for this content item.
- [func imageURL(forTraits: TVContentItemImageTrait) -> URL?](./imageurl%28fortraits%29.md)
  Retrieve the URL for the image that best matches the specified traits.
- [struct TVContentItemImageTrait](../tvcontentitemimagetrait.md)
  Traits describing the type of image you want.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvcontentitem/setimageurl(_:fortraits:))*