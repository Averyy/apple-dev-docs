# predictionWithConfidence(from:)

**Framework**: Create ML  
**Kind**: method

Predicts multiple possible labels and their confidence scores for the specified string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func predictionWithConfidence(from text: String) throws -> [String : Double]
```

#### Return Value

A dictionary of label predictions and confidence scores.

## Parameters

- `text`: The string to classify.

## See Also

- [func prediction(from: String) throws -> String](mltextclassifier/prediction(from:).md)
  Classifies a string with a label.
- [func predictions(from:)](mltextclassifier/predictions(from:).md)
  Classifies an array of strings with labels.
- [func predictionsWithConfidence(from:)](mltextclassifier/predictionswithconfidence(from:).md)
  Predicts multiple possible labels and their confidence scores for each string in the specified array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/predictionwithconfidence(from:))*