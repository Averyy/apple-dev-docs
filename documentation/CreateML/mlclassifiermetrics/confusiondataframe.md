# confusionDataFrame

**Framework**: Create ML  
**Kind**: property

A data frame comparing the actual and predicted labels for each class.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var confusionDataFrame: DataFrame { get }
```

#### Discussion

The confusion data frame describes how examples were mislabeled between categories. Each row contains the true label, the predicted label, and the number of instances of that combination. For example, the table below lists that “business” was labeled correctly with “business” 113 times, while “business” was confused with “entertainment” 2 times.

![A table showing the format of the confusion matrix containing rows for the true label the label predicted by](https://docs-assets.developer.apple.com/published/c9b7730d227217804dd88adf475e1069/MLClassifierMetrics-confusion-1%402x.png)

## See Also

- [var classificationError: Double](mlclassifiermetrics/classificationerror.md)
  The fraction of incorrectly labeled examples.
- [var precisionRecall: MLDataTable](mlclassifiermetrics/precisionrecall.md)
  A data table listing the precision and recall percentages for each class.
- [var confusion: MLDataTable](mlclassifiermetrics/confusion.md)
  A table comparing the actual and predicted labels for each classification category.
- [var precisionRecallDataFrame: DataFrame](mlclassifiermetrics/precisionrecalldataframe.md)
  A data frame listing the precision and recall percentages for each class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlclassifiermetrics/confusiondataframe)*