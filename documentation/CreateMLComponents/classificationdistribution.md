# ClassificationDistribution

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

A classification distribution that contains a probability for each classification label.

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
struct ClassificationDistribution<Label> where Label : Hashable
```

## Topics

### Creating the distribution
- [init<C>(C)](./classificationdistribution/init%28_%29.md)
  Creates a classification distribution.
### Getting the properties
- [var endIndex: Int](./classificationdistribution/endindex.md)
  The index of the final element in the classification distribution.
- [var labelsSortedByProbability: [Label]](./classificationdistribution/labelssortedbyprobability.md)
  The labels sorted  by decreasing probability.
- [var mostLikelyLabel: Label?](./classificationdistribution/mostlikelylabel.md)
  The label with the highest probability.
- [var startIndex: Int](./classificationdistribution/startindex.md)
  The index of the initial element in the classification distribution.
### Getting the index
- [func index(after: Int) -> Int](./classificationdistribution/index%28after%29.md)
  Returns the index immediately after an element index.
- [func index(before: Int) -> Int](./classificationdistribution/index%28before%29.md)
  Returns the index immediately before an element index.
### Labeling and mapping
- [func topLabels(Int) -> [Label]](./classificationdistribution/toplabels%28_%29.md)
  Computes the most likely labels in the classification set.
- [func map<T>((Classification<Label>) throws -> Classification<T>) rethrows -> ClassificationDistribution<T>](./classificationdistribution/map%28_%29.md)
  Creates a new classification distribution by applying a transformation to every element.
### Accessing by subscript
- [subscript(_:)](./classificationdistribution/subscript%28_%29.md)
  Accesses a contiguous range of elements.

## Relationships

### Conforms To
- [Collection](../Swift/collection.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Metrics
- [struct Classification](./classification.md)
  An item in a classification result.
- [struct ClassificationMetrics](./classificationmetrics.md)
  Classification metrics.
- [struct MultiLabelClassificationMetrics](./multilabelclassificationmetrics.md)
  Multi-label classification metrics.
- [func rootMeanSquaredError<T>([AnnotatedPrediction<T, T>]) -> T](./rootmeansquarederror%28_%29.md)
  Computes the root mean squared error between predicted and ground truth values.
- [func rootMeanSquaredError<T>(some Collection, some Collection) -> T](./rootmeansquarederror%28_,_%29.md)
  Computes the root mean squared error between predicted and ground truth values.
- [func maximumAbsoluteError<T>([AnnotatedPrediction<T, T>]) -> T](./maximumabsoluteerror%28_%29.md)
  Computes the maximum absolute error between predicted and ground truth values.
- [func maximumAbsoluteError<T>(some Collection, some Collection) -> T](./maximumabsoluteerror%28_,_%29.md)
  Computes the maximum absolute error between predicted and ground truth values.
- [func meanAbsoluteError<T>([AnnotatedPrediction<T, T>]) -> T](./meanabsoluteerror%28_%29.md)
  Computes the mean absolute error between predicted and ground truth values.
- [func meanAbsoluteError<T>(some Collection, some Collection) -> T](./meanabsoluteerror%28_,_%29.md)
  Computes the mean absolute error between predicted and ground truth values.
- [func meanAbsolutePercentageError<T>([AnnotatedPrediction<T, T>]) -> T](./meanabsolutepercentageerror%28_%29.md)
  Computes the mean absolute percentage error between predicted and ground truth values.
- [func meanSquaredError<T>([AnnotatedPrediction<T, T>]) -> T](./meansquarederror%28_%29.md)
  Computes the root mean squared error between predicted and ground truth values.
- [func meanSquaredError<T>(some Collection, some Collection) -> T](./meansquarederror%28_,_%29.md)
  Computes the mean squared error between predicted and ground truth values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationdistribution)*