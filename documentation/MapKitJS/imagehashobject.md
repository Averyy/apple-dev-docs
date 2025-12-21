# ImageHashObject

**Framework**: MapKit JS  
**Kind**: typealias

An object that defines a set of images URLs for different scales.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
type ImageHashObject = {
    [ratio: string]: string | undefined;
} & {};
```

#### Discussion

The framework automatically loads the appropriate image for the device’s screen scale. Use [`ImageDelegate`](imagedelegate.md) to provide custom URLs for different scales.

## See Also

- [interface ImageDelegate](imagedelegate.md)
  An object you use to specify image URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/imagehashobject)*