# init(trainingData:targetColumn:featureColumns:parameters:)

**Framework**: Create ML  
**Kind**: init

Creates a boosted tree regressor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]? = nil, parameters: MLBoostedTreeRegressor.ModelParameters = ModelParameters(validation: .split(strategy: .automatic))) throws
```

## Parameters

- `trainingData`: The training data
- `targetColumn`: Name of the column containing the target values
- `featureColumns`: Names of the columns containing feature values. If   all columns, other than the target   column, will be used as feature values.
- `parameters`: Model training parameters

## See Also

- [var targetColumn: String](mlboostedtreeregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](mlboostedtreeregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:))*