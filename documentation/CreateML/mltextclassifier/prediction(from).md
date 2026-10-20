# prediction(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

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

### Testing a text classifier
- [func predictions(from:)](./predictions%28from%29.md)
  Classifies an array of strings with labels.
- [func predictionWithConfidence(from: String) throws -> [String : Double]](./predictionwithconfidence%28from%29.md)
  Predicts multiple possible labels and their confidence scores for the specified string.
- [func predictionsWithConfidence(from:)](./predictionswithconfidence%28from%29.md)
  Predicts multiple possible labels and their confidence scores for each string in the specified array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/prediction(from:))*