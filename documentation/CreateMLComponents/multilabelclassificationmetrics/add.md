# add(_:)

**Framework**: Create ML Components  
**Kind**: method

Updates the metrics with more pairs of classifications and ground truth labels.

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
mutating func add(_ pairs: some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>)
```

## Parameters

- `pairs`: A sequence of classifications and true label pairs.

## See Also

- [func add(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>)](multilabelclassificationmetrics/add(classifications:groundtruth:).md)
  Updates the metrics with more classifications and ground truth labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics/add(_:))*