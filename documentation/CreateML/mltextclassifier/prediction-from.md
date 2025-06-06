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

- [func predictions(from: [String]) throws -> [String]](mltextclassifier/predictions(from:)-1u3f2.md)
  Classifies an array of strings with labels.
- [func predictionWithConfidence(from: String) throws -> [String : Double]](mltextclassifier/predictionwithconfidence(from:).md)
  Predicts multiple possible labels and their confidence scores for the specified string.
- [func predictionsWithConfidence(from: [String]) throws -> [[String : Double]]](mltextclassifier/predictionswithconfidence(from:)-uezi.md)
  Predicts multiple possible labels and their confidence scores for each string in the specified array.
- [func predictions(from: MLDataColumn<String>) throws -> MLDataColumn<String>](mltextclassifier/predictions(from:)-40gtb.md)
  Classifies a data column with labels.
- [func predictionsWithConfidence(from: MLDataColumn<String>) throws -> MLDataColumn<[String : Double]>](mltextclassifier/predictionswithconfidence(from:)-1w9zo.md)
  Predicts multiple possible labels and their confidence scores for each string in the specified data column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/prediction(from:))*