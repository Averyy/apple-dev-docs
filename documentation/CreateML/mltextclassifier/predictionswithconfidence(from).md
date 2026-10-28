# predictionsWithConfidence(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

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

**Other overloads**:

```swift
func predictionsWithConfidence(from texts: MLDataColumn<String>) throws -> MLDataColumn<[String : Double]>
```

## Return Value

An array of dictionaries. Each dictionary corresponds to a string in the input array. A dictionary entry contains a label prediction with its associated confidence score.

## Parameters

- `texts`: The array of strings to classify.

## See Also

### Testing a text classifier
- [func prediction(from: String) throws -> String](./prediction%28from%29.md)
  Classifies a string with a label.
- [func predictions(from:)](./predictions%28from%29.md)
  Classifies an array of strings with labels.
- [func predictionWithConfidence(from: String) throws -> [String : Double]](./predictionwithconfidence%28from%29.md)
  Predicts multiple possible labels and their confidence scores for the specified string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/predictionswithconfidence(from:))*