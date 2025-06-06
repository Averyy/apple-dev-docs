# size

**Framework**: UIKit  
**Kind**: property

The logical dimensions, in points, for the image.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var size: CGSize { get }
```

#### Discussion

This value reflects the logical size of the image and takes the image’s current orientation into account. Multiply the size values by the value in the [`scale`](uiimage/scale.md) property to get the pixel dimensions of the image.

## See Also

- [var scale: CGFloat](uiimage/scale.md)
  The scale factor of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/size)*