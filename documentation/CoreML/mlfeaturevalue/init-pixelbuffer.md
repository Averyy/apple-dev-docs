# init(pixelBuffer:)

**Framework**: Core ML  
**Kind**: init

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

#### Discussion

[`Core ML`](CoreML.md) supports different pixel format types depending on the model’s feature description. For information about `ImageFeatureType`, see [`Core ML Format Reference`](https://developer.apple.comhttps://apple.github.io/coremltools/mlmodel/Format/FeatureTypes.html#imagefeaturetype). When the image feature’s color space is `GRAYSCALE`, use [`kCVPixelFormatType_OneComponent8`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_OneComponent8); and when it’s `GRAYSCALE_FLOAT16`, use [`kCVPixelFormatType_OneComponent16Half`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_OneComponent16Half); otherwise, use [`kCVPixelFormatType_32BGRA`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_32BGRA) when it’s set to `RGB` or `BGR`.

## Parameters

- `value`: A   (Swift) or   (Objective-C) instance.

## See Also

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
- [MLFeatureValue.ImageOption](mlfeaturevalue/imageoption.md)
  The initializer options you use to crop and scale an image when creating an image feature value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlfeaturevalue/init(pixelbuffer:))*