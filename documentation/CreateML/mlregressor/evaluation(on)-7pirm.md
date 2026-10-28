# evaluation(on:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Evaluates the classifier on the provided labeled data.

**Availability**:
- macOS 10.14+ - Deprecated in 13.0

> **Deprecated**: Use DataFrame instead of MLDataTable.

## Declaration

```swift
func evaluation(on labeledData: MLDataTable) -> MLRegressorMetrics
```

**Other overloads**:

```swift
func evaluation(on labeledData: DataFrame) -> MLRegressorMetrics
```

## Return Value

Metrics that describe the maximum error ([`maximumError`](../mlregressormetrics/maximumerror.md)) or the average error ([`rootMeanSquaredError`](../mlregressormetrics/rootmeansquarederror.md)).

## Discussion

Evaluation should be done on a testing data set that the model has not seen as part of the training or validation data sets. The data should have feature columns with identical name and type to the training data, as well as a labels column with the same name.

## Parameters

- `labeledData`: An `MLDataTable` to evaluate the trained model on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlregressor/evaluation(on:)-7pirm)*