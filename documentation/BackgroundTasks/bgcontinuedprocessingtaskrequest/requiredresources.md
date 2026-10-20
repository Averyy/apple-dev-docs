# requiredResources

**Framework**: Background Tasks  
**Kind**: property  
**Role**: Instance Property

An option that indicates any special system resources that the task requires.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var requiredResources: BGContinuedProcessingTaskRequest.Resources { get set }
```

```objc
@property (nonatomic) BGContinuedProcessingTaskRequestResources requiredResources;
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](../performing-long-running-tasks-on-ios-and-ipados.md)

#### Discussion

To request background GPU support for the task, set this property to [`gpu`](./resources/gpu.md). First, check whether the device supports background GPU use; see [`supportedResources`](../bgtaskscheduler/supportedresources.md).

The default value is [`BGContinuedProcessingTaskRequestResourcesDefault`](../bgcontinuedprocessingtaskrequestresources/bgcontinuedprocessingtaskrequestresourcesdefault.md).

## See Also

### Identifying resource dependencies
- [BGContinuedProcessingTaskRequest.Resources](./resources.md)
  Options that specify additional system resources a background task needs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/requiredresources)*