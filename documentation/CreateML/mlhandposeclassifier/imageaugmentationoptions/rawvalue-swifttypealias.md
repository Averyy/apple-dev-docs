# MLHandPoseClassifier.ImageAugmentationOptions.RawValue

**Framework**: Create ML  
**Kind**: typealias

The raw type that can be used to represent all values of the conforming type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
typealias RawValue = Int
```

#### Discussion

Every distinct value of the conforming type has a corresponding unique value of the `RawValue` type, but there may be values of the `RawValue` type that don’t have a corresponding value of the conforming type.

## See Also

- [static let horizontallyFlip: MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions/horizontallyflip.md)
  Apply left-right flips to the pose in an image.
- [static let rotate: MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions/rotate.md)
  Randomly rotate the pose in an image.
- [static let scale: MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions/scale.md)
  Randomly scale the pose in an image.
- [static let translate: MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions/translate.md)
  Randomly translate the pose in an image.
- [MLHandPoseClassifier.ImageAugmentationOptions.Element](mlhandposeclassifier/imageaugmentationoptions/element.md)
  The element type of the option set.
- [MLHandPoseClassifier.ImageAugmentationOptions.ArrayLiteralElement](mlhandposeclassifier/imageaugmentationoptions/arrayliteralelement.md)
  The type of the elements of an array literal.
- [Option Set Support](imageaugmentationoptions-option-set-support.md)
  ****Inspect and modify an image augmentation option set with the properties and methods it inherits from standard protocols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/imageaugmentationoptions/rawvalue-swift.typealias)*