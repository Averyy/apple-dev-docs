# MLHandPoseClassifier.ModelParameters.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

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
- [MLHandPoseClassifier.ModelParameters.ModelAlgorithmType.gcn](./modelalgorithmtype/gcn.md)
  Selects the graph convolutional neural-network algorithm for a hand pose classifier.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Parameter supporting types
- [MLHandPoseClassifier.ImageAugmentationOptions](../imageaugmentationoptions.md)
  Options a hand pose classification training session can use to generate additional training data from the images you provide.
- [MLHandPoseClassifier.ModelParameters.ValidationData](./validationdata.md)
  A dataset a hand pose classifier task uses to validate the model during a training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.struct/modelalgorithmtype)*