# MLCheckpoint

**Framework**: Create ML  
**Kind**: struct

The state of a model’s asynchronous training session at a specific point in time during the feature extraction or training phase.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLCheckpoint
```

## Topics

### Inspecting a checkpoint
- [var phase: MLPhase](mlcheckpoint/phase.md)
  The training session’s phase when it created the checkpoint.
- [var iteration: Int](mlcheckpoint/iteration.md)
  The iteration number of a training session’s phase when it created the checkpoint.
- [var date: Date](mlcheckpoint/date.md)
  The time when the training session created the checkpoint.
- [var url: URL](mlcheckpoint/url.md)
  The location of the checkpoint in the file system.
### Assessing a checkpoint
- [var metrics: [MLProgress.Metric : Any]](mlcheckpoint/metrics.md)
  Measurements of the model’s performance at the time the session saved the checkpoint.
- [MLProgress.Metric](mlprogress/metric.md)
  Metrics you use to evaluate a model’s performance during a training session.
### Encoding and decoding a checkpoint
- [func encode(to: any Encoder) throws](mlcheckpoint/encode(to:).md)
  Encodes the checkpoint into the encoder.
- [init(from: any Decoder) throws](mlcheckpoint/init(from:).md)
  Creates a new checkpoint by decoding from the decoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MLJob](mljob.md)
  The representation of a model’s asynchronous training session you use to monitor the session’s progress or terminate its execution.
- [class MLTrainingSession](mltrainingsession.md)
  The current state of a model’s asynchronous training session.
- [struct MLTrainingSessionParameters](mltrainingsessionparameters.md)
  The configuration settings for a training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlcheckpoint)*