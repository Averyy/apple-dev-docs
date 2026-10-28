# predictions(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Predicts the labels for the given terms in the table column.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

## Declaration

```swift
func predictions(from texts: MLDataColumn<String>) throws -> MLDataColumn<String>
```

**Other overloads**:

```swift
func predictions(from texts: [String]) throws -> [String]
```

## Return Value

A column of labels.

## Parameters

- `texts`: The column of terms.

## See Also

### Testing a gazetteer
- [func prediction(from: String) throws -> String](./prediction%28from%29.md)
  Predicts the label for the given term.
- [func predictions(from:)](./predictions%28from%29.md)
  Predicts the labels for the given terms.
- [func predictions(from: [String]) throws -> [String]](./predictions%28from%29-2rej.md)
  Predicts the labels for the given terms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlgazetteer/predictions(from:)-2jaui)*