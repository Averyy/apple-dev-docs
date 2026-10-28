# prediction(from:confidenceThresholds:)

**Framework**: Create ML Components  
**Kind**: method  
**Role**: Instance Method

Performs a prediction and keeps label-confidence pairs that are greater than or equal to the provided confidence thresholds.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func prediction(from input: FullyConnectedNetworkMultiLabelClassifierModel<Scalar, Label>.Input, confidenceThresholds: [Label : Scalar]) throws -> ClassificationDistribution<Label>
```

**Other overloads**:

```swift
func prediction<S>(from input: S, confidenceThresholds: [Label : Scalar]) throws -> [ClassificationDistribution<Label>] where S : Sequence, S.Element == MLShapedArray<Scalar>
```

## Return Value

A dictionary of labels and confidences.

## Discussion

When the confidence threshold is `NaN`, the label-confidence pair is not included in the result, regardless of the label’s confidence.

## Parameters

- `input`: The classifier input.
- `confidenceThresholds`: A dictionary of label and confidence threshold pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/fullyconnectednetworkmultilabelclassifiermodel/prediction(from:confidencethresholds:))*