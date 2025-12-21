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
- [Option set support](option-set-support.md)
  Inspect and modify a video augmentation option set with the properties and methods it inherits from standard protocols.
### Creating image augmentation options
- [init(rawValue: Int)](mlhandposeclassifier/imageaugmentationoptions/init(rawvalue:).md)
  Creates an option set from an integer.

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

- [MLHandPoseClassifier.DataSource](mlhandposeclassifier/datasource.md)
  A hand pose classifier dataset that contains annotated images or hand joint location data.
- [MLHandPoseClassifier.ModelParameters](mlhandposeclassifier/modelparameters-swift.struct.md)
  A set of parameters that affect the training process of a hand pose classifier task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/imageaugmentationoptions)*