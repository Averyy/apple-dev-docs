# image

**Framework**: MapKit JS  
**Kind**: property

The image for the annotation.

**Availability**:
- MapKit JS 6.0+

## Declaration

```swift
get image():
    | ImageDelegate
    | ImageHashObject
    | ImageSource
    | Promise<ImageSource>;
set image(
    value:
        | ImageDelegate
        | ImageHashObject
        | ImageSource
        | Promise<ImageSource>,
);
```

#### Discussion

Set this property to one of the following:

- An [`ImageHashObject`](imagehashobject.md) that contains URLs for images at multiple resolutions.
- An [`ImageDelegate`](imagedelegate.md) that dynamically provides the image.
- An [`ImageSource`](imagesource.md) such as an `HTMLImageElement`, `HTMLCanvasElement`, `ImageBitmap`, or `OffscreenCanvas`.
- A `Promise` that resolves to an [`ImageSource`](imagesource.md).

Using an [`ImageSource`](imagesource.md) or a `Promise` gives you control over image loading. For example, you can use the Fetch API with custom headers, apply transformations to an image before display, or implement custom error recovery logic. See [`ImageSource`](imagesource.md) for cross-origin requirements.

## See Also

- [url](imageannotation/url.md)
  An object that contains URLs for the image assets in multiple resolutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/imageannotation/image)*