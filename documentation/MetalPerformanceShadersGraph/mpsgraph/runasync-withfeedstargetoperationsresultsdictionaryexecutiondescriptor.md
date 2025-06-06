# runAsync(with:feeds:targetOperations:resultsDictionary:executionDescriptor:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Encodes the graph for the given feeds to returns the target tensor values in the results dictionary provided by the user.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func runAsync(with commandQueue: any MTLCommandQueue, feeds: [MPSGraphTensor : MPSGraphTensorData], targetOperations: [MPSGraphOperation]?, resultsDictionary: [MPSGraphTensor : MPSGraphTensorData], executionDescriptor: MPSGraphExecutionDescriptor?)
```

#### Discussion

It ensures all target operations also executed. This call is asynchronous and will return immediately if a completionHandler is set.

## Parameters

- `commandQueue`: CommandQueue passed to exectute the graph on.
- `feeds`: Feeds dictionary for the placeholder tensors.
- `targetOperations`: Operations to be completed at the end of the run.
- `resultsDictionary`: MPSGraphTensors dictionary passed by user, these will be filled with graph output data.
- `executionDescriptor`: ExecutionDescriptor to be passed in and used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/runasync(with:feeds:targetoperations:resultsdictionary:executiondescriptor:))*