# blur

**Framework**: Create ML  
**Kind**: property  
**Role**: Type Property

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

![Diagram showing how the original image results in four blurred variants.](https://developer.apple.com/tutorials/images/com.apple.createml/MLImageClassifier-ImageAugmentationOptions-blur-1@2x.png)

The classifier creates four new images with random amounts of blur for each original.

## See Also

### Selecting augmentation options
- [static let crop: MLImageClassifier.ImageAugmentationOptions](./crop.md)
  An option for augmenting training data by creating cropped versions of each image.
- [static let rotation: MLImageClassifier.ImageAugmentationOptions](./rotation.md)
  An option for augmenting training data by rotating each image.
- [static let exposure: MLImageClassifier.ImageAugmentationOptions](./exposure.md)
  An option for augmenting training data by lightening or darkening each image.
- [static let noise: MLImageClassifier.ImageAugmentationOptions](./noise.md)
  An option for augmenting training data by adding random amounts of noise to each image.
- [static let flip: MLImageClassifier.ImageAugmentationOptions](./flip.md)
  An option for augmenting training data by flipping each image along the horizontal and vertical axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/imageaugmentationoptions/blur)*