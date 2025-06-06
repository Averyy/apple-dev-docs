# run(with:inputs:results:executionDescriptor:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func run(with commandQueue: any MTLCommandQueue, inputs inputsArray: [MPSGraphTensorData], results resultsArray: [MPSGraphTensorData]?, executionDescriptor: MPSGraphExecutableExecutionDescriptor?) -> [MPSGraphTensorData]
```

#### Return Value

A valid MPSGraphTensorData array with results synchronized to the CPU memory if MPSGraphOptionsSynchronizeResults set.

#### Discussion

This call is synchronous and will return on completion of execution.

## Parameters

- `commandQueue`: CommandQueue passed to exectute the graph on.
- `inputsArray`: Feeds tensorData for the placeholder tensors, same order as arguments of main function.
- `resultsArray`: Results tensorData for which the caller wishes MPSGraphTensorData to be returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutable/run(with:inputs:results:executiondescriptor:))*