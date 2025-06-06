# encode(to:inputs:results:executionDescriptor:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed. This call is asynchronous and will return immediately after finishing encoding.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func encode(to commandBuffer: MPSCommandBuffer, inputs inputsArray: [MPSGraphTensorData], results resultsArray: [MPSGraphTensorData]?, executionDescriptor: MPSGraphExecutableExecutionDescriptor?) -> [MPSGraphTensorData]
```

#### Return Value

A valid MPSGraphTensorData array with results synchronized to the CPU memory if MPSGraphOptionsSynchronizeResults set.

## Parameters

- `commandBuffer`: CommandBuffer passed to exectute the graph on, commitAndContinue might be called, please don’t rely on underlying MTLCommandBuffer to remain uncommitted
- `inputsArray`: Feeds tensorData for the placeholder tensors, same order as arguments of main function
- `resultsArray`: Tensors for which the caller wishes MPSGraphTensorData to be returned
- `executionDescriptor`: ExecutionDescriptor to be passed in and used,


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutable/encode(to:inputs:results:executiondescriptor:))*