# MLProgress.Metric

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

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
- [MLProgress.Metric.accuracy](./metric/accuracy.md)
  The metric for the model’s accuracy.
- [MLProgress.Metric.contentLoss](./metric/contentloss.md)
  The metric for the style transfer model’s content loss.
- [MLProgress.Metric.loss](./metric/loss.md)
  The metric for the model’s loss.
- [MLProgress.Metric.maximumError](./metric/maximumerror.md)
  The metric for the model’s maximum error.
- [MLProgress.Metric.rootMeanSquaredError](./metric/rootmeansquarederror.md)
  The metric for the model’s root mean squared error (RMSE).
- [MLProgress.Metric.styleLoss](./metric/styleloss.md)
  The metric for the style transfer model’s style loss.
- [MLProgress.Metric.stylizedImageURL](./metric/stylizedimageurl.md)
  The location of the stylized image content in the file system.
- [MLProgress.Metric.validationAccuracy](./metric/validationaccuracy.md)
  The metric for the model’s validation accuracy.
- [MLProgress.Metric.validationLoss](./metric/validationloss.md)
  The metric for the model’s validation loss.
- [MLProgress.Metric.validationMaximumError](./metric/validationmaximumerror.md)
  The metric for the model’s validation maximum error.
- [MLProgress.Metric.validationRootMeanSquaredError](./metric/validationrootmeansquarederror.md)
  The metric for the model’s validation root mean squared error (RMSE).

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Copyable](../../Swift/copyable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Assessing a checkpoint
- [var metrics: [MLProgress.Metric : Any]](../mlcheckpoint/metrics.md)
  Measurements of the model’s performance at the time the session saved the checkpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlprogress/metric)*