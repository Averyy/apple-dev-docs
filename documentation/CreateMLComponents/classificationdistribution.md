# ClassificationDistribution

**Framework**: Create ML Components  
**Kind**: struct

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
- [init<C>(C)](classificationdistribution/init(_:).md)
  Creates a classification distribution.
### Getting the properties
- [var endIndex: Int](classificationdistribution/endindex.md)
  The index of the final element in the classification distribution.
- [var labelsSortedByProbability: [Label]](classificationdistribution/labelssortedbyprobability.md)
  The labels sorted  by decreasing probability.
- [var mostLikelyLabel: Label?](classificationdistribution/mostlikelylabel.md)
  The label with the highest probability.
- [var startIndex: Int](classificationdistribution/startindex.md)
  The index of the initial element in the classification distribution.
### Getting the index
- [func index(after: Int) -> Int](classificationdistribution/index(after:).md)
  Returns the index immediately after an element index.
- [func index(before: Int) -> Int](classificationdistribution/index(before:).md)
  Returns the index immediately before an element index.
### Labeling and mapping
- [func topLabels(Int) -> [Label]](classificationdistribution/toplabels(_:).md)
  Computes the most likely labels in the classification set.
- [func map<T>((Classification<Label>) throws -> Classification<T>) rethrows -> ClassificationDistribution<T>](classificationdistribution/map(_:).md)
  Creates a new classification distribution by applying a transformation to every element.
### Accessing by subscript
- [subscript(Range<Int>) -> Slice<ClassificationDistribution<Label>>](classificationdistribution/subscript(_:)-7uvgm.md)
  Accesses a contiguous range of elements.
- [subscript(Int) -> Classification<Label>](classificationdistribution/subscript(_:)-856r7.md)
  Accesses a classification at an index.
- [subscript(Label) -> Float?](classificationdistribution/subscript(_:)-s5as.md)
  Accesses a probability with label.
### Type Aliases
- [ClassificationDistribution.Element](classificationdistribution/element.md)
  A type representing the sequence’s elements.
- [ClassificationDistribution.Index](classificationdistribution/index.md)
  A type that represents a position in the collection.
- [ClassificationDistribution.Indices](classificationdistribution/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [ClassificationDistribution.Iterator](classificationdistribution/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [ClassificationDistribution.SubSequence](classificationdistribution/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [Collection Implementations](classificationdistribution/collection-implementations.md)
- [Decodable Implementations](classificationdistribution/decodable-implementations.md)
- [Encodable Implementations](classificationdistribution/encodable-implementations.md)
- [Equatable Implementations](classificationdistribution/equatable-implementations.md)
- [Hashable Implementations](classificationdistribution/hashable-implementations.md)
- [Sequence Implementations](classificationdistribution/sequence-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct Classification](classification.md)
  An item in a classification result.
- [struct ClassificationMetrics](classificationmetrics.md)
  Classification metrics.
- [struct MultiLabelClassificationMetrics](multilabelclassificationmetrics.md)
  Multi-label classification metrics.
- [func rootMeanSquaredError<T>([AnnotatedPrediction<T, T>]) -> T](rootmeansquarederror(_:).md)
  Computes the root mean squared error between predicted and ground truth values.
- [func rootMeanSquaredError<T>(some Collection, some Collection) -> T](rootmeansquarederror(_:_:).md)
  Computes the root mean squared error between predicted and ground truth values.
- [func maximumAbsoluteError<T>([AnnotatedPrediction<T, T>]) -> T](maximumabsoluteerror(_:).md)
  Computes the maximum absolute error between predicted and ground truth values.
- [func maximumAbsoluteError<T>(some Collection, some Collection) -> T](maximumabsoluteerror(_:_:).md)
  Computes the maximum absolute error between predicted and ground truth values.
- [func meanAbsoluteError<T>([AnnotatedPrediction<T, T>]) -> T](meanabsoluteerror(_:).md)
  Computes the mean absolute error between predicted and ground truth values.
- [func meanAbsoluteError<T>(some Collection, some Collection) -> T](meanabsoluteerror(_:_:).md)
  Computes the mean absolute error between predicted and ground truth values.
- [func meanAbsolutePercentageError<T>([AnnotatedPrediction<T, T>]) -> T](meanabsolutepercentageerror(_:).md)
  Computes the mean absolute percentage error between predicted and ground truth values.
- [func meanSquaredError<T>([AnnotatedPrediction<T, T>]) -> T](meansquarederror(_:).md)
  Computes the root mean squared error between predicted and ground truth values.
- [func meanSquaredError<T>(some Collection, some Collection) -> T](meansquarederror(_:_:).md)
  Computes the mean squared error between predicted and ground truth values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classificationdistribution)*