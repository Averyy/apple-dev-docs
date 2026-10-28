# BGContinuedProcessingTaskRequestResourcesDefault

**Framework**: Background Tasks  
**Kind**: case  
**Role**: Enumeration Case

An option for a task with no additional required system resources.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```c
BGContinuedProcessingTaskRequestResourcesDefault
```

## Discussion

Unless informed otherwise, the scheduler assumes the default resources, allowing background CPU and network access.

## See Also

### Identiying a resource
- [static var gpu: BGContinuedProcessingTaskRequest.Resources](../bgcontinuedprocessingtaskrequest/resources/gpu.md)
  An option that indicates a long-running task requires the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundtasks/bgcontinuedprocessingtaskrequestresources/bgcontinuedprocessingtaskrequestresourcesdefault)*