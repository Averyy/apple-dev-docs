# predictionsWithConfidence(from:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Predicts multiple possible labels and their confidence scores for each string in the specified data column.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 11.0+ - Deprecated in 13.0
- visionOS 1.0+

> **Deprecated**: Use DataFrame instead of MLDataTable.

## Declaration

```swift
func predictionsWithConfidence(from texts: MLDataColumn<String>) throws -> MLDataColumn<[String : Double]>
```

**Other overloads**:

```swift
func predictionsWithConfidence(from texts: [String]) throws -> [[String : Double]]
```

## Return Value

A data column of dictionaries. Each dictionary corresponds to a string in the input data column. A dictionary entry contains a label prediction with its associated confidence score.

## Parameters

- `texts`: The data column of strings to classify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/predictionswithconfidence(from:)-1w9zo)*