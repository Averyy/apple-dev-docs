# heicData()

**Framework**: UIKit  
**Kind**: method

Returns HEIC data representing the image, or nil if such a representation could not be generated. HEIC is recommended for efficiently storing all kinds of images, including those with high dynamic range content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func heicData() -> Data?
```

## See Also

- [var isHighDynamicRange: Bool](uiimage/ishighdynamicrange.md)
  Indicates that this image is tagged for display of high dynamic range content.
- [func imageRestrictedToStandardDynamicRange() -> UIImage](uiimage/imagerestrictedtostandarddynamicrange.md)
  Returns a new image that will render within the standard range.
- [UIImage.DynamicRange](uiimage/dynamicrange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/heicdata())*