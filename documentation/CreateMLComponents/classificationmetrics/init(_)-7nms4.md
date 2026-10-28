# init(_:)

**Framework**: Create ML Components  
**Kind**: init  
**Role**: Initializer

Creates classification metrics from a temporal sequence of annotated classifications.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
init<S, Inner>(_ predicted: S) async throws where S : Sequence, Inner : TemporalSequence, S.Element == AnnotatedFeature<Inner, Label>, Inner.Feature == ClassificationDistribution<Label>
```

**Other overloads**:

```swift
init(_ pairs: some Sequence<(predicted: Label, label: Label)>)
```

## Discussion

- Parameters

  - predicted: The predicted sequence of annotated temporal sequences of classification distributions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationmetrics/init(_:)-7nms4)*