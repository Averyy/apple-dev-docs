# evaluation(on:)

**Framework**: Create ML  
**Kind**: method

Evaluates the classifier on the provided labeled data.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func evaluation(on labeledData: DataFrame) -> MLRegressorMetrics
```

#### Return Value

Metrics that describe the maximum error ([`maximumError`](mlregressormetrics/maximumerror.md)) or the average error ([`rootMeanSquaredError`](mlregressormetrics/rootmeansquarederror.md)).

#### Discussion

Evaluation should be done on a testing data set that the model has not seen as part of the training or validation data sets. The data should have feature columns with identical name and type to the training data, as well as a labels column with the same name.

## Parameters

- `labeledData`: A   to evaluate the trained model on.

## See Also

- [var trainingMetrics: MLRegressorMetrics](mlregressor/trainingmetrics.md)
  Measurements of the regressor’s performance on the training data set.
- [var validationMetrics: MLRegressorMetrics](mlregressor/validationmetrics.md)
  Measurements of the regressor’s performance on the validation data set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlregressor/evaluation(on:))*