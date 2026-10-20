# MLActionClassifier.VideoAugmentationOptions

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

The video augmentations for an action classifier training session.

**Availability**:
- macOS 11.0+

## Declaration

```swift
struct VideoAugmentationOptions
```

## Topics

### Designating video augmentation options
- [static let horizontalFlip: MLActionClassifier.VideoAugmentationOptions](./videoaugmentationoptions/horizontalflip.md)
  A video augmentation that creates a horizontally flipped copy of a sample video.
### Creating augmentation options
- [init(rawValue: Int)](./videoaugmentationoptions/init%28rawvalue%29.md)
  Creates a video augmentation option set from a raw value.

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
- [MLActionClassifier.DataSource](./datasource.md)
  A data source for an action classifier.
- [MLActionClassifier.ModelParameters](./modelparameters-swift.struct.md)
  Parameters that affect the training process of an action classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/videoaugmentationoptions)*