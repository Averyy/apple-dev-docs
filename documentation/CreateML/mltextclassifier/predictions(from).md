# predictions(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

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

**Other overloads**:

```swift
func predictions(from texts: MLDataColumn<String>) throws -> MLDataColumn<String>
```

## Return Value

An array of labels for the given strings.

## Parameters

- `texts`: The array of strings to be classified.

## See Also

### Testing a text classifier
- [func prediction(from: String) throws -> String](./prediction%28from%29.md)
  Classifies a string with a label.
- [func predictionWithConfidence(from: String) throws -> [String : Double]](./predictionwithconfidence%28from%29.md)
  Predicts multiple possible labels and their confidence scores for the specified string.
- [func predictionsWithConfidence(from:)](./predictionswithconfidence%28from%29.md)
  Predicts multiple possible labels and their confidence scores for each string in the specified array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/predictions(from:))*