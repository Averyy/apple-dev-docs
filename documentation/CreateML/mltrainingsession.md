# MLTrainingSession

**Framework**: Create ML  
**Kind**: class  
**Role**: Class

The current state of a model’s asynchronous training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
final class MLTrainingSession<Task>
```

## Topics

### Checking a training session’s progress
- [var phase: MLPhase](./mltrainingsession/phase.md)
  The training session’s current state.
- [enum MLPhase](./mlphase.md)
  The possible states of a training session.
- [var iteration: Int](./mltrainingsession/iteration.md)
  The iteration number of a training session’s phase.
- [var checkpoints: [MLCheckpoint]](./mltrainingsession/checkpoints.md)
  An array of checkpoints the training session has created so far.
### Removing checkpoints
- [func removeCheckpoints((MLCheckpoint) -> Bool) throws](./mltrainingsession/removecheckpoints%28_%29.md)
  Removes the checkpoints that satisfy your closure from the training session.
### Reusing features from a previous session
- [func reuseExtractedFeatures(from: MLTrainingSession<Task>) throws](./mltrainingsession/reuseextractedfeatures%28from%29.md)
  Uses the features another session has already extracted from its dataset.
### Inspecting a session
- [var date: Date](./mltrainingsession/date.md)
  The time when you created this training session.
- [let parameters: MLTrainingSessionParameters](./mltrainingsession/parameters.md)
  The parameters you used to create the training session.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Model training Control
- [class MLJob](./mljob.md)
  The representation of a model’s asynchronous training session you use to monitor the session’s progress or terminate its execution.
- [struct MLTrainingSessionParameters](./mltrainingsessionparameters.md)
  The configuration settings for a training session.
- [struct MLCheckpoint](./mlcheckpoint.md)
  The state of a model’s asynchronous training session at a specific point in time during the feature extraction or training phase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltrainingsession)*