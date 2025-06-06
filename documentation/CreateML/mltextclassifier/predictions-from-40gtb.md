# predictions(from:)

**Framework**: Create ML  
**Kind**: method

Classifies a data column with labels.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func predictions(from texts: MLDataColumn<String>) throws -> MLDataColumn<String>
```

#### Return Value

An array of labels for the given strings.

## Parameters

- `texts`: The data column of strings to be classified.

## See Also

- [func prediction(from: String) throws -> String](mltextclassifier/prediction(from:).md)
  Classifies a string with a label.
- [func predictions(from: [String]) throws -> [String]](mltextclassifier/predictions(from:)-1u3f2.md)
  Classifies an array of strings with labels.
- [func predictionWithConfidence(from: String) throws -> [String : Double]](mltextclassifier/predictionwithconfidence(from:).md)
  Predicts multiple possible labels and their confidence scores for the specified string.
- [func predictionsWithConfidence(from: [String]) throws -> [[String : Double]]](mltextclassifier/predictionswithconfidence(from:)-uezi.md)
  Predicts multiple possible labels and their confidence scores for each string in the specified array.
- [func predictionsWithConfidence(from: MLDataColumn<String>) throws -> MLDataColumn<[String : Double]>](mltextclassifier/predictionswithconfidence(from:)-1w9zo.md)
  Predicts multiple possible labels and their confidence scores for each string in the specified data column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/predictions(from:)-40gtb)*