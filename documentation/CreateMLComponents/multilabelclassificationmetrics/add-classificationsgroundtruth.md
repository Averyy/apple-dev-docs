# add(classifications:groundTruth:)

**Framework**: Create ML Components  
**Kind**: method

Updates the metrics with more classifications and ground truth labels.

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
mutating func add(classifications: some Sequence<ClassificationDistribution<Label>>, groundTruth: some Sequence<Set<Label>>)
```

#### Discussion

The classifications and ground truth sequences are matched element by element in the order they are provided. Both sequences must have the same number of elements.

## Parameters

- `classifications`: A collection of classifications.
- `groundTruth`: A collection of true labels.

## See Also

- [func add(some Sequence<(classification: ClassificationDistribution<Label>, labels: Set<Label>)>)](multilabelclassificationmetrics/add(_:).md)
  Updates the metrics with more pairs of classifications and ground truth labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/multilabelclassificationmetrics/add(classifications:groundtruth:))*