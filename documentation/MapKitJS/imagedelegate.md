# ImageDelegate

**Framework**: MapKit JS  
**Kind**: struct

An object you use to provide images for annotations.

**Availability**:
- MapKit JS 5.74+

## Declaration

```swift
interface ImageDelegate
```

## Mentions

- [MapKit JS 6](mapkit-js-6.md)
- [Migrating from Version 5 to Version 6](migrating-from-version-5-to-version-6.md)

#### Overview

In addition to using a dictionary object that defines image URLs for [`ImageAnnotation`](imageannotation.md) or [`MarkerAnnotation`](markerannotation.md), you can specify an image delegate that allows you to return an image dynamically or asynchronously.

Implement [`getImage()`](imagedelegate/getimage.md) to return a `Promise` that resolves to a URL string, an [`ImageSource`](imagesource.md), or `undefined`:

```javascript
const imageDelegate = {
    async getImage(scale) {
        const response = await fetch(`https://example.com/images/marker?scale=${scale}`, {
            headers: { "Authorization": "Bearer " + token }
        });
        if (!response.ok) return undefined;
        const blob = await response.blob();
        return createImageBitmap(blob);
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

### Returning an image
- [getImage(ratio)](imagedelegate/getimage.md)
  Returns an image for the specified scale.
- [getImageUrl(ratio, callback)](imagedelegate/getimageurl.md)
  Returns the URL to an image of the specified scale.

## Relationships

### Conforming Types
- [MapFeatureAnnotationGlyphImage](mapfeatureannotationglyphimage.md)

## See Also

- [type ImageHashObject](imagehashobject.md)
  An object that defines a set of images URLs for different scales.
- [type ImageSource](imagesource.md)
  A union type that represents image sources that the framework can use for annotations and tile overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/imagedelegate)*