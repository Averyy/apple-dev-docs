# rotation

**Framework**: Create ML  
**Kind**: property

An option for augmenting training data by rotating each image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
static let rotation: MLImageClassifier.ImageAugmentationOptions
```

#### Discussion

Use this option to tell the image classifier to augment your training data set by rotating the original images.

![Diagram showing how the original image results in four rotated variants.](https://docs-assets.developer.apple.com/published/ed42a26499089f8a3b7e03c08ff63552/MLImageClassifier-ImageAugmentationOptions-rotation-1%402x.png)

The classifier creates four new images with random rotation angles for each original.

## See Also

- [static let crop: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/crop.md)
  An option for augmenting training data by creating cropped versions of each image.
- [static let blur: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/blur.md)
  An option for augmenting training data by blurring each image.
- [static let exposure: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/exposure.md)
  An option for augmenting training data by lightening or darkening each image.
- [static let noise: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/noise.md)
  An option for augmenting training data by adding random amounts of noise to each image.
- [static let flip: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/flip.md)
  An option for augmenting training data by flipping each image along the horizontal and vertical axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/imageaugmentationoptions/rotation)*