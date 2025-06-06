# MLImageClassifier.ModelParameters.ValidationData.split(strategy:)

**Framework**: Create ML  
**Kind**: case

A validation dataset derived by randomly selecting a portion of the image classifier’s training dataset using the split strategy.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case split(strategy: MLSplitStrategy)
```

## See Also

- [MLImageClassifier.ModelParameters.ValidationData.dataSource(_:)](mlimageclassifier/modelparameters-swift.struct/validationdata-swift.enum/datasource(_:).md)
  A validation dataset represented by a data source.
- [MLImageClassifier.ModelParameters.ValidationData.dictionary(_:)](mlimageclassifier/modelparameters-swift.struct/validationdata-swift.enum/dictionary(_:).md)
  A validation dataset represented by a dictionary.
- [MLImageClassifier.ModelParameters.ValidationData.none](mlimageclassifier/modelparameters-swift.struct/validationdata-swift.enum/none.md)
  An empty validation dataset that skips the model validation phase after training.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/validationdata-swift.enum/split(strategy:))*