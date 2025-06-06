# MLHandActionClassifier.ModelParameters.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum

The hand action classifier training algorithm options.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
enum ModelAlgorithmType
```

## Topics

### Choosing an algorithm type
- [MLHandActionClassifier.ModelParameters.ModelAlgorithmType.gcn](mlhandactionclassifier/modelparameters-swift.struct/modelalgorithmtype/gcn.md)
  Selects the graph convolutional neural-network algorithm for a hand action classifier.
### Comparing an algorithm type
- [static func == (MLHandActionClassifier.ModelParameters.ModelAlgorithmType, MLHandActionClassifier.ModelParameters.ModelAlgorithmType) -> Bool](mlhandactionclassifier/modelparameters-swift.struct/modelalgorithmtype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](mlhandactionclassifier/modelparameters-swift.struct/modelalgorithmtype/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Hashing an algorithm type
- [var hashValue: Int](mlhandactionclassifier/modelparameters-swift.struct/modelalgorithmtype/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](mlhandactionclassifier/modelparameters-swift.struct/modelalgorithmtype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mlhandactionclassifier/modelparameters-swift.struct/modelalgorithmtype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/videoaugmentationoptions.md)
  Options a hand action classification training session can use to generate additional training data from the videos you provide.
- [MLHandActionClassifier.ModelParameters.ValidationData](mlhandactionclassifier/modelparameters-swift.struct/validationdata.md)
  A dataset a hand action classifier task uses to validate the model during a training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/modelparameters-swift.struct/modelalgorithmtype)*