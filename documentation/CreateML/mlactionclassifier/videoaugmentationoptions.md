# MLActionClassifier.VideoAugmentationOptions

**Framework**: Create ML  
**Kind**: struct

The video augmentations for an action classifier training session.

**Availability**:
- macOS 11.0+

## Declaration

```swift
struct VideoAugmentationOptions
```

## Topics

### Designating video augmentation options
- [static let horizontalFlip: MLActionClassifier.VideoAugmentationOptions](mlactionclassifier/videoaugmentationoptions/horizontalflip.md)
  A video augmentation that creates a horizontally flipped copy of a sample video.
### Creating augmentation options
- [init(rawValue: Int)](mlactionclassifier/videoaugmentationoptions/init(rawvalue:).md)
  Creates a video augmentation option set from a raw value.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [MLActionClassifier.DataSource](mlactionclassifier/datasource.md)
  A data source for an action classifier.
- [MLActionClassifier.ModelParameters](mlactionclassifier/modelparameters-swift.struct.md)
  Parameters that affect the training process of an action classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/videoaugmentationoptions)*