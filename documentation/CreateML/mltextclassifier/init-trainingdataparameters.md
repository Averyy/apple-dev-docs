# init(trainingData:parameters:)

**Framework**: Create ML  
**Kind**: init

Creates a text classifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init(trainingData: MLTextClassifier.DataSource, parameters: MLTextClassifier.ModelParameters = ModelParameters(validation: .split(strategy: .automatic))) throws
```

## Parameters

- `trainingData`: A data source specifying the training data.
- `parameters`: Model training parameters.

## See Also

- [init(trainingData:textColumn:labelColumn:parameters:)](mltextclassifier/init(trainingdata:textcolumn:labelcolumn:parameters:).md)
  Creates a text classifier.
- [MLTextClassifier.DataSource](mltextclassifier/datasource.md)
  A data source for a text classifier.
- [MLTextClassifier.ModelParameters](mltextclassifier/modelparameters-swift.struct.md)
  Parameters that specify model training parameters and validation data.
- [let modelParameters: MLTextClassifier.ModelParameters](mltextclassifier/modelparameters-swift.property.md)
  The configuration parameters that the text classifier used for training during initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/init(trainingdata:parameters:))*