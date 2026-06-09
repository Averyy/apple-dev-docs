# image

**Framework**: MapKit JS  
**Kind**: property

The image for the annotation.

**Availability**:
- MapKit JS 6.0+

## Declaration

```swift
image?:
    | ImageDelegate
    | ImageHashObject
    | ImageSource
    | Promise<ImageSource>;
```

#### Discussion

Set this property to an [`ImageHashObject`](imagehashobject.md), an [`ImageDelegate`](imagedelegate.md), an [`ImageSource`](imagesource.md), or a `Promise` that resolves to an [`ImageSource`](imagesource.md). For more information, see the [`ImageAnnotation`](imageannotation.md) [`image`](imageannotation/image.md) property.

## See Also

- [url](imageannotationconstructoroptions/url.md)
  An object that contains URLs for the image assets in multiple resolutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/imageannotationconstructoroptions/image)*