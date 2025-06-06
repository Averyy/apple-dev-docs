# featureColumns

**Framework**: Create ML  
**Kind**: property

The names of the columns you selected at initialization to train the classifier.

**Availability**:
- macOS 10.14+

## Declaration

```swift
var featureColumns: [String] { get }
```

## See Also

- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?) throws](mlclassifier/init(trainingdata:targetcolumn:featurecolumns:)-6ojd1.md)
  Creates a classifier.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?) throws](mlclassifier/init(trainingdata:targetcolumn:featurecolumns:)-p3f6.md)
  Creates a classifier from the feature columns in the training data to predict the categories in the target column.
- [var targetColumn: String](mlclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlclassifier/featurecolumns)*