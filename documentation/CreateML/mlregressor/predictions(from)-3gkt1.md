# predictions(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Predicts the target value from the provided data.

**Availability**:
- macOS 10.14+ - Deprecated in 13.0

> **Deprecated**: Use DataFrame instead of MLDataTable.

## Declaration

```swift
func predictions(from data: MLDataTable) throws -> MLUntypedColumn
```

**Other overloads**:

```swift
func predictions(from data: DataFrame) throws -> AnyColumn
```

## Return Value

A column of values predicted by the regressor.

## Discussion

If the supplied data doesn’t match the expected columns (noted by the [`featureColumns`](./featurecolumns.md) property), this method throws an [`MLCreateError.type(reason:)`](../mlcreateerror/type%28reason%29.md).

## Parameters

- `data`: The data you want the model to make predictions from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlregressor/predictions(from:)-3gkt1)*