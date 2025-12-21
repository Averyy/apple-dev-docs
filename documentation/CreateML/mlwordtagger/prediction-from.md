# prediction(from:)

**Framework**: Create ML  
**Kind**: method

Predicts a tag for the input string.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func prediction(from text: String) throws -> [String]
```

#### Return Value

An array of tags for the tokens in the string.

## Parameters

- `text`: The string to tag.

## See Also

- [func predictions(from:)](mlwordtagger/predictions(from:).md)
  Predicts sequences of labels, token locations, and token lengths from the input strings.
- [func predictionWithConfidence(from:)](mlwordtagger/predictionwithconfidence(from:).md)
  Predicts tags and confidence scores for the input string. Predicts tags and confidence scores for the input string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/prediction(from:))*