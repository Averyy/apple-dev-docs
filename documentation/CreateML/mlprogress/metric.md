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
### Iterating all metric keys
- [static var allCases: [MLProgress.Metric]](mlprogress/metric/allcases-swift.type.property.md)
  A collection of all values of this type.
- [MLProgress.Metric.AllCases](mlprogress/metric/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
### Creating a key from a string
- [init?(rawValue: String)](mlprogress/metric/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Getting a key’s string value
- [var rawValue: String](mlprogress/metric/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [MLProgress.Metric.RawValue](mlprogress/metric/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Encoding and decoding a key
- [func encode(to: any Encoder) throws](mlprogress/metric/encode(to:).md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `String`.
- [init(from: any Decoder) throws](mlprogress/metric/init(from:).md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `String`.
### Providing a key’s hash value
- [func hash(into: inout Hasher)](mlprogress/metric/hash(into:).md)
- [var hashValue: Int](mlprogress/metric/hashvalue.md)
### Comparing metric keys
- [static func != (Self, Self) -> Bool](mlprogress/metric/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Default Implementations
- [Equatable Implementations](mlprogress/metric/equatable-implementations.md)
- [RawRepresentable Implementations](mlprogress/metric/rawrepresentable-implementations.md)

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