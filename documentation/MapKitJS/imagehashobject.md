# ImageHashObject

**Framework**: MapKit JS  
**Kind**: typealias

An object that defines a set of images URLs for different scales.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
type ImageHashObject = Record<string, string | undefined> & {};
```

## Mentions

- [MapKit JS 6](mapkit-js-6.md)
- [Migrating from Version 5 to Version 6](migrating-from-version-5-to-version-6.md)

#### Discussion

The framework automatically loads the appropriate image for the device’s screen scale. Use [`ImageDelegate`](imagedelegate.md) to dynamically provide images for different scales, or use an [`ImageSource`](imagesource.md) to provide a preloaded or dynamically generated image directly.

## See Also

- [interface ImageDelegate](imagedelegate.md)
  An object you use to provide images for annotations.
- [type ImageSource](imagesource.md)
  A union type that represents image sources that the framework can use for annotations and tile overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/imagehashobject)*