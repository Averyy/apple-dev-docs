# init(trainingData:textColumn:labelColumn:parameters:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

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

**Other overloads**:

```swift
init(trainingData: MLDataTable, textColumn: String, labelColumn: String, parameters: MLTextClassifier.ModelParameters = ModelParameters(validationData: nil)) throws
```

## Parameters

- `trainingData`: A data frame specifying the training data.
- `textColumn`: The name of the text column in the provided trainingData.
- `labelColumn`: The name of the label column in the provided trainingData.
- `parameters`: Model training parameters.

## See Also

### Creating and training a text classifier
- [init(trainingData:parameters:)](./init%28trainingdata,parameters%29.md)
  Creates a text classifier.
- [MLTextClassifier.DataSource](./datasource.md)
  A data source for a text classifier.
- [MLTextClassifier.ModelParameters](./modelparameters-swift.struct.md)
  Parameters that specify model training parameters and validation data.
- [let modelParameters: MLTextClassifier.ModelParameters](./modelparameters-swift.property.md)
  The configuration parameters that the text classifier used for training during initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/init(trainingdata:textcolumn:labelcolumn:parameters:))*