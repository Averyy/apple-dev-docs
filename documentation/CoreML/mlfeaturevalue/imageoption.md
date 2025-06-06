# MLFeatureValue.ImageOption

**Framework**: Core ML  
**Kind**: struct

The initializer options you use to crop and scale an image when creating an image feature value.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
struct ImageOption
```

## Topics

### Image Options Keys
- [static let cropRect: MLFeatureValue.ImageOption](mlfeaturevalue/imageoption/croprect.md)
  The option you use to crop an image when creating an image feature value.
- [static let cropAndScale: MLFeatureValue.ImageOption](mlfeaturevalue/imageoption/cropandscale.md)
  The option you use to crop and scale an image when creating an image feature value.
### Image Option Key Initializers
- [init(String)](mlfeaturevalue/imageoption/init(_:).md)
  Creates an image feature option key from a string.
- [init(rawValue: String)](mlfeaturevalue/imageoption/init(rawvalue:).md)
  Creates an image feature option key from a raw value string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [convenience init(pixelBuffer: CVPixelBuffer)](mlfeaturevalue/init(pixelbuffer:).md)
  Creates a feature value that contains an image from a pixel buffer.
- [convenience init(CGImage: CGImage, pixelsWide: Int, pixelsHigh: Int, pixelFormatType: OSType, options: [MLFeatureValue.ImageOption : Any]?) throws](mlfeaturevalue/init(cgimage:pixelswide:pixelshigh:pixelformattype:options:).md)
  Creates a feature value that contains an image defined by a core graphics image and its size and pixel format.
- [convenience init(CGImage: CGImage, orientation: CGImagePropertyOrientation, pixelsWide: Int, pixelsHigh: Int, pixelFormatType: OSType, options: [MLFeatureValue.ImageOption : Any]?) throws](mlfeaturevalue/init(cgimage:orientation:pixelswide:pixelshigh:pixelformattype:options:).md)
  Creates a feature value that contains an image defined by a core graphics image and its orientation, size, and pixel format.
- [convenience init(CGImage: CGImage, constraint: MLImageConstraint, options: [MLFeatureValue.ImageOption : Any]?) throws](mlfeaturevalue/init(cgimage:constraint:options:).md)
  Creates a feature value that contains an image defined by a core graphics image and a constraint.
- [convenience init(CGImage: CGImage, orientation: CGImagePropertyOrientation, constraint: MLImageConstraint, options: [MLFeatureValue.ImageOption : Any]?) throws](mlfeaturevalue/init(cgimage:orientation:constraint:options:).md)
  Creates a feature value that contains an image defined by a core graphics image, an orientation, and a constraint.
- [convenience init(imageAtURL: URL, pixelsWide: Int, pixelsHigh: Int, pixelFormatType: OSType, options: [MLFeatureValue.ImageOption : Any]?) throws](mlfeaturevalue/init(imageaturl:pixelswide:pixelshigh:pixelformattype:options:).md)
  Creates a feature value that contains an image defined by an image URL and the image’s size and pixel format.
- [convenience init(imageAtURL: URL, orientation: CGImagePropertyOrientation, pixelsWide: Int, pixelsHigh: Int, pixelFormatType: OSType, options: [MLFeatureValue.ImageOption : Any]?) throws](mlfeaturevalue/init(imageaturl:orientation:pixelswide:pixelshigh:pixelformattype:options:).md)
  Creates a feature value that contains an image defined by an image URL and the image’s orientation, size, and pixel format.
- [convenience init(imageAtURL: URL, constraint: MLImageConstraint, options: [MLFeatureValue.ImageOption : Any]?) throws](mlfeaturevalue/init(imageaturl:constraint:options:).md)
  Creates a feature value that contains an image defined by an image URL and a constraint.
- [convenience init(imageAtURL: URL, orientation: CGImagePropertyOrientation, constraint: MLImageConstraint, options: [MLFeatureValue.ImageOption : Any]?) throws](mlfeaturevalue/init(imageaturl:orientation:constraint:options:).md)
  Creates a feature value that contains an image defined by an image URL, an orientation, and a constraint.
- [class MLImageConstraint](mlimageconstraint.md)
  The width, height, and pixel format constraints of an image feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturevalue/imageoption)*