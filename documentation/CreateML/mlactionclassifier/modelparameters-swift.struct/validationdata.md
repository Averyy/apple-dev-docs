# MLActionClassifier.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum

The source of a validation dataset for an action classifier.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum ValidationData
```

## Topics

### Designating validation data
- [MLActionClassifier.ModelParameters.ValidationData.dataSource(_:)](mlactionclassifier/modelparameters-swift.struct/validationdata/datasource(_:).md)
  A validation dataset represented by a data source.
- [MLActionClassifier.ModelParameters.ValidationData.split(strategy:)](mlactionclassifier/modelparameters-swift.struct/validationdata/split(strategy:).md)
  A validation dataset derived by randomly selecting a portion of the action classifier’s training dataset using the split strategy.
- [MLActionClassifier.ModelParameters.ValidationData.none](mlactionclassifier/modelparameters-swift.struct/validationdata/none.md)
  An empty validation dataset that skips the model validation phase after training.

## See Also

- [MLActionClassifier.VideoAugmentationOptions](mlactionclassifier/videoaugmentationoptions.md)
  The video augmentations for an action classifier training session.
- [MLActionClassifier.ModelParameters.ModelAlgorithmType](mlactionclassifier/modelparameters-swift.struct/modelalgorithmtype.md)
  The action classifier training algorithm options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/modelparameters-swift.struct/validationdata)*