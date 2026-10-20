# MLHandActionClassifier.VideoAugmentationOptions

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

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
- [static let dropFrames: MLHandActionClassifier.VideoAugmentationOptions](./videoaugmentationoptions/dropframes.md)
  Randomly drop frames from a video.
- [static let horizontallyFlip: MLHandActionClassifier.VideoAugmentationOptions](./videoaugmentationoptions/horizontallyflip.md)
  Apply left-right flips to the pose in a video.
- [static let interpolateFrames: MLHandActionClassifier.VideoAugmentationOptions](./videoaugmentationoptions/interpolateframes.md)
  Random time interpolation through a video.
- [static let rotate: MLHandActionClassifier.VideoAugmentationOptions](./videoaugmentationoptions/rotate.md)
  Randomly rotate the pose in a video.
- [static let scale: MLHandActionClassifier.VideoAugmentationOptions](./videoaugmentationoptions/scale.md)
  Randomly scale the pose in a video.
- [static let translate: MLHandActionClassifier.VideoAugmentationOptions](./videoaugmentationoptions/translate.md)
  Randomly translate the pose in a video.
- [Option set support](../option-set-support.md)
  Inspect and modify a video augmentation option set with the properties and methods it inherits from standard protocols.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Supporting types
- [MLHandActionClassifier.DataSource](./datasource.md)
  A hand action classifier dataset that contains annotated videos or hand joint location data.
- [MLHandActionClassifier.ModelParameters](./modelparameters-swift.struct.md)
  A set of parameters that affect the training process of a hand action classifier task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/videoaugmentationoptions)*