# MLTrainingSessionParameters

**Framework**: Create ML  
**Kind**: struct

The configuration settings for a training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLTrainingSessionParameters
```

## Topics

### Creating a session’s parameters
- [init(sessionDirectory: URL?, reportInterval: Int, checkpointInterval: Int, iterations: Int)](mltrainingsessionparameters/init(sessiondirectory:reportinterval:checkpointinterval:iterations:).md)
  Creates a set of parameters for a training session.
### Configuring the session’s parameters
- [let sessionDirectory: URL?](mltrainingsessionparameters/sessiondirectory.md)
  The location in the file system where the session stores its progress.
- [var reportInterval: Int](mltrainingsessionparameters/reportinterval.md)
  The number of iterations the session completes before it reports its progress.
- [var checkpointInterval: Int](mltrainingsessionparameters/checkpointinterval.md)
  The number of iterations the session completes before it saves a checkpoint.
- [var iterations: Int](mltrainingsessionparameters/iterations.md)
  The maximum number of iterations for the training session.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MLJob](mljob.md)
  The representation of a model’s asynchronous training session you use to monitor the session’s progress or terminate its execution.
- [class MLTrainingSession](mltrainingsession.md)
  The current state of a model’s asynchronous training session.
- [struct MLCheckpoint](mlcheckpoint.md)
  The state of a model’s asynchronous training session at a specific point in time during the feature extraction or training phase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltrainingsessionparameters)*