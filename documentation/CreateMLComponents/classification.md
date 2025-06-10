# Classification

**Framework**: Create ML Components  
**Kind**: struct

An item in a classification result.

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
struct Classification<Label> where Label : Hashable
```

## Topics

### Creating the item
- [init(label: Label, probability: Float)](classification/init(label:probability:).md)
  Creates a classification with label and probability.
### Getting the properties
- [var label: Label](classification/label.md)
  The classification label.
- [var probability: Float](classification/probability.md)
  The classification probability. A value between 0 and 1.
### Operators
- [static func == (Classification<Label>, Classification<Label>) -> Bool](classification/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](classification/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](classification/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Decodable Implementations](classification/decodable-implementations.md)
- [Encodable Implementations](classification/encodable-implementations.md)
- [Equatable Implementations](classification/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ClassificationDistribution](classificationdistribution.md)
  A classification distribution that contains a probability for each classification label.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classification)*