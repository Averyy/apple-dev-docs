# init(trainingData:targetColumn:featureColumns:parameters:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a Decision Tree Regressor from the feature columns in the training data to predict the values in the target column.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 13.0
- visionOS 1.0+

> **Deprecated**: Use DataFrame instead of MLDataTable when initializing.

## Declaration

```swift
init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]? = nil, parameters: MLDecisionTreeRegressor.ModelParameters = ModelParameters(validationData: nil)) throws
```

**Other overloads**:

```swift
init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]? = nil, parameters: MLDecisionTreeRegressor.ModelParameters = ModelParameters(validation: .split(strategy: .automatic))) throws
```

## Parameters

- `trainingData`: A data table of training examples.
- `targetColumn`: The column name for the values in the training data the regressor should predict.
- `featureColumns`: The column names for the values in the training data that the regressor uses to predict the target value.
- `parameters`: Model training parameters. See [`MLDecisionTreeRegressor.ModelParameters`](./modelparameters-swift.struct.md) for the defaults.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:)-7cjvn)*