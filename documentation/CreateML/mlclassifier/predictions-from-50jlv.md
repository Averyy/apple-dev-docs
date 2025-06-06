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

#### Discussion

If the supplied data doesn’t match the expected columns (noted by the [`featureColumns`](mlclassifier/featurecolumns.md) property), this method throws an [`MLCreateError.type(reason:)`](mlcreateerror/type(reason:).md).

## Parameters

- `data`: The data you want the model to classify.

## See Also

- [func predictions(from: DataFrame) throws -> AnyColumn](mlclassifier/predictions(from:)-7mww4.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlclassifier/predictions(from:)-50jlv)*