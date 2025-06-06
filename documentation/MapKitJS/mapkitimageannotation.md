# mapkit.ImageAnnotation

**Framework**: MapKit JS  
**Kind**: class

A customized annotation with image resources that you provide.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface mapkit.ImageAnnotation
```

#### Overview

There are times when you want to customize the look of an annotation. The easiest way to do that is to use a [`mapkit.ImageAnnotation`](mapkit.imageannotation/mapkit.imageannotation.md) object, which lets you specify your own image resources. Minimally, all you need to provide is a URL to your asset (such as a PNG or JPEG image).

To make your image look crisp on Retina displays, provide URLs to the Retina versions of your asset. You may want to define the anchor of your asset with [`anchorOffset`](mapkit.annotation/anchoroffset.md).

The shape of your icon might affect the placement of the callout. You can modify the position of the callout with [`calloutOffset`](mapkit.annotation/calloutoffset.md).

## Topics

### Creating an image annotation
- [mapkit.ImageAnnotation](mapkit.imageannotation/mapkit.imageannotation.md)
  Creates an image annotation with a URL to its image and a coordinate.
- [ImageAnnotationConstructorOptions](imageannotationconstructoroptions.md)
  An object containing options for creating an image annotation.
### Retrieving the image URL
- [url](mapkit.imageannotation/url.md)
  An object containing URLs for the image assets in multiple resolutions.

## Relationships

### Inherited By
- [mapkit.Annotation](mapkit.annotation/mapkit.annotation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.imageannotation)*