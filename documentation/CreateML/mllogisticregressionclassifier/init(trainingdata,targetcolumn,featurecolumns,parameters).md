# init(trainingData:targetColumn:featureColumns:parameters:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a logistic regression classifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]? = nil, parameters: MLLogisticRegressionClassifier.ModelParameters = ModelParameters(validation: .split(strategy: .automatic))) throws
```

**Other overloads**:

```swift
init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]? = nil, parameters: MLLogisticRegressionClassifier.ModelParameters = ModelParameters(validationData: nil)) throws
```

## Parameters

- `trainingData`: The training data
- `targetColumn`: Name of the column containing the class labels
- `featureColumns`: Names of the columns containing feature values. If `nil` all columns, other than the target column, will be used as feature values.
- `parameters`: Model training parameters

## See Also

### Training a logistic regression classifier synchronously
- [var targetColumn: String](./targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](./featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllogisticregressionclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:))*