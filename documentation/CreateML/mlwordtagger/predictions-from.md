# predictions(from:)

**Framework**: Create ML  
**Kind**: method

Predicts sequences of labels, token locations, and token lengths from the input strings.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func predictions<S>(from texts: S) throws -> DataFrame where S : Sequence, S.Element == String
```

#### Return Value

A `DataFrame` containing predicted labels, token locations, and token lengths.

## Parameters

- `texts`: A sequence of strings to tokenize and tag.

## See Also

- [func prediction(from:)](mlwordtagger/prediction(from:).md)
  Predicts a tag for the input string.
- [func predictionWithConfidence(from:)](mlwordtagger/predictionwithconfidence(from:).md)
  Predicts tags and confidence scores for the input string. Predicts tags and confidence scores for the input string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/predictions(from:))*