# init(trainingData:targetColumn:featureColumns:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a classifier.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]? = nil) throws
```

**Other overloads**:

```swift
init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]? = nil) throws
```

## Parameters

- `trainingData`: The training data
- `targetColumn`: Name of the column containing the class labels
- `featureColumns`: Names of the columns containing feature values. If `nil` all columns, other than the target column, will be used as feature values.

## See Also

### Creating and training a classifier
- [var targetColumn: String](./targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](./featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlclassifier/init(trainingdata:targetcolumn:featurecolumns:))*