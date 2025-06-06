# encode(to:feeds:targetTensors:targetOperations:executionDescriptor:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Encodes the graph for the given feeds to returns the target tensor values, ensuring all target operations also executed.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func encode(to commandBuffer: MPSCommandBuffer, feeds: [MPSGraphTensor : MPSGraphTensorData], targetTensors: [MPSGraphTensor], targetOperations: [MPSGraphOperation]?, executionDescriptor: MPSGraphExecutionDescriptor?) -> [MPSGraphTensor : MPSGraphTensorData]
```

#### Return Value

A valid MPSGraphTensor : MPSGraphTensorData dictionary with results synchronized to the CPU memory if MPSGraphOptionsSynchronizeResults set.

#### Discussion

This call is asynchronous and will return immediately if a completionHandler is set.

## Parameters

- `commandBuffer`: commandBuffer passed to exectute the graph on, it is an MPSCommandBuffer, commitAndContinue might be called, please don’t rely on underlying MTLCommandBuffer to remain uncommitted.
- `feeds`: Feeds dictionary for the placeholder tensors.
- `targetTensors`: Tensors for which the caller wishes MPSGraphTensorData to be returned.
- `targetOperations`: Operations to be completed at the end of the run.
- `executionDescriptor`: ExecutionDescriptor to be passed in and used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/encode(to:feeds:targettensors:targetoperations:executiondescriptor:))*