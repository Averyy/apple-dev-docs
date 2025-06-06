# predictions(from:)

**Framework**: Create ML  
**Kind**: method

Classifies the provided data into the target categories.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func predictions(from data: MLDataTable) throws -> MLUntypedColumn
```

#### Return Value

A column of labels predicted by the classifier.

## Parameters

- `data`: The data you want the model to classify.

## See Also

- [func predictions(from: DataFrame) throws -> AnyColumn](mldecisiontreeclassifier/predictions(from:)-2clno.md)
  Predicts a column of labels for the given testing data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeclassifier/predictions(from:)-2di6j)*