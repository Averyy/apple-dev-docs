# predictions(from:)

**Framework**: Create ML  
**Kind**: method

Predicts the labels for the given terms in the table column.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func predictions(from texts: MLDataColumn<String>) throws -> MLDataColumn<String>
```

#### Return Value

A column of labels.

## Parameters

- `texts`: The column of terms.

## See Also

- [func prediction(from: String) throws -> String](mlgazetteer/prediction(from:).md)
  Predicts the label for the given term.
- [func predictions(from:)](mlgazetteer/predictions(from:).md)
  Predicts the labels for the given terms.
- [func predictions(from: [String]) throws -> [String]](mlgazetteer/predictions(from:)-2rej.md)
  Predicts the labels for the given terms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlgazetteer/predictions(from:)-2jaui)*