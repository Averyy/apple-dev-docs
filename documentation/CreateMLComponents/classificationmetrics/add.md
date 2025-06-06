# add(_:)

**Framework**: Create ML Components  
**Kind**: method

Updates the metrics with more predicted and ground truth label pairs.

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
mutating func add(_ pairs: some Sequence<(predicted: Label, label: Label)>)
```

## Parameters

- `pairs`: A collection of predicted and true label pairs.

## See Also

- [func add(predicted: some Sequence<Label>, groundTruth: some Sequence<Label>)](classificationmetrics/add(predicted:groundtruth:).md)
  Updates the metrics with more predicted and ground truth labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationmetrics/add(_:))*