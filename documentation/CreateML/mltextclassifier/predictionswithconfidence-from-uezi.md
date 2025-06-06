# predictionsWithConfidence(from:)

**Framework**: Create ML  
**Kind**: method

Predicts multiple possible labels and their confidence scores for each string in the specified array.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func predictionsWithConfidence(from texts: [String]) throws -> [[String : Double]]
```

#### Return Value

An array of dictionaries. Each dictionary corresponds to a string in the input array. A dictionary entry contains a label prediction with its associated confidence score.

## Parameters

- `texts`: The array of strings to classify.

## See Also

- [func prediction(from: String) throws -> String](mltextclassifier/prediction(from:).md)
  Classifies a string with a label.
- [func predictions(from: [String]) throws -> [String]](mltextclassifier/predictions(from:)-1u3f2.md)
  Classifies an array of strings with labels.
- [func predictionWithConfidence(from: String) throws -> [String : Double]](mltextclassifier/predictionwithconfidence(from:).md)
  Predicts multiple possible labels and their confidence scores for the specified string.
- [func predictions(from: MLDataColumn<String>) throws -> MLDataColumn<String>](mltextclassifier/predictions(from:)-40gtb.md)
  Classifies a data column with labels.
- [func predictionsWithConfidence(from: MLDataColumn<String>) throws -> MLDataColumn<[String : Double]>](mltextclassifier/predictionswithconfidence(from:)-1w9zo.md)
  Predicts multiple possible labels and their confidence scores for each string in the specified data column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/predictionswithconfidence(from:)-uezi)*