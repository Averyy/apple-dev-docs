# BGContinuedProcessingTask

**Framework**: Background Tasks  
**Kind**: class

A task that starts in the foreground and can continue running in the background as needed.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class BGContinuedProcessingTask
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](performing-long-running-tasks-on-ios-and-ipados.md)

#### Overview

This task works with [`BGContinuedProcessingTaskRequest`](bgcontinuedprocessingtaskrequest.md).

The system displays the progress of this task in a Live Activity and a person can cancel it through the interface if they wish.

The system can terminate a continuous background task abruptly depending on run-time conditions, for example, under resource constraints. Your implementation needs to report progress using the [`ProgressReporting`](https://developer.apple.com/documentation/Foundation/ProgressReporting) protocol that this task conforms to. The system prioritizes the termination of tasks that reflect minimal or no progress, when resources become constrained.

For more information on Continuous Background Task requests, see [`Performing long-running tasks on iOS and iPadOS`](performing-long-running-tasks-on-ios-and-ipados.md).

## Topics

### Titling the task
- [var title: String](bgcontinuedprocessingtask/title.md)
  The localized title displayed to a person.
- [var subtitle: String](bgcontinuedprocessingtask/subtitle.md)
  The localized subtitle displayed to a person.
- [func updateTitle(String, subtitle: String)](bgcontinuedprocessingtask/updatetitle(_:subtitle:).md)
  Update the task title and subtitle that the system displays to a person.

## Relationships

### Inherits From
- [BGTask](bgtask.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [ProgressReporting](../Foundation/ProgressReporting.md)

## See Also

- [Performing long-running tasks on iOS and iPadOS](performing-long-running-tasks-on-ios-and-ipados.md)
  Use a continuous background task to do work that can complete as needed.
- [Background GPU Access](../BundleResources/Entitlements/com.apple.developer.background-tasks.continued-processing.gpu.md)
  The entitlement the system requires for a continuous background task to use the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtask)*