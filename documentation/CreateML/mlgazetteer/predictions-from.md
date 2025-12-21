# predictions(from:)

**Framework**: Create ML  
**Kind**: method

Predicts the labels for the given terms.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func predictions(from texts: [String]) throws -> [String]
```

#### Return Value

An array of labels.

## Parameters

- `texts`: The array of input terms.

## See Also

- [func prediction(from: String) throws -> String](mlgazetteer/prediction(from:).md)
  Predicts the label for the given term.
- [func predictions(from: [String]) throws -> [String]](mlgazetteer/predictions(from:)-2rej.md)
  Predicts the labels for the given terms.
- [func predictions(from: MLDataColumn<String>) throws -> MLDataColumn<String>](mlgazetteer/predictions(from:)-2jaui.md)
  Predicts the labels for the given terms in the table column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlgazetteer/predictions(from:))*