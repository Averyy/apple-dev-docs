# prediction(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Predicts the label for the given term.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func prediction(from text: String) throws -> String
```

#### Return Value

A label.

## Parameters

- `text`: The input term.

## See Also

### Testing a gazetteer
- [func predictions(from:)](./predictions%28from%29.md)
  Predicts the labels for the given terms.
- [func predictions(from: [String]) throws -> [String]](./predictions%28from%29-2rej.md)
  Predicts the labels for the given terms.
- [func predictions(from: MLDataColumn<String>) throws -> MLDataColumn<String>](./predictions%28from%29-2jaui.md)
  Predicts the labels for the given terms in the table column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlgazetteer/prediction(from:))*