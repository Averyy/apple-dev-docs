# init(imageAtURL:orientation:pixelsWide:pixelsHigh:pixelFormatType:options:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a feature value that contains an image defined by an image URL and the image’s orientation, size, and pixel format.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init(imageAtURL url: URL, orientation: CGImagePropertyOrientation, pixelsWide: Int, pixelsHigh: Int, pixelFormatType: OSType, options: [MLFeatureValue.ImageOption : Any]? = nil) throws
```

## Parameters

- `url`: A [`URL`](../../Foundation/url.md) (Swift) or [`NSURL`](../../Foundation/nsurl.md) (Objective-C) to an image.
- `orientation`: A [`CGImagePropertyOrientation`](../../ImageIO/cgimagepropertyorientation.md) instance.
- `pixelsWide`: The image’s width in pixels.
- `pixelsHigh`: The image’s height in pixels.
- `pixelFormatType`: The image’s pixel format (see [Pixel Format Identifiers](../../CoreVideo/pixel-format-identifiers.md)).
- `options`: A dictionary of [`VNImageCropAndScaleOption`](../../Vision/vnimagecropandscaleoption.md) values, each keyed by [`MLFeatureValue.ImageOption`](./imageoption.md).

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
- [convenience init(imageAtURL: URL, constraint: MLImageConstraint, options: [MLFeatureValue.ImageOption : Any]?) throws](./init%28imageaturl,constraint,options%29.md)
  Creates a feature value that contains an image defined by an image URL and a constraint.
- [convenience init(imageAtURL: URL, orientation: CGImagePropertyOrientation, constraint: MLImageConstraint, options: [MLFeatureValue.ImageOption : Any]?) throws](./init%28imageaturl,orientation,constraint,options%29.md)
  Creates a feature value that contains an image defined by an image URL, an orientation, and a constraint.
- [class MLImageConstraint](../mlimageconstraint.md)
  The width, height, and pixel format constraints of an image feature.
- [MLFeatureValue.ImageOption](./imageoption.md)
  The initializer options you use to crop and scale an image when creating an image feature value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturevalue/init(imageaturl:orientation:pixelswide:pixelshigh:pixelformattype:options:))*