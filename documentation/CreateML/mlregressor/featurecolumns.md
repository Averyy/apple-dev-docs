# featureColumns

**Framework**: Create ML  
**Kind**: property

The names of the columns you selected at initialization to train the regressor.

**Availability**:
- macOS 10.14+

## Declaration

```swift
var featureColumns: [String] { get }
```

## See Also

- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?) throws](mlregressor/init(trainingdata:targetcolumn:featurecolumns:)-5mhd2.md)
  Creates a regressor.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?) throws](mlregressor/init(trainingdata:targetcolumn:featurecolumns:)-56rvo.md)
  Creates a regressor from the feature columns in the training data to predict the values in the target column.
- [var targetColumn: String](mlregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlregressor/featurecolumns)*