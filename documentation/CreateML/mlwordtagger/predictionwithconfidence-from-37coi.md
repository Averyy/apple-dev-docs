# predictionWithConfidence(from:)

**Framework**: Create ML  
**Kind**: method

Predicts tags and confidence scores for each token in the specified token array.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func predictionWithConfidence(from tokens: [MLWordTagger.Token]) throws -> [[String : Double]]
```

#### Return Value

An array of dictionaries. Each dictionary corresponds to a token in the input token array. A dictionary entry contains a tag prediction with its associated confidence score.

## Parameters

- `tokens`: An array of tokens to tag.

## See Also

- [func predictions<S>(from: S) throws -> DataFrame](mlwordtagger/predictions(from:)-12r03.md)
  Predicts sequences of labels, token locations, and token lengths from the input strings.
- [func predictions(from: MLDataColumn<String>) throws -> MLDataTable](mlwordtagger/predictions(from:)-22b8d.md)
  Predicts sequences of labels, token locations, and token lengths from the input column containing strings.
- [func prediction(from: [MLWordTagger.Token]) throws -> [String]](mlwordtagger/prediction(from:)-7rqyq.md)
  Predicts a tag for each token in the specified array.
- [func prediction(from: String) throws -> [String]](mlwordtagger/prediction(from:)-r5gb.md)
  Predicts a tag for the input string.
- [func predictionWithConfidence(from: String) throws -> [[String : Double]]](mlwordtagger/predictionwithconfidence(from:)-398qj.md)
  Predicts tags and confidence scores for the input string. Predicts tags and confidence scores for the input string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/predictionwithconfidence(from:)-37coi)*