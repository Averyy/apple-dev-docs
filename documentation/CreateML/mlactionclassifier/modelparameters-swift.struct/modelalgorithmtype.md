# MLActionClassifier.ModelParameters.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum

The action classifier training algorithm options.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum ModelAlgorithmType
```

## Topics

### Designating an algorithm
- [MLActionClassifier.ModelParameters.ModelAlgorithmType.stgcn](mlactionclassifier/modelparameters-swift.struct/modelalgorithmtype/stgcn.md)
  The spatial-temporal graph convolution neural-network algorithm.
### Hashing an algorithm type
- [var hashValue: Int](mlactionclassifier/modelparameters-swift.struct/modelalgorithmtype/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](mlactionclassifier/modelparameters-swift.struct/modelalgorithmtype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing algorithm types
- [static func == (MLActionClassifier.ModelParameters.ModelAlgorithmType, MLActionClassifier.ModelParameters.ModelAlgorithmType) -> Bool](mlactionclassifier/modelparameters-swift.struct/modelalgorithmtype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](mlactionclassifier/modelparameters-swift.struct/modelalgorithmtype/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Default Implementations
- [Equatable Implementations](mlactionclassifier/modelparameters-swift.struct/modelalgorithmtype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [MLActionClassifier.ModelParameters.ValidationData](mlactionclassifier/modelparameters-swift.struct/validationdata.md)
  The source of a validation dataset for an action classifier.
- [MLActionClassifier.VideoAugmentationOptions](mlactionclassifier/videoaugmentationoptions.md)
  The video augmentations for an action classifier training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/modelparameters-swift.struct/modelalgorithmtype)*