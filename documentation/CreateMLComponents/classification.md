# Classification

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

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
- [init(label: Label, probability: Float)](./classification/init%28label,probability%29.md)
  Creates a classification with label and probability.
### Getting the properties
- [var label: Label](./classification/label.md)
  The classification label.
- [var probability: Float](./classification/probability.md)
  The classification probability. A value between 0 and 1.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Metrics
- [struct ClassificationDistribution](./classificationdistribution.md)
  A classification distribution that contains a probability for each classification label.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classification)*