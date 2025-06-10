# BGContinuedProcessingTaskRequest.Resources

**Framework**: Background Tasks  
**Kind**: struct

Options that specify additional system resources a background task needs.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
struct Resources
```

#### Overview

The following properties are of this type:

- Continuous Background Task request ([`BGContinuedProcessingTaskRequest`](bgcontinuedprocessingtaskrequest.md)) property [`requiredResources`](bgcontinuedprocessingtaskrequest/requiredresources.md).
- [`BGTaskScheduler`](bgtaskscheduler.md) property [`supportedResources`](bgtaskscheduler/supportedresources.md).

## Topics

### Identiying a resource
- [static var gpu: BGContinuedProcessingTaskRequest.Resources](bgcontinuedprocessingtaskrequest/resources/gpu.md)
  An option that indicates a long-running task requires the GPU.
### Creating a resource
- [init(rawValue: Int)](bgcontinuedprocessingtaskrequest/resources/init(rawvalue:).md)
  Initializes a required resource for a Continuous Background Task by raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var requiredResources: BGContinuedProcessingTaskRequest.Resources](bgcontinuedprocessingtaskrequest/requiredresources.md)
  An option that indicates any special system resources that the task requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/resources)*