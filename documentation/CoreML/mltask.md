# MLTask

**Framework**: Core ML  
**Kind**: class

An abstract base class for machine learning tasks.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class MLTask
```

#### Overview

You don’t create use this class directly. Instead, use a class that inherits from this one, such as [`MLUpdateTask`](mlupdatetask.md).

## Topics

### Identifying a task
- [var taskIdentifier: String](mltask/taskidentifier.md)
  A unique name of the task to distinguish it from all other tasks at runtime.
### Starting and stopping a task
- [func resume()](mltask/resume.md)
  Begins or resumes a machine learning task.
- [func cancel()](mltask/cancel.md)
  Cancels a machine learning task before it completes.
### Checking the state of a task
- [var state: MLTaskState](mltask/state.md)
  The current state of the machine learning task.
- [enum MLTaskState](mltaskstate.md)
  The state of a machine learning task.
- [var error: (any Error)?](mltask/error.md)
  The underlying error if the task is in a failed state.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MLUpdateTask](mlupdatetask.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Personalizing a Model with On-Device Updates](personalizing-a-model-with-on-device-updates.md)
  Modify an updatable Core ML model by running an update task with labeled data.
- [class MLUpdateTask](mlupdatetask.md)
  A task that updates a model with additional training data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltask)*