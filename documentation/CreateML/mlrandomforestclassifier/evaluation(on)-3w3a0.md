# evaluation(on:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Evaluates the classifier on the provided labeled data.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 13.0
- visionOS 1.0+

> **Deprecated**: Use DataFrame instead of MLDataTable.

## Declaration

```swift
func evaluation(on labeledData: MLDataTable) -> MLClassifierMetrics
```

**Other overloads**:

```swift
func evaluation(on labeledData: DataFrame) -> MLClassifierMetrics
```

## Return Value

Metrics that describe the classification errors ([`classificationError`](../mlclassifiermetrics/classificationerror.md)), the precision and recall percentages ([`precisionRecall`](../mlclassifiermetrics/precisionrecall.md)), and a table that describes how labels were misapplied ([`confusion`](../mlclassifiermetrics/confusion.md)) on the provided data.

## Discussion

Evaluation should be done on a testing data set that the model has not seen as part of the training or validation data sets. The data should have feature columns with identical name and type to the training data, as well as a labels column with the same name.

## Parameters

- `labeledData`: An `MLDataTable` to evaluate the trained model on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestclassifier/evaluation(on:)-3w3a0)*