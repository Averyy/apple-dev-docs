# predictionWithConfidence(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Predicts tags and confidence scores for each token in the specified token array.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func predictionWithConfidence(from tokens: [MLWordTagger.Token]) throws -> [[String : Double]]
```

**Other overloads**:

```swift
func predictionWithConfidence(from text: String) throws -> [[String : Double]]
```

## Return Value

An array of dictionaries. Each dictionary corresponds to a token in the input token array. A dictionary entry contains a tag prediction with its associated confidence score.

## Parameters

- `tokens`: An array of tokens to tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/predictionwithconfidence(from:)-37coi)*