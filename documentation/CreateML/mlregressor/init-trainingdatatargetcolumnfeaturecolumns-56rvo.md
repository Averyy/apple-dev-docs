# init(trainingData:targetColumn:featureColumns:)

**Framework**: Create ML  
**Kind**: init

Creates a regressor from the feature columns in the training data to predict the values in the target column.

**Availability**:
- macOS 10.14+

## Declaration

```swift
init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]? = nil) throws
```

#### Discussion

To view details about the supporting model picked by the [`MLRegressor`](mlregressor.md), print the model’s description:

```swift
print(model)
```

## Parameters

- `trainingData`: A data table of training examples.
- `targetColumn`: The column name for the values in the training data the regressor should predict.
- `featureColumns`: The column names for the values in the training data that the regressor uses to predict the   target value.

## See Also

- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?) throws](mlregressor/init(trainingdata:targetcolumn:featurecolumns:)-5mhd2.md)
  Creates a regressor.
- [var targetColumn: String](mlregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](mlregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlregressor/init(trainingdata:targetcolumn:featurecolumns:)-56rvo)*