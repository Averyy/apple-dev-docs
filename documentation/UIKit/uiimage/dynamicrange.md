# UIImage.DynamicRange

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UIImageDynamicRange : NSInteger;
```

## Topics

### Enumeration Cases
- [UIImage.DynamicRange.constrainedHigh](./dynamicrange/constrainedhigh.md)
  Allow image content to use some extended range. This is appropriate for mixing content with standard and high dynamic ranges.
- [UIImage.DynamicRange.high](./dynamicrange/high.md)
  Allow image content to use unrestricted extended range.
- [UIImage.DynamicRange.standard](./dynamicrange/standard.md)
  Restrict the image content dynamic range to the standard range.
- [UIImage.DynamicRange.unspecified](./dynamicrange/unspecified.md)
  Do not specify a preferred dynamic range.
### Initializers
- [init?(rawValue: Int)](./dynamicrange/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying the dynamic range
- [var isHighDynamicRange: Bool](./ishighdynamicrange.md)
  Indicates that this image is tagged for display of high dynamic range content.
- [func imageRestrictedToStandardDynamicRange() -> UIImage](./imagerestrictedtostandarddynamicrange%28%29.md)
  Returns a new image that will render within the standard range.
- [func heicData() -> Data?](./heicdata%28%29.md)
  Returns HEIC data representing the image, or nil if such a representation could not be generated. HEIC is recommended for efficiently storing all kinds of images, including those with high dynamic range content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/dynamicrange)*