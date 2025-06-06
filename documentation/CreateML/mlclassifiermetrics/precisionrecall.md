# precisionRecall

**Framework**: Create ML  
**Kind**: property

A data table listing the precision and recall percentages for each class.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var precisionRecall: MLDataTable { get }
```

## Mentions

- [Improving Your Model’s Accuracy](improving-your-model-s-accuracy.md)

#### Discussion

Precision and recall are metrics calculated for each class. Together they describe the tradeoff between misapplying a label too liberally and missing examples of that label.

Precision describes how effective the model was at applying a label only when appropriate for a given category (few false positives).

Recall describes how effective the model was at finding all the relevant examples of a category (few false negatives).

![None](https://docs-assets.developer.apple.com/published/7855eb855befe83b05e51d97fbcc6a95/MLClassifierMetrics-precisionRecall-1%402x.png)

The figure below shows how each example contributes to the precision and recall percentages for the category “Elephant”.

![A table of actual and predicted labels for the Elephant category.](https://docs-assets.developer.apple.com/published/d2e3bf7a61ae75d3205a71b3d78cee9d/MLClassifierMetrics-precisionRecall-2%402x.png)

“Elephant” appears as the true or correct label only once, but it’s predicted twice. This second prediction is an error in precision. Precision and recall can give you a much better idea of how your model is making mistakes than [`classificationError`](mlclassifiermetrics/classificationerror.md).

To determine what other categories “Elephant” examples may have been labeled with, see the [`confusion`](mlclassifiermetrics/confusion.md) property.

## See Also

- [var classificationError: Double](mlclassifiermetrics/classificationerror.md)
  The fraction of incorrectly labeled examples.
- [var confusion: MLDataTable](mlclassifiermetrics/confusion.md)
  A table comparing the actual and predicted labels for each classification category.
- [var confusionDataFrame: DataFrame](mlclassifiermetrics/confusiondataframe.md)
  A data frame comparing the actual and predicted labels for each class.
- [var precisionRecallDataFrame: DataFrame](mlclassifiermetrics/precisionrecalldataframe.md)
  A data frame listing the precision and recall percentages for each class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlclassifiermetrics/precisionrecall)*