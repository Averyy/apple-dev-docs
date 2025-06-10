# MLHandPoseClassifier.ImageAugmentationOptions

**Framework**: Create ML  
**Kind**: struct

Options a hand pose classification training session can use to generate additional training data from the images you provide.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct ImageAugmentationOptions
```

## Topics

### Augmentations supporting types
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
- [MLHandPoseClassifier.ImageAugmentationOptions.Element](mlhandposeclassifier/imageaugmentationoptions/element.md)
  The element type of the option set.
- [MLHandPoseClassifier.ImageAugmentationOptions.ArrayLiteralElement](mlhandposeclassifier/imageaugmentationoptions/arrayliteralelement.md)
  The type of the elements of an array literal.
- [Option Set Support](imageaugmentationoptions-option-set-support.md)
  ****Inspect and modify an image augmentation option set with the properties and methods it inherits from standard protocols.
### Default Implementations
- [Equatable Implementations](mlhandposeclassifier/imageaugmentationoptions/equatable-implementations.md)
- [OptionSet Implementations](mlhandposeclassifier/imageaugmentationoptions/optionset-implementations.md)
- [RawRepresentable Implementations](mlhandposeclassifier/imageaugmentationoptions/rawrepresentable-implementations.md)
- [SetAlgebra Implementations](mlhandposeclassifier/imageaugmentationoptions/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [MLHandPoseClassifier.ModelParameters.ValidationData](mlhandposeclassifier/modelparameters-swift.struct/validationdata.md)
  A dataset a hand pose classifier task uses to validate the model during a training session.
- [MLHandPoseClassifier.ModelParameters.ModelAlgorithmType](mlhandposeclassifier/modelparameters-swift.struct/modelalgorithmtype.md)
  The hand pose classifier training algorithm options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/imageaugmentationoptions)*