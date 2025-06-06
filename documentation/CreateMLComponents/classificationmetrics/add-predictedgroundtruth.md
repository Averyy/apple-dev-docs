# add(predicted:groundTruth:)

**Framework**: Create ML Components  
**Kind**: method

Updates the metrics with more predicted and ground truth labels.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
mutating func add(predicted: some Sequence<Label>, groundTruth: some Sequence<Label>)
```

#### Discussion

The predicted and ground truth sequences are matched element by element in the order they are provided. Both sequences must have the same number of elements.

## Parameters

- `predicted`: The predicted labels.
- `groundTruth`: The true labels.

## See Also

- [func add(some Sequence<(predicted: Label, label: Label)>)](classificationmetrics/add(_:).md)
  Updates the metrics with more predicted and ground truth label pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationmetrics/add(predicted:groundtruth:))*