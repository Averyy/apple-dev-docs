# MLHandActionClassifier.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum

A dataset a hand action classifier task uses to validate the model during a training session.

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
- [MLHandActionClassifier.ModelParameters.ValidationData.dataSource(_:)](mlhandactionclassifier/modelparameters-swift.struct/validationdata/datasource(_:).md)
  Creates a validation dataset from a data source.
- [MLHandActionClassifier.ModelParameters.ValidationData.split(strategy:)](mlhandactionclassifier/modelparameters-swift.struct/validationdata/split(strategy:).md)
  Creates a validation dataset by randomly selecting a portion of the hand action classifier task’s training dataset with a split strategy.
- [MLHandActionClassifier.ModelParameters.ValidationData.none](mlhandactionclassifier/modelparameters-swift.struct/validationdata/none.md)
  Creates an empty validation dataset, which tells the task to skip the model validation phase in a training session.

## See Also

- [MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/videoaugmentationoptions.md)
  Options a hand action classification training session can use to generate additional training data from the videos you provide.
- [MLHandActionClassifier.ModelParameters.ModelAlgorithmType](mlhandactionclassifier/modelparameters-swift.struct/modelalgorithmtype.md)
  The hand action classifier training algorithm options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/modelparameters-swift.struct/validationdata)*