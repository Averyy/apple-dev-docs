# MLFeatureValue.ImageOption

**Framework**: Core ML  
**Kind**: struct  
**Role**: Structure

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

```c
typedef NSString * MLFeatureValueImageOption;
```

## Topics

### Image options keys
- [static let cropRect: MLFeatureValue.ImageOption](./imageoption/croprect.md)
  The option you use to crop an image when creating an image feature value.
- [static let cropAndScale: MLFeatureValue.ImageOption](./imageoption/cropandscale.md)
  The option you use to crop and scale an image when creating an image feature value.
### Image option key initializers
- [init(String)](./imageoption/init%28_%29.md)
  Creates an image feature option key from a string.
- [init(rawValue: String)](./imageoption/init%28rawvalue%29.md)
  Creates an image feature option key from a raw value string.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating image feature values
- [convenience init(pixelBuffer: CVPixelBuffer)](./init%28pixelbuffer%29.md)
  Creates a feature value that contains an image from a pixel buffer.
- [convenience init(CGImage: CGImage, pixelsWide: Int, pixelsHigh: Int, pixelFormatType: OSType, options: [MLFeatureValue.ImageOption : Any]?) throws](./init%28cgimage,pixelswide,pixelshigh,pixelformattype,options%29-2zg43.md)
  Creates a feature value that contains an image defined by a core graphics image and its size and pixel format.
- [convenience init(CGImage: CGImage, orientation: CGImagePropertyOrientation, pixelsWide: Int, pixelsHigh: Int, pixelFormatType: OSType, options: [MLFeatureValue.ImageOption : Any]?) throws](./init%28cgimage,orientation,pixelswide,pixelshigh,pixelformattype,options%29-4nme0.md)
  Creates a feature value that contains an image defined by a core graphics image and its orientation, size, and pixel format.
- [convenience init(CGImage: CGImage, constraint: MLImageConstraint, options: [MLFeatureValue.ImageOption : Any]?) throws](./init%28cgimage,constraint,options%29-1j00l.md)
  Creates a feature value that contains an image defined by a core graphics image and a constraint.
- [convenience init(CGImage: CGImage, orientation: CGImagePropertyOrientation, constraint: MLImageConstraint, options: [MLFeatureValue.ImageOption : Any]?) throws](./init%28cgimage,orientation,constraint,options%29-87vk0.md)
  Creates a feature value that contains an image defined by a core graphics image, an orientation, and a constraint.
- [convenience init(imageAtURL: URL, pixelsWide: Int, pixelsHigh: Int, pixelFormatType: OSType, options: [MLFeatureValue.ImageOption : Any]?) throws](./init%28imageaturl,pixelswide,pixelshigh,pixelformattype,options%29.md)
  Creates a feature value that contains an image defined by an image URL and the image’s size and pixel format.
- [convenience init(imageAtURL: URL, orientation: CGImagePropertyOrientation, pixelsWide: Int, pixelsHigh: Int, pixelFormatType: OSType, options: [MLFeatureValue.ImageOption : Any]?) throws](./init%28imageaturl,orientation,pixelswide,pixelshigh,pixelformattype,options%29.md)
  Creates a feature value that contains an image defined by an image URL and the image’s orientation, size, and pixel format.
- [convenience init(imageAtURL: URL, constraint: MLImageConstraint, options: [MLFeatureValue.ImageOption : Any]?) throws](./init%28imageaturl,constraint,options%29.md)
  Creates a feature value that contains an image defined by an image URL and a constraint.
- [convenience init(imageAtURL: URL, orientation: CGImagePropertyOrientation, constraint: MLImageConstraint, options: [MLFeatureValue.ImageOption : Any]?) throws](./init%28imageaturl,orientation,constraint,options%29.md)
  Creates a feature value that contains an image defined by an image URL, an orientation, and a constraint.
- [class MLImageConstraint](../mlimageconstraint.md)
  The width, height, and pixel format constraints of an image feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturevalue/imageoption)*