# MLImageConstraint

**Framework**: Core ML  
**Kind**: class

The width, height, and pixel format constraints of an image feature.

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
class MLImageConstraint
```

#### Overview

In CoreML, an  is a collection of pixels represented by [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/cvpixelbuffer-q2e) (Swift) or [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/CVPixelBuffer) (Objective-C). An  is a model input or output that accepts or produces, respectively, an image bundled in an [`MLFeatureValue`](mlfeaturevalue.md). `MLImageConstraint` defines the image feature’s limitations for the images within an `MLFeatureValue`.

If a model has an image feature for an input or output, the model author uses an  by creating an [`MLFeatureDescription`](mlfeaturedescription.md). The feature description for an image input or output has:

- Its [`type`](mlfeaturedescription/type.md) property set to [`MLFeatureType.image`](mlfeaturetype/image.md)
- Its [`imageConstraint`](mlfeaturedescription/imageconstraint.md) property set to an [`MLImageConstraint`](mlimageconstraint.md) instance configured to the image feature’s size and format

Image features that support additional image sizes provide a range of sizes, or a list of discrete sizes, in their image constraint’s [`sizeConstraint`](mlimageconstraint/sizeconstraint.md) property.

## Topics

### Accessing the constraints
- [var pixelsWide: Int](mlimageconstraint/pixelswide.md)
  The model’s default width for an image feature.
- [var pixelsHigh: Int](mlimageconstraint/pixelshigh.md)
  The model’s default height for an image feature.
- [var pixelFormatType: OSType](mlimageconstraint/pixelformattype.md)
  The model’s pixel format for an image feature.
### Inspecting acceptable sizes
- [var sizeConstraint: MLImageSizeConstraint](mlimageconstraint/sizeconstraint.md)
  Additional sizes this image feature supports.
- [class MLImageSizeConstraint](mlimagesizeconstraint.md)
  A list or range of sizes that augment an image constraint’s default size.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

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
- [MLFeatureValue.ImageOption](mlfeaturevalue/imageoption.md)
  The initializer options you use to crop and scale an image when creating an image feature value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlimageconstraint)*