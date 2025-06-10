# MLHandPoseClassifier.ModelParameters.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum

The hand pose classifier training algorithm options.

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
- [MLHandPoseClassifier.ModelParameters.ModelAlgorithmType.gcn](mlhandposeclassifier/modelparameters-swift.struct/modelalgorithmtype/gcn.md)
  Selects the graph convolutional neural-network algorithm for a hand pose classifier.
### Comparing an algorithm type
- [static func == (MLHandPoseClassifier.ModelParameters.ModelAlgorithmType, MLHandPoseClassifier.ModelParameters.ModelAlgorithmType) -> Bool](mlhandposeclassifier/modelparameters-swift.struct/modelalgorithmtype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](mlhandposeclassifier/modelparameters-swift.struct/modelalgorithmtype/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Hashing an algorithm type
- [var hashValue: Int](mlhandposeclassifier/modelparameters-swift.struct/modelalgorithmtype/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](mlhandposeclassifier/modelparameters-swift.struct/modelalgorithmtype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mlhandposeclassifier/modelparameters-swift.struct/modelalgorithmtype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions.md)
  Options a hand pose classification training session can use to generate additional training data from the images you provide.
- [MLHandPoseClassifier.ModelParameters.ValidationData](mlhandposeclassifier/modelparameters-swift.struct/validationdata.md)
  A dataset a hand pose classifier task uses to validate the model during a training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.struct/modelalgorithmtype)*