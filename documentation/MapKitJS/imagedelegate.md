# ImageDelegate

**Framework**: MapKit JS  
**Kind**: struct

An object you use to specify image URLs.

**Availability**:
- MapKit JS 5.74+

## Declaration

```swift
interface ImageDelegate
```

#### Overview

In addition to using a dictionary object that defines image URLs for [`ImageAnnotation`](imageannotation.md) or [`MarkerAnnotation`](markerannotation.md), you can specify an image delegate that allows you to return a URL dynamically or asynchronously.

```javascript
getImageUrl(scale, callback)
```

MapKit JS calls this method with a pixel ratio value that your function uses to construct a URL to an appropriately scaled image, and returns it as the first argument of the callback, as in the following example:

```javascript
const imageDelegate = {
    getImageUrl(scale, callback) {
        callback(`https://example.com/images/marker?scale=${scale}`);
    }
};

const annotation = new mapkit.MarkerAnnotation(
    new mapkit.Coordinate(10, 10),
    {
        glyphImage: imageDelegate
    }
);

```

## Topics

### Returning an image URL
- [getImageUrl(ratio, callback)](imagedelegate/getimageurl.md)
  Returns the URL to an image of the specified scale.

## See Also

- [type ImageHashObject](imagehashobject.md)
  An object that defines a set of images URLs for different scales.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/imagedelegate)*