# MLHandPoseClassifier.ImageAugmentationOptions.Element

**Framework**: Create ML  
**Kind**: typealias

The element type of the option set.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
typealias Element = MLHandPoseClassifier.ImageAugmentationOptions
```

#### Discussion

To inherit all the default implementations from the `OptionSet` protocol, the `Element` type must be `Self`, the default.

## See Also

- [static let horizontallyFlip: MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions/horizontallyflip.md)
  Apply left-right flips to the pose in an image.
- [static let rotate: MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions/rotate.md)
  Randomly rotate the pose in an image.
- [static let scale: MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions/scale.md)
  Randomly scale the pose in an image.
- [static let translate: MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions/translate.md)
  Randomly translate the pose in an image.
- [MLHandPoseClassifier.ImageAugmentationOptions.RawValue](mlhandposeclassifier/imageaugmentationoptions/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
- [MLHandPoseClassifier.ImageAugmentationOptions.ArrayLiteralElement](mlhandposeclassifier/imageaugmentationoptions/arrayliteralelement.md)
  The type of the elements of an array literal.
- [Option Set Support](imageaugmentationoptions-option-set-support.md)
  ****Inspect and modify an image augmentation option set with the properties and methods it inherits from standard protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/imageaugmentationoptions/element)*