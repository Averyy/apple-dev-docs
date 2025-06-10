# supportedResources

**Framework**: Background Tasks  
**Kind**: property

Additional system resources that a continuous background task can request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
class var supportedResources: BGContinuedProcessingTaskRequest.Resources { get }
```

## Mentions

- [Performing long-running tasks on iOS and iPadOS](performing-long-running-tasks-on-ios-and-ipados.md)

#### Discussion

The [`BGContinuedProcessingTaskRequest.Resources`](bgcontinuedprocessingtaskrequest/resources.md) enumeration indicates optional system resources that a specific [`BGContinuedProcessingTaskRequest`](bgcontinuedprocessingtaskrequest.md) instance can request through its [`requiredResources`](bgcontinuedprocessingtaskrequest/requiredresources.md) property.

Before requesting a resource, check this property to ensure that the device supports it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler/supportedresources)*