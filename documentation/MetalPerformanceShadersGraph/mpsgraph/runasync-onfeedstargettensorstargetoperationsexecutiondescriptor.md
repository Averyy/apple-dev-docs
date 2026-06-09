# runAsync(on:feeds:targetTensors:targetOperations:executionDescriptor:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func runAsync(on commandQueue: any MTL4CommandQueue, feeds: [MPSGraphTensor : MPSGraphTensorData], targetTensors: [MPSGraphTensor], targetOperations: [MPSGraphOperation]?, executionDescriptor: MPSGraphExecutionDescriptor?) -> [MPSGraphTensor : MPSGraphTensorData]
```

#### Return Value

A valid MPSGraphTensor : MPSGraphTensorData dictionary with results synchronized to the CPU memory if MPSGraphOptionsSynchronizeResults set.

#### Discussion

This call is asynchronous and will return immediately if a completionHandler is set.

## Parameters

- `commandQueue`: MTL4CommandQueue passed to exectute the graph on.
- `feeds`: Feeds dictionary for the placeholder tensors.
- `targetTensors`: Tensors for which the caller wishes MPSGraphTensorData to be returned.
- `targetOperations`: Operations to be completed at the end of the run.
- `executionDescriptor`: ExecutionDescriptor to be passed in and used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/runasync(on:feeds:targettensors:targetoperations:executiondescriptor:))*