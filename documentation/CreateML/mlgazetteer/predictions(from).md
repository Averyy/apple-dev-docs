# predictions(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Predicts the labels for the given terms.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func predictions(from texts: [String]) throws -> [String]
```

**Other overloads**:

```swift
func predictions(from texts: MLDataColumn<String>) throws -> MLDataColumn<String>
```

## Return Value

An array of labels.

## Parameters

- `texts`: The array of input terms.

## See Also

### Testing a gazetteer
- [func prediction(from: String) throws -> String](./prediction%28from%29.md)
  Predicts the label for the given term.
- [func predictions(from: [String]) throws -> [String]](./predictions%28from%29-2rej.md)
  Predicts the labels for the given terms.
- [func predictions(from: MLDataColumn<String>) throws -> MLDataColumn<String>](./predictions%28from%29-2jaui.md)
  Predicts the labels for the given terms in the table column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlgazetteer/predictions(from:))*