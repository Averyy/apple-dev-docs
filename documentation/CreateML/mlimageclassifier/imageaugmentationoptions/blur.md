# blur

**Framework**: Create ML  
**Kind**: property

An option for augmenting training data by blurring each image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
static let blur: MLImageClassifier.ImageAugmentationOptions
```

#### Discussion

Use this option to tell the image classifier to augment your training data set by creating blurred versions of the original images.

![Diagram showing how the original image results in four blurred variants.](https://docs-assets.developer.apple.com/published/8e69adbdfeeaa69d4b2ff7479e4e3330/MLImageClassifier-ImageAugmentationOptions-blur-1%402x.png)

The classifier creates four new images with random amounts of blur for each original.

## See Also

- [static let crop: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/crop.md)
  An option for augmenting training data by creating cropped versions of each image.
- [static let rotation: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/rotation.md)
  An option for augmenting training data by rotating each image.
- [static let exposure: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/exposure.md)
  An option for augmenting training data by lightening or darkening each image.
- [static let noise: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/noise.md)
  An option for augmenting training data by adding random amounts of noise to each image.
- [static let flip: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/flip.md)
  An option for augmenting training data by flipping each image along the horizontal and vertical axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/imageaugmentationoptions/blur)*