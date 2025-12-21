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
- [Option set support](option-set-support.md)
  Inspect and modify a video augmentation option set with the properties and methods it inherits from standard protocols.
### Initializers
- [init(rawValue: Int)](mlhandactionclassifier/videoaugmentationoptions/init(rawvalue:).md)
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

- [MLHandActionClassifier.DataSource](mlhandactionclassifier/datasource.md)
  A hand action classifier dataset that contains annotated videos or hand joint location data.
- [MLHandActionClassifier.ModelParameters](mlhandactionclassifier/modelparameters-swift.struct.md)
  A set of parameters that affect the training process of a hand action classifier task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/videoaugmentationoptions)*