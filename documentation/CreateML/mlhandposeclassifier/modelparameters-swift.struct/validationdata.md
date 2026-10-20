# MLHandPoseClassifier.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

A dataset a hand pose classifier task uses to validate the model during a training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
enum ValidationData
```

## Topics

### Designating validation data
- [MLHandPoseClassifier.ModelParameters.ValidationData.dataSource(_:)](./validationdata/datasource%28_%29.md)
  Creates a validation dataset from a data source.
- [MLHandPoseClassifier.ModelParameters.ValidationData.split(strategy:)](./validationdata/split%28strategy%29.md)
  Creates a validation dataset by randomly selecting a portion of the hand pose classifier task’s training dataset with a split strategy.
- [MLHandPoseClassifier.ModelParameters.ValidationData.none](./validationdata/none.md)
  Creates an empty validation dataset, which tells the task to skip the model validation phase in a training session.

## See Also

### Parameter supporting types
- [MLHandPoseClassifier.ImageAugmentationOptions](../imageaugmentationoptions.md)
  Options a hand pose classification training session can use to generate additional training data from the images you provide.
- [MLHandPoseClassifier.ModelParameters.ModelAlgorithmType](./modelalgorithmtype.md)
  The hand pose classifier training algorithm options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.struct/validationdata)*