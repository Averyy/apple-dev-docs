# flip

**Framework**: Create ML  
**Kind**: property

An option for augmenting training data by flipping each image along the horizontal and vertical axes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
static let flip: MLImageClassifier.ImageAugmentationOptions
```

#### Discussion

Use this option to tell the image classifier to augment your training data set by flipping the original images.

![Diagram showing how the original image results in three flipped variants.](https://docs-assets.developer.apple.com/published/062c2d1598840c3a4a94abe8bf4015bb/MLImageClassifier-ImageAugmentationOptions-flip-1%402x.png)

The classifier creates three new images by flipping the original horizontally, vertically, and both horizontally and vertically.

## See Also

- [static let crop: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/crop.md)
  An option for augmenting training data by creating cropped versions of each image.
- [static let rotation: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/rotation.md)
  An option for augmenting training data by rotating each image.
- [static let blur: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/blur.md)
  An option for augmenting training data by blurring each image.
- [static let exposure: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/exposure.md)
  An option for augmenting training data by lightening or darkening each image.
- [static let noise: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/noise.md)
  An option for augmenting training data by adding random amounts of noise to each image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/imageaugmentationoptions/flip)*