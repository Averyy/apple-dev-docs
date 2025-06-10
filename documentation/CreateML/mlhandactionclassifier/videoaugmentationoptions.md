# MLHandActionClassifier.VideoAugmentationOptions

**Framework**: Create ML  
**Kind**: struct

Options a hand action classification training session can use to generate additional training data from the videos you provide.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct VideoAugmentationOptions
```

## Topics

### Augmentations supporting types
- [static let dropFrames: MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/videoaugmentationoptions/dropframes.md)
  Randomly drop frames from a video.
- [static let horizontallyFlip: MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/videoaugmentationoptions/horizontallyflip.md)
  Apply left-right flips to the pose in a video.
- [static let interpolateFrames: MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/videoaugmentationoptions/interpolateframes.md)
  Random time interpolation through a video.
- [static let rotate: MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/videoaugmentationoptions/rotate.md)
  Randomly rotate the pose in a video.
- [static let scale: MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/videoaugmentationoptions/scale.md)
  Randomly scale the pose in a video.
- [static let translate: MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/videoaugmentationoptions/translate.md)
  Randomly translate the pose in a video.
- [MLHandActionClassifier.VideoAugmentationOptions.RawValue](mlhandactionclassifier/videoaugmentationoptions/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
- [MLHandActionClassifier.VideoAugmentationOptions.Element](mlhandactionclassifier/videoaugmentationoptions/element.md)
  The element type of the option set.
- [MLHandActionClassifier.VideoAugmentationOptions.ArrayLiteralElement](mlhandactionclassifier/videoaugmentationoptions/arrayliteralelement.md)
  The type of the elements of an array literal.
- [Option Set Support](videoaugmentationoptions-option-set-support.md)
  Inspect and modify a video augmentation option set with the properties and methods it inherits from standard protocols.
### Default Implementations
- [Equatable Implementations](mlhandactionclassifier/videoaugmentationoptions/equatable-implementations.md)
- [OptionSet Implementations](mlhandactionclassifier/videoaugmentationoptions/optionset-implementations.md)
- [RawRepresentable Implementations](mlhandactionclassifier/videoaugmentationoptions/rawrepresentable-implementations.md)
- [SetAlgebra Implementations](mlhandactionclassifier/videoaugmentationoptions/setalgebra-implementations.md)

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

- [MLHandActionClassifier.ModelParameters.ValidationData](mlhandactionclassifier/modelparameters-swift.struct/validationdata.md)
  A dataset a hand action classifier task uses to validate the model during a training session.
- [MLHandActionClassifier.ModelParameters.ModelAlgorithmType](mlhandactionclassifier/modelparameters-swift.struct/modelalgorithmtype.md)
  The hand action classifier training algorithm options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/videoaugmentationoptions)*