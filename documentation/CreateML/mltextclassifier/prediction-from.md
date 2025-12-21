# prediction(from:)

**Framework**: Create ML  
**Kind**: method

Classifies a string with a label.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func prediction(from text: String) throws -> String
```

#### Return Value

The label for the given string.

## Parameters

- `text`: The string to be classified.

## See Also

- [func predictions(from:)](mltextclassifier/predictions(from:).md)
  Classifies an array of strings with labels.
- [func predictionWithConfidence(from: String) throws -> [String : Double]](mltextclassifier/predictionwithconfidence(from:).md)
  Predicts multiple possible labels and their confidence scores for the specified string.
- [func predictionsWithConfidence(from:)](mltextclassifier/predictionswithconfidence(from:).md)
  Predicts multiple possible labels and their confidence scores for each string in the specified array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/prediction(from:))*