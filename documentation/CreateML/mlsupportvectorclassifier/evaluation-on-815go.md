# evaluation(on:)

**Framework**: Create ML  
**Kind**: method

Evaluates the classifier on the provided labeled data.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func evaluation(on labeledData: MLDataTable) -> MLClassifierMetrics
```

#### Return Value

Metrics that describe the classification errors ([`classificationError`](mlclassifiermetrics/classificationerror.md)), the precision and recall percentages ([`precisionRecall`](mlclassifiermetrics/precisionrecall.md)), and a table that describes how labels were misapplied ([`confusion`](mlclassifiermetrics/confusion.md)) on the provided data.

#### Discussion

Evaluation should be done on a testing data set that the model has not seen as part of the training or validation data sets. The data should have feature columns with identical name and type to the training data, as well as a labels column with the same name.

## Parameters

- `labeledData`: An   to evaluate the trained model on.

## See Also

- [func evaluation(on: DataFrame) -> MLClassifierMetrics](mlsupportvectorclassifier/evaluation(on:)-3fvw.md)
  Evaluates the classifier on the provided labeled data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/evaluation(on:)-815go)*