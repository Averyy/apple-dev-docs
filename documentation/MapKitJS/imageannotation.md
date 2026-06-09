# ImageAnnotation

**Framework**: MapKit JS  
**Kind**: class

A customized annotation with image resources that you provide.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class ImageAnnotation extends Annotation
```

## Mentions

- [MapKit JS 6](mapkit-js-6.md)
- [Migrating from Version 5 to Version 6](migrating-from-version-5-to-version-6.md)

#### Overview

There are times when you want to customize the look of an annotation. To do this, use an [`ImageAnnotation`](imageannotation.md) object, which lets you specify your own image resources by providing a URL to your asset (such as a PNG or JPEG image), an [`ImageSource`](imagesource.md) like an `HTMLCanvasElement` or `ImageBitmap`, or a `Promise` that resolves to an [`ImageSource`](imagesource.md).

To make your image look crisp on Retina displays, provide URLs to the Retina versions of your asset, or use an [`ImageDelegate`](imagedelegate.md) to dynamically return the appropriate image. You may want to define the anchor of your asset with [`anchorOffset`](annotation/anchoroffset.md).

The shape of your icon might affect the placement of the callout. You can modify the position of the callout with [`calloutOffset`](annotation/calloutoffset.md).

## Topics

### Creating an image annotation
- [new ImageAnnotation(location, options)](imageannotation/imageannotationconstructor.md)
  Creates an image annotation with an image and a coordinate.
- [interface ImageAnnotationConstructorOptions](imageannotationconstructoroptions.md)
  An object containing options for creating an image annotation.
### Setting the image
- [image](imageannotation/image.md)
  The image for the annotation.
- [url](imageannotation/url.md)
  An object that contains URLs for the image assets in multiple resolutions.

## Relationships

### Inherits From
- [Annotation](annotation.md)

## See Also

- [Clustering annotations](clustering-annotations.md)
  Combine multiple annotations into a single clustered annotation.
- [class Annotation](annotation.md)
  The base annotation object for creating custom annotations.
- [class MarkerAnnotation](markerannotation.md)
  An annotation that displays a balloon-shaped marker at the designated location.
- [class PlaceAnnotation](placeannotation.md)
  An annotation for a place.
- [class MapFeatureAnnotation](mapfeatureannotation.md)
  An object that represents a map feature that the user selects.
- [class UserLocationAnnotation](userlocationannotation.md)
  An annotation that represents someone’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/imageannotation)*