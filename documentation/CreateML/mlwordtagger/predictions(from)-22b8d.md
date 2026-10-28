# predictions(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Predicts sequences of labels, token locations, and token lengths from the input column containing strings.

**Availability**:
- macOS 10.14+ - Deprecated in 13.0

## Declaration

```swift
func predictions(from texts: MLDataColumn<String>) throws -> MLDataTable
```

**Other overloads**:

```swift
func predictions<S>(from texts: S) throws -> DataFrame where S : Sequence, S.Element == String
```

## Return Value

A table containing predicted labels, token locations, and token lengths.

## Parameters

- `texts`: A column of strings to tokenize and tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/predictions(from:)-22b8d)*