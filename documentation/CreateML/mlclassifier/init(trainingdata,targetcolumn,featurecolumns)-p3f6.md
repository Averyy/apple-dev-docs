# init(trainingData:targetColumn:featureColumns:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a classifier from the feature columns in the training data to predict the categories in the target column.

**Availability**:
- macOS 10.14+ - Deprecated in 13.0

> **Deprecated**: Use DataFrame instead of MLDataTable when initializing.

## Declaration

```swift
init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]? = nil) throws
```

**Other overloads**:

```swift
init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]? = nil) throws
```

## Discussion

To view details about the supporting model chosen by the [`MLClassifier`](../mlclassifier.md), print the model’s description:

```swift
print(model)
```

## Parameters

- `trainingData`: A data table of training examples.
- `targetColumn`: The column name for the values in the training data that the classifier should predict.
- `featureColumns`: The column names for the values in the training data  that the classifier uses to predict the target value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlclassifier/init(trainingdata:targetcolumn:featurecolumns:)-p3f6)*