# evaluation(on:)

**Framework**: Create ML  
**Kind**: method

Evaluates the classifier on the provided labeled data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func evaluation(on labeledData: MLDataTable) -> MLRegressorMetrics
```

#### Return Value

Metrics that describe the maximum error ([`maximumError`](mlregressormetrics/maximumerror.md)) or the average error ([`rootMeanSquaredError`](mlregressormetrics/rootmeansquarederror.md)).

#### Discussion

Evaluation should be done on a testing data set that the model has not seen as part of the training or validation data sets. The data should have feature columns with identical name and type to the training data, as well as a labels column with the same name.

## Parameters

- `labeledData`: An   to evaluate the trained model on.

## See Also

- [func evaluation(on: DataFrame) -> MLRegressorMetrics](mlrandomforestregressor/evaluation(on:)-237pc.md)
  Evaluates the classifier on the provided labeled data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestregressor/evaluation(on:)-99j4w)*