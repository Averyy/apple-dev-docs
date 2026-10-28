# evaluation(on:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Computes evaluation metrics.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func evaluation(on labeledTexts: [String : [String]]) -> MLClassifierMetrics
```

**Other overloads**:

```swift
func evaluation(on labeledTexts: MLTextClassifier.DataSource) -> MLClassifierMetrics
```

## Return Value

Classifier metrics.

## Parameters

- `labeledTexts`: A dictionary of labeled texts to evaluate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/evaluation(on:)-3h6eu)*