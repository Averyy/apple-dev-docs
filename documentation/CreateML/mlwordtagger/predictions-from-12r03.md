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

- [func predictions(from: MLDataColumn<String>) throws -> MLDataTable](mlwordtagger/predictions(from:)-22b8d.md)
  Predicts sequences of labels, token locations, and token lengths from the input column containing strings.
- [func prediction(from: [MLWordTagger.Token]) throws -> [String]](mlwordtagger/prediction(from:)-7rqyq.md)
  Predicts a tag for each token in the specified array.
- [func prediction(from: String) throws -> [String]](mlwordtagger/prediction(from:)-r5gb.md)
  Predicts a tag for the input string.
- [func predictionWithConfidence(from: String) throws -> [[String : Double]]](mlwordtagger/predictionwithconfidence(from:)-398qj.md)
  Predicts tags and confidence scores for the input string. Predicts tags and confidence scores for the input string.
- [func predictionWithConfidence(from: [MLWordTagger.Token]) throws -> [[String : Double]]](mlwordtagger/predictionwithconfidence(from:)-37coi.md)
  Predicts tags and confidence scores for each token in the specified token array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/predictions(from:)-12r03)*