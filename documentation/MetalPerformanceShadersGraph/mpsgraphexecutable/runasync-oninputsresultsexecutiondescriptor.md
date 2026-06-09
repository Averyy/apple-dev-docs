# runAsync(on:inputs:results:executionDescriptor:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed. This call is asynchronous and will return immediately.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func runAsync(on commandQueue: any MTL4CommandQueue, inputs inputsArray: [MPSGraphTensorData], results resultsArray: [MPSGraphTensorData]?, executionDescriptor: MPSGraphExecutableExecutionDescriptor?) -> [MPSGraphTensorData]
```

#### Return Value

A valid MPSGraphTensorData array with results synchronized to the CPU memory if MPSGraphOptionsSynchronizeResults set.

## Parameters

- `commandQueue`: MTL4CommandQueue passed to exectute the graph on.
- `inputsArray`: Feeds tensorData for the placeholder tensors, same order as arguments of main function.
- `resultsArray`: Tensors for which the caller wishes MPSGraphTensorData to be returned.
- `executionDescriptor`: ExecutionDescriptor to be passed in and used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutable/runasync(on:inputs:results:executiondescriptor:))*