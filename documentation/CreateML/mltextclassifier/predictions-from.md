# predictions(from:)

**Framework**: Create ML  
**Kind**: method

Classifies an array of strings with labels.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func predictions(from texts: [String]) throws -> [String]
```

#### Return Value

An array of labels for the given strings.

## Parameters

- `texts`: The array of strings to be classified.

## See Also

- [func prediction(from: String) throws -> String](mltextclassifier/prediction(from:).md)
  Classifies a string with a label.
- [func predictionWithConfidence(from: String) throws -> [String : Double]](mltextclassifier/predictionwithconfidence(from:).md)
  Predicts multiple possible labels and their confidence scores for the specified string.
- [func predictionsWithConfidence(from:)](mltextclassifier/predictionswithconfidence(from:).md)
  Predicts multiple possible labels and their confidence scores for each string in the specified array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/predictions(from:))*