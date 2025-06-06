# init(trainingData:targetColumn:featureColumns:)

**Framework**: Create ML  
**Kind**: init

Creates a classifier from the feature columns in the training data to predict the categories in the target column.

**Availability**:
- macOS 10.14+

## Declaration

```swift
init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]? = nil) throws
```

#### Discussion

To view details about the supporting model chosen by the [`MLClassifier`](mlclassifier.md), print the model’s description:

```swift
print(model)
```

## Parameters

- `trainingData`: A data table of training examples.
- `targetColumn`: The column name for the values in the training data that the classifier should predict.
- `featureColumns`: The column names for the values in the training data  that the classifier uses to predict   the target value.

## See Also

- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?) throws](mlclassifier/init(trainingdata:targetcolumn:featurecolumns:)-6ojd1.md)
  Creates a classifier.
- [var targetColumn: String](mlclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mlclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlclassifier/init(trainingdata:targetcolumn:featurecolumns:)-p3f6)*