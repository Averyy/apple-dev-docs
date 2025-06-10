# requiredResources

**Framework**: Background Tasks  
**Kind**: property

An option that indicates any special system resources that the task requires.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
var requiredResources: BGContinuedProcessingTaskRequest.Resources { get set }
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](performing-long-running-tasks-on-ios-and-ipados.md)

#### Discussion

To request background GPU support for the task, set this property to [`gpu`](bgcontinuedprocessingtaskrequest/resources/gpu.md). First, check whether the device supports background GPU use; see [`supportedResources`](bgtaskscheduler/supportedresources.md).

The default value is [`BGContinuedProcessingTaskRequestResourcesDefault`](bgcontinuedprocessingtaskrequestresources/bgcontinuedprocessingtaskrequestresourcesdefault.md).

## See Also

- [BGContinuedProcessingTaskRequest.Resources](bgcontinuedprocessingtaskrequest/resources.md)
  Options that specify additional system resources a background task needs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/requiredresources)*