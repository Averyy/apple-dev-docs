# prediction(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Predicts a tag for the input string.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func prediction(from text: String) throws -> [String]
```

**Other overloads**:

```swift
func prediction(from tokens: [MLWordTagger.Token]) throws -> [String]
```

#### Return Value

An array of tags for the tokens in the string.

## Parameters

- `text`: The string to tag.

## See Also

### Testing a word tagger
- [func predictions(from:)](./predictions%28from%29.md)
  Predicts sequences of labels, token locations, and token lengths from the input strings.
- [func predictionWithConfidence(from:)](./predictionwithconfidence%28from%29.md)
  Predicts tags and confidence scores for the input string. Predicts tags and confidence scores for the input string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/prediction(from:))*