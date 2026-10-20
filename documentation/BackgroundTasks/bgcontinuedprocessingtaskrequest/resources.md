# BGContinuedProcessingTaskRequest.Resources

**Framework**: Background Tasks  
**Kind**: struct  
**Role**: Structure

Options that specify additional system resources a background task needs.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct Resources
```

```c
enum BGContinuedProcessingTaskRequestResources : NSInteger;
```

#### Overview

The following properties are of this type:

- Continuous Background Task request ([`BGContinuedProcessingTaskRequest`](../bgcontinuedprocessingtaskrequest.md)) property [`requiredResources`](./requiredresources.md).
- [`BGTaskScheduler`](../bgtaskscheduler.md) property [`supportedResources`](../bgtaskscheduler/supportedresources.md).

## Topics

### Identiying a resource
- [static var gpu: BGContinuedProcessingTaskRequest.Resources](./resources/gpu.md)
  An option that indicates a long-running task requires the GPU.
### Creating a resource
- [init(rawValue: Int)](./resources/init%28rawvalue%29.md)
  Initializes a required resource for a Continuous Background Task by raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Identifying resource dependencies
- [var requiredResources: BGContinuedProcessingTaskRequest.Resources](./requiredresources.md)
  An option that indicates any special system resources that the task requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequest/resources)*