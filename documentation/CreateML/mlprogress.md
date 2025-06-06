# MLProgress

**Framework**: Create ML  
**Kind**: struct

A convenience type that exposes information about the progress of a training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLProgress
```

#### Overview

Create ML uses this type to exposes specific values within a  instance as properties.

## Topics

### Creating a training progress update
- [init(phase: MLPhase)](mlprogress/init(phase:).md)
  Creates a training session progress instance from a training phase.
- [init?(progress: Progress)](mlprogress/init(progress:).md)
  Creates a training session progress instance from a foundation progress object.
### Inspecting a session’s progress
- [var elapsedTime: TimeInterval](mlprogress/elapsedtime.md)
  The time, in seconds, since the training session started.
- [var phase: MLPhase](mlprogress/phase.md)
  The current phase of the training session.
- [var itemCount: Int](mlprogress/itemcount.md)
  The current number of files processed during a feature extraction phase, or the completed iterations during a training phase.
- [var totalItemCount: Int?](mlprogress/totalitemcount.md)
  The total number of files during a feature extraction phase, or total iterations during a training phase.
- [var metrics: [MLProgress.Metric : Any]](mlprogress/metrics.md)
  Measurements of the model’s performance during the training or evaluation phases of a training session.
- [MLProgress.Metric](mlprogress/metric.md)
  Metrics you use to evaluate a model’s performance during a training session.
### Accessing general information
- [static let elapsedTimeKey: ProgressUserInfoKey](mlprogress/elapsedtimekey.md)
  The key that accesses the elapsed time value.
- [static let phaseKey: ProgressUserInfoKey](mlprogress/phasekey.md)
  The key that accesses the current phase value.
- [static let itemCountKey: ProgressUserInfoKey](mlprogress/itemcountkey.md)
  The key that accesses the current item count value.
- [static let totalItemCountKey: ProgressUserInfoKey](mlprogress/totalitemcountkey.md)
  The key that accesses the total item count value.
### Accessing assessment metrics
- [static let accuracyKey: ProgressUserInfoKey](mlprogress/accuracykey.md)
  The key that accesses the training accuracy value.
- [static let lossKey: ProgressUserInfoKey](mlprogress/losskey.md)
  The key that accesses the training loss value.
- [static let validationAccuracyKey: ProgressUserInfoKey](mlprogress/validationaccuracykey.md)
  The key that accesses the validation accuracy value.
- [static let validationLossKey: ProgressUserInfoKey](mlprogress/validationlosskey.md)
  The key that accesses the validation loss value.
### Accessing style transfer metrics
- [static let contentLossKey: ProgressUserInfoKey](mlprogress/contentlosskey.md)
  The key that accesses the content image loss value.
- [static let styleLossKey: ProgressUserInfoKey](mlprogress/stylelosskey.md)
  The key that accesses the style image loss value.
- [static let stylizedImageKey: ProgressUserInfoKey](mlprogress/stylizedimagekey.md)
  The key that accesses the stylized image value.
### Accessing error information
- [static let maximumErrorKey: ProgressUserInfoKey](mlprogress/maximumerrorkey.md)
  They key that accesses the maximum error value.
- [static let rootMeanSquaredErrorKey: ProgressUserInfoKey](mlprogress/rootmeansquarederrorkey.md)
  They key that accesses the root-mean-squared error value.
- [static let validationMaximumErrorKey: ProgressUserInfoKey](mlprogress/validationmaximumerrorkey.md)
  They key that accesses the validation maximum error value.
- [static let validationRootMeanSquaredErrorKey: ProgressUserInfoKey](mlprogress/validationrootmeansquarederrorkey.md)
  They key that accesses the validation root-mean-squared error value.
### Encoding and decoding a session’s progress
- [func encode(to: any Encoder) throws](mlprogress/encode(to:).md)
  Encodes the progress value into the given encoder.
- [init(from: any Decoder) throws](mlprogress/init(from:).md)
  Creates a progress instance by decoding from the given decoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)

## See Also

- [let startDate: Date](mljob/startdate.md)
  The date and time when the training session began.
- [let progress: Progress](mljob/progress.md)
  The training session’s current progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlprogress)*