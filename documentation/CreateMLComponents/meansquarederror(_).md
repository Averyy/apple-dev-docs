# meanSquaredError(_:)

**Framework**: Create ML Components  
**Kind**: func  
**Role**: Function

Computes the root mean squared error between predicted and ground truth values.

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
@backDeployed(before: macOS 15.0, iOS 18.0, tvOS 18.0, visionOS 2.0)
func meanSquaredError<T>(_ annotatedPredictions: [AnnotatedPrediction<T, T>]) -> T where T : FloatingPoint
```

#### Return Value

The root mean squared error.

#### Discussion

If an empty `AnnotatedPrediction` is supplied, the result will be NaN.

## Parameters

- `annotatedPredictions`: An `AnnotatedPrediction` object.

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
- [func maximumAbsoluteError<T>(some Collection, some Collection) -> T](./maximumabsoluteerror%28_,_%29.md)
  Computes the maximum absolute error between predicted and ground truth values.
- [func meanAbsoluteError<T>([AnnotatedPrediction<T, T>]) -> T](./meanabsoluteerror%28_%29.md)
  Computes the mean absolute error between predicted and ground truth values.
- [func meanAbsoluteError<T>(some Collection, some Collection) -> T](./meanabsoluteerror%28_,_%29.md)
  Computes the mean absolute error between predicted and ground truth values.
- [func meanAbsolutePercentageError<T>([AnnotatedPrediction<T, T>]) -> T](./meanabsolutepercentageerror%28_%29.md)
  Computes the mean absolute percentage error between predicted and ground truth values.
- [func meanSquaredError<T>(some Collection, some Collection) -> T](./meansquarederror%28_,_%29.md)
  Computes the mean squared error between predicted and ground truth values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/meansquarederror(_:))*