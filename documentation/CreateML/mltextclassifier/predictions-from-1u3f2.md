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
- [func predictionsWithConfidence(from: [String]) throws -> [[String : Double]]](mltextclassifier/predictionswithconfidence(from:)-uezi.md)
  Predicts multiple possible labels and their confidence scores for each string in the specified array.
- [func predictions(from: MLDataColumn<String>) throws -> MLDataColumn<String>](mltextclassifier/predictions(from:)-40gtb.md)
  Classifies a data column with labels.
- [func predictionsWithConfidence(from: MLDataColumn<String>) throws -> MLDataColumn<[String : Double]>](mltextclassifier/predictionswithconfidence(from:)-1w9zo.md)
  Predicts multiple possible labels and their confidence scores for each string in the specified data column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/predictions(from:)-1u3f2)*