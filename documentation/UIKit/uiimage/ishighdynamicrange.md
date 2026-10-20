# isHighDynamicRange

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Indicates that this image is tagged for display of high dynamic range content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var isHighDynamicRange: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL isHighDynamicRange;
```

## See Also

### Specifying the dynamic range
- [func imageRestrictedToStandardDynamicRange() -> UIImage](./imagerestrictedtostandarddynamicrange%28%29.md)
  Returns a new image that will render within the standard range.
- [func heicData() -> Data?](./heicdata%28%29.md)
  Returns HEIC data representing the image, or nil if such a representation could not be generated. HEIC is recommended for efficiently storing all kinds of images, including those with high dynamic range content.
- [UIImage.DynamicRange](./dynamicrange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/ishighdynamicrange)*