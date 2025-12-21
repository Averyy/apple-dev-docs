# MLProgress.Metric

**Framework**: Create ML  
**Kind**: enum

Metrics you use to evaluate a model’s performance during a training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum Metric
```

## Topics

### Retrieving metric keys
- [MLProgress.Metric.accuracy](mlprogress/metric/accuracy.md)
  The metric for the model’s accuracy.
- [MLProgress.Metric.contentLoss](mlprogress/metric/contentloss.md)
  The metric for the style transfer model’s content loss.
- [MLProgress.Metric.loss](mlprogress/metric/loss.md)
  The metric for the model’s loss.
- [MLProgress.Metric.maximumError](mlprogress/metric/maximumerror.md)
  The metric for the model’s maximum error.
- [MLProgress.Metric.rootMeanSquaredError](mlprogress/metric/rootmeansquarederror.md)
  The metric for the model’s root mean squared error (RMSE).
- [MLProgress.Metric.styleLoss](mlprogress/metric/styleloss.md)
  The metric for the style transfer model’s style loss.
- [MLProgress.Metric.stylizedImageURL](mlprogress/metric/stylizedimageurl.md)
  The location of the stylized image content in the file system.
- [MLProgress.Metric.validationAccuracy](mlprogress/metric/validationaccuracy.md)
  The metric for the model’s validation accuracy.
- [MLProgress.Metric.validationLoss](mlprogress/metric/validationloss.md)
  The metric for the model’s validation loss.
- [MLProgress.Metric.validationMaximumError](mlprogress/metric/validationmaximumerror.md)
  The metric for the model’s validation maximum error.
- [MLProgress.Metric.validationRootMeanSquaredError](mlprogress/metric/validationrootmeansquarederror.md)
  The metric for the model’s validation root mean squared error (RMSE).

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var metrics: [MLProgress.Metric : Any]](mlcheckpoint/metrics.md)
  Measurements of the model’s performance at the time the session saved the checkpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlprogress/metric)*