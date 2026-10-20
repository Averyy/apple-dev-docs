# predictionWithConfidence(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Predicts tags and confidence scores for the input string. Predicts tags and confidence scores for the input string.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func predictionWithConfidence(from text: String) throws -> [[String : Double]]
```

**Other overloads**:

```swift
func predictionWithConfidence(from tokens: [MLWordTagger.Token]) throws -> [[String : Double]]
```

#### Return Value

An array of dictionaries. Each dictionary corresponds to a token in the input text string. A dictionary entry contains a tag prediction with its associated confidence score.

## Parameters

- `text`: The string to tag.

## See Also

### Testing a word tagger
- [func prediction(from:)](./prediction%28from%29.md)
  Predicts a tag for the input string.
- [func predictions(from:)](./predictions%28from%29.md)
  Predicts sequences of labels, token locations, and token lengths from the input strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/predictionwithconfidence(from:))*