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

- [MLActionClassifier.DataSource](mlactionclassifier/datasource.md)
  A data source for an action classifier.
- [MLActionClassifier.ModelParameters](mlactionclassifier/modelparameters-swift.struct.md)
  Parameters that affect the training process of an action classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/videoaugmentationoptions)*