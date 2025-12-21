# init(trainingData:targetColumn:featureColumns:)

**Framework**: Create ML  
**Kind**: init

Creates a regressor.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]? = nil) throws
```

## Parameters

- `trainingData`: The training data
- `targetColumn`: Name of the column containing the target values
- `featureColumns`: Names of the columns containing feature values. If   all columns, other than the target   column, will be used as feature values.

## See Also

- [var targetColumn: String](mlregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](mlregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlregressor/init(trainingdata:targetcolumn:featurecolumns:))*