# predictions(from:)

**Framework**: Create ML  
**Kind**: method

Predicts the target value from the provided data.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func predictions(from data: MLDataTable) throws -> MLUntypedColumn
```

#### Return Value

A column of values predicted by the regressor.

#### Discussion

If the supplied data doesn’t match the expected columns (noted by the [`featureColumns`](mlregressor/featurecolumns.md) property), this method throws an [`MLCreateError.type(reason:)`](mlcreateerror/type(reason:).md).

## Parameters

- `data`: The data you want the model to make predictions from.

## See Also

- [func predictions(from: DataFrame) throws -> AnyColumn](mlregressor/predictions(from:)-6e6ti.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlregressor/predictions(from:)-3gkt1)*