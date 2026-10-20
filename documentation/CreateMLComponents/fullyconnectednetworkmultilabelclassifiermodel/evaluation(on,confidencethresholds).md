# evaluation(on:confidenceThresholds:)

**Framework**: Create ML Components  
**Kind**: method

Computes evaluation metrics on annotated examples.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func evaluation(on input: some Collection<AnnotatedFeature<MLShapedArray<Scalar>, Set<Label>>>, confidenceThresholds: [Label : Float]) throws -> MultiLabelClassificationMetrics<Label>
```

#### Return Value

Multi-label classifier metrics.

## Parameters

- `input`: A collection of annotated examples.
- `confidenceThresholds`: A dictionary of label and confidence threshold pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifiermodel/evaluation(on:confidencethresholds:))*