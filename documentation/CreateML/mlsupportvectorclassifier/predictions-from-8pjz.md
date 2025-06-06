# predictions(from:)

**Framework**: Create ML  
**Kind**: method

Classifies the provided data into the target categories.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func predictions(from data: MLDataTable) throws -> MLUntypedColumn
```

#### Return Value

A column of labels predicted by the classifier.

## Parameters

- `data`: The data you want the model to classify.

## See Also

- [func predictions(from: DataFrame) throws -> AnyColumn](mlsupportvectorclassifier/predictions(from:)-p5qk.md)
  Predicts a column of labels for the given testing data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/predictions(from:)-8pjz)*