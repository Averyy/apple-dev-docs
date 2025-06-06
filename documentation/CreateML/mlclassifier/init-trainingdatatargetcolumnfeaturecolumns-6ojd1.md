# init(trainingData:targetColumn:featureColumns:)

**Framework**: Create ML  
**Kind**: init

Creates a classifier.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]? = nil) throws
```

## Parameters

- `trainingData`: The training data
- `targetColumn`: Name of the column containing the class labels
- `featureColumns`: Names of the columns containing feature values. If   all columns, other than the target   column, will be used as feature values.

## See Also

- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?) throws](mlclassifier/init(trainingdata:targetcolumn:featurecolumns:)-p3f6.md)
  Creates a classifier from the feature columns in the training data to predict the categories in the target column.
- [var targetColumn: String](mlclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mlclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlclassifier/init(trainingdata:targetcolumn:featurecolumns:)-6ojd1)*