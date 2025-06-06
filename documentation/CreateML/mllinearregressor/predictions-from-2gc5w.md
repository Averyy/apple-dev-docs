# predictions(from:)

**Framework**: Create ML  
**Kind**: method

Predicts the target value from the provided data.

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

A column of values predicted by the regressor.

## Parameters

- `data`: The data you want the model to make predictions from.

## See Also

- [func predictions(from: DataFrame) throws -> AnyColumn](mllinearregressor/predictions(from:)-7mob0.md)
  Predicts a column of labels for the given testing data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllinearregressor/predictions(from:)-2gc5w)*