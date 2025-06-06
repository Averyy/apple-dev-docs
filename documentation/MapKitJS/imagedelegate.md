# ImageDelegate

**Framework**: MapKit JS  
**Kind**: class

An object you use to specify image URLs.

**Availability**:
- MapKit JS 5.74+

## Declaration

```swift
interface ImageDelegate
```

#### Overview

In addition to using a dictionary object that defines image URLs for [`mapkit.ImageAnnotation`](mapkit.imageannotation.md) or [`mapkit.MarkerAnnotation`](mapkit.markerannotation.md), you can specify an image delegate that allows you to return a URL dynamically or asynchronously.

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
- [getImageUrl](imagedelegate/getimageurl.md)
  Returns the URL to an image of the specified scale.

## Relationships

### Inherits From
- [mapkit.MapFeatureAnnotationGlyphImage](mapkit.mapfeatureannotationglyphimage.md)

## See Also

- [FetchDelegate](fetchdelegate.md)
  An object to pass to a map feature annotation to fetch place objects instead of a callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/imagedelegate)*