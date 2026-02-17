# UIImage.DynamicRange

**Framework**: UIKit  
**Kind**: enum

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum DynamicRange
```

## Topics

### Enumeration Cases
- [UIImage.DynamicRange.constrainedHigh](uiimage/dynamicrange/constrainedhigh.md)
  Allow image content to use some extended range. This is appropriate for mixing content with standard and high dynamic ranges.
- [UIImage.DynamicRange.high](uiimage/dynamicrange/high.md)
  Allow image content to use unrestricted extended range.
- [UIImage.DynamicRange.standard](uiimage/dynamicrange/standard.md)
  Restrict the image content dynamic range to the standard range.
- [UIImage.DynamicRange.unspecified](uiimage/dynamicrange/unspecified.md)
  Do not specify a preferred dynamic range.
### Initializers
- [init?(rawValue: Int)](uiimage/dynamicrange/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isHighDynamicRange: Bool](uiimage/ishighdynamicrange.md)
  Indicates that this image is tagged for display of high dynamic range content.
- [func imageRestrictedToStandardDynamicRange() -> UIImage](uiimage/imagerestrictedtostandarddynamicrange.md)
  Returns a new image that will render within the standard range.
- [func heicData() -> Data?](uiimage/heicdata.md)
  Returns HEIC data representing the image, or nil if such a representation could not be generated. HEIC is recommended for efficiently storing all kinds of images, including those with high dynamic range content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/dynamicrange)*