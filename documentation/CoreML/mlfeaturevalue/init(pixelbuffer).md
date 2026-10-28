# init(pixelBuffer:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a feature value that contains an image from a pixel buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
convenience init(pixelBuffer value: CVPixelBuffer)
```

```objc
+ (instancetype) featureValueWithPixelBuffer:(CVPixelBufferRef) value;
```

## Discussion

[Core ML](../CoreML.md) supports different pixel format types depending on the model’s feature description. For information about `ImageFeatureType`, see [Core ML Format Reference](https://apple.github.io/coremltools/mlmodel/Format/FeatureTypes.html#imagefeaturetype). When the image feature’s color space is `GRAYSCALE`, use [`kCVPixelFormatType_OneComponent8`](../../CoreVideo/kcvpixelformattype_onecomponent8.md); and when it’s `GRAYSCALE_FLOAT16`, use [`kCVPixelFormatType_OneComponent16Half`](../../CoreVideo/kcvpixelformattype_onecomponent16half.md); otherwise, use [`kCVPixelFormatType_32BGRA`](../../CoreVideo/kcvpixelformattype_32bgra.md) when it’s set to `RGB` or `BGR`.

## Parameters

- `value`: A [CVPixelBuffer](../../CoreVideo/cvpixelbuffer-q2e.md) (Swift) or [`CVPixelBuffer`](../../CoreVideo/cvpixelbuffer.md) (Objective-C) instance.

## See Also

### Creating image feature values
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
- [MLFeatureValue.ImageOption](./imageoption.md)
  The initializer options you use to crop and scale an image when creating an image feature value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturevalue/init(pixelbuffer:))*