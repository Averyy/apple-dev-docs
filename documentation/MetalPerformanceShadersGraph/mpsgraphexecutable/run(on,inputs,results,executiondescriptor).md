# run(on:inputs:results:executionDescriptor:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func run(on commandQueue: any MTL4CommandQueue, inputs inputsArray: [MPSGraphTensorData], results resultsArray: [MPSGraphTensorData]?, executionDescriptor: MPSGraphExecutableExecutionDescriptor?) -> [MPSGraphTensorData]
```

#### Return Value

A valid MPSGraphTensorData array with results synchronized to the CPU memory if MPSGraphOptionsSynchronizeResults set.

#### Discussion

This call is synchronous and will return on completion of execution.

## Parameters

- `commandQueue`: MTL4CommandQueue passed to exectute the graph on.
- `inputsArray`: Feeds tensorData for the placeholder tensors, same order as arguments of main function.
- `resultsArray`: Results tensorData for which the caller wishes MPSGraphTensorData to be returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutable/run(on:inputs:results:executiondescriptor:))*