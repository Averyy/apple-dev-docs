# maximumAbsoluteError(_:_:)

**Framework**: Create ML Components  
**Kind**: func  
**Role**: Function

Computes the maximum absolute error between predicted and ground truth values.

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
@backDeployed(before: macOS 14.0, iOS 17.0, tvOS 17.0)
func maximumAbsoluteError<T>(_ predicted: some Collection, _ groundTruth: some Collection) -> T where T : FloatingPoint
```

## Return Value

The maximum absolute error.

## Discussion

Empty collections of predicted and ground truth values will return a value of NaN.

## Parameters

- `predicted`: The predicted values.
- `groundTruth`: The ground truth values. The collection must have same number of elements as the predicted values.

## See Also

### Metrics
- [struct Classification](./classification.md)
  An item in a classification result.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/maximumabsoluteerror(_:_:))*