# init(trainingData:textColumn:labelColumn:parameters:)

**Framework**: Create ML  
**Kind**: init

Creates a text classifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(trainingData: DataFrame, textColumn: String, labelColumn: String, parameters: MLTextClassifier.ModelParameters = ModelParameters(validation: .split(strategy: .automatic))) throws
```

## Parameters

- `trainingData`: A data frame specifying the training data.
- `textColumn`: The name of the text column in the provided trainingData.
- `labelColumn`: The name of the label column in the provided trainingData.
- `parameters`: Model training parameters.

## See Also

- [init(trainingData: [String : [String]], parameters: MLTextClassifier.ModelParameters) throws](mltextclassifier/init(trainingdata:parameters:)-9uj3q.md)
  Creates a text classifier.
- [init(trainingData: MLTextClassifier.DataSource, parameters: MLTextClassifier.ModelParameters) throws](mltextclassifier/init(trainingdata:parameters:)-8n8vs.md)
  Creates a text classifier.
- [MLTextClassifier.DataSource](mltextclassifier/datasource.md)
  A data source for a text classifier.
- [MLTextClassifier.ModelParameters](mltextclassifier/modelparameters-swift.struct.md)
  Parameters that specify model training parameters and validation data.
- [let modelParameters: MLTextClassifier.ModelParameters](mltextclassifier/modelparameters-swift.property.md)
  The configuration parameters that the text classifier used for training during initialization.
- [init(trainingData: MLDataTable, textColumn: String, labelColumn: String, parameters: MLTextClassifier.ModelParameters) throws](mltextclassifier/init(trainingdata:textcolumn:labelcolumn:parameters:)-7lp6w.md)
  Creates a text classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/init(trainingdata:textcolumn:labelcolumn:parameters:)-6keqn)*