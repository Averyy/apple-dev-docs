# MLHandPoseClassifier.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum

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
- [MLHandPoseClassifier.ModelParameters.ValidationData.dataSource(_:)](mlhandposeclassifier/modelparameters-swift.struct/validationdata/datasource(_:).md)
  Creates a validation dataset from a data source.
- [MLHandPoseClassifier.ModelParameters.ValidationData.split(strategy:)](mlhandposeclassifier/modelparameters-swift.struct/validationdata/split(strategy:).md)
  Creates a validation dataset by randomly selecting a portion of the hand pose classifier task’s training dataset with a split strategy.
- [MLHandPoseClassifier.ModelParameters.ValidationData.none](mlhandposeclassifier/modelparameters-swift.struct/validationdata/none.md)
  Creates an empty validation dataset, which tells the task to skip the model validation phase in a training session.

## See Also

- [MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions.md)
  Options a hand pose classification training session can use to generate additional training data from the images you provide.
- [MLHandPoseClassifier.ModelParameters.ModelAlgorithmType](mlhandposeclassifier/modelparameters-swift.struct/modelalgorithmtype.md)
  The hand pose classifier training algorithm options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.struct/validationdata)*