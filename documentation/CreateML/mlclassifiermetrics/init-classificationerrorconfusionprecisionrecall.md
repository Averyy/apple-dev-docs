# init(classificationError:confusion:precisionRecall:)

**Framework**: Create ML  
**Kind**: init

Creates empty classifier metrics.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(classificationError: Double, confusion: MLDataTable, precisionRecall: MLDataTable)
```

#### Discussion

You typically don’t initialize metrics directly. Instead you get metrics about your model after training. For example, when you train an [`MLClassifier`](mlclassifier.md), you can look at its [`trainingMetrics`](mlclassifier/trainingmetrics.md) and [`validationMetrics`](mlclassifier/validationmetrics.md) properties. Additionally, you can check the performance on a test set with the [`evaluation(on:)`](mlclassifier/evaluation(on:)-6433y.md) method.

> ⚠️ **Warning**: This initializer should not be used, it creates an empty instance.

## Parameters

- `classificationError`: The fraction of incorrectly labeled examples.
- `confusion`: A confusion matrix describing the classifications for each category.
- `precisionRecall`: A two-dimensional table describing the precision and recall for each category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlclassifiermetrics/init(classificationerror:confusion:precisionrecall:))*