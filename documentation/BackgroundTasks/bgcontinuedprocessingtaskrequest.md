# BGContinuedProcessingTaskRequest

**Framework**: Background Tasks  
**Kind**: class

A request for a workload that the system continues processing even if a person backgrounds the app.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
class BGContinuedProcessingTaskRequest
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](performing-long-running-tasks-on-ios-and-ipados.md)

#### Overview

The app submits this request from the foreground. Submission needs to occur as a result of a person’s action, such as tapping a button. The framework begins processing the task immediately, if possible, and the system allows it to continue running even if the app moves to the background.

For more information on Continuous Background Task requests, see [`Performing long-running tasks on iOS and iPadOS`](performing-long-running-tasks-on-ios-and-ipados.md).

## Topics

### Creating a task request
- [init(identifier: String, title: String, subtitle: String)](bgcontinuedprocessingtaskrequest/init(identifier:title:subtitle:).md)
  Creates an instance on behalf of the currently foregrounded app.
### Identifying resource dependencies
- [var requiredResources: BGContinuedProcessingTaskRequest.Resources](bgcontinuedprocessingtaskrequest/requiredresources.md)
  An option that indicates any special system resources that the task requires.
- [BGContinuedProcessingTaskRequest.Resources](bgcontinuedprocessingtaskrequest/resources.md)
  Options that specify additional system resources a background task needs.
### Choosing a processing strategy
- [var strategy: BGContinuedProcessingTaskRequest.SubmissionStrategy](bgcontinuedprocessingtaskrequest/strategy.md)
  The submission strategy for the scheduler to abide by.
- [BGContinuedProcessingTaskRequest.SubmissionStrategy](bgcontinuedprocessingtaskrequest/submissionstrategy.md)
  The ways your app suggests the system handle your task’s submission under varying conditions.
### Titling the task
- [var subtitle: String](bgcontinuedprocessingtaskrequest/subtitle.md)
  The localized subtitle displayed to a person.
- [var title: String](bgcontinuedprocessingtaskrequest/title.md)
  The localized task title displayed to a person.

## Relationships

### Inherits From
- [BGTaskRequest](bgtaskrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class BGProcessingTaskRequest](bgprocessingtaskrequest.md)
  A request to launch your app in the background to execute a processing task that can take minutes to complete.
- [class BGAppRefreshTaskRequest](bgapprefreshtaskrequest.md)
  A request to launch your app in the background to execute a short refresh task.
- [class BGTaskRequest](bgtaskrequest.md)
  An abstract class for representing task requests.
- [class BGHealthResearchTaskRequest](bghealthresearchtaskrequest.md)
  A request to launch your app in the background to execute processing for a health research study in which a user participates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest)*