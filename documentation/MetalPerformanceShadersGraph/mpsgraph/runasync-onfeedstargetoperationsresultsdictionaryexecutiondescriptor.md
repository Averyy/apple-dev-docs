# runAsync(on:feeds:targetOperations:resultsDictionary:executionDescriptor:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Encodes the graph for the given feeds to returns the target tensor values in the results dictionary provided by the user.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func runAsync(on commandQueue: any MTL4CommandQueue, feeds: [MPSGraphTensor : MPSGraphTensorData], targetOperations: [MPSGraphOperation]?, resultsDictionary: [MPSGraphTensor : MPSGraphTensorData], executionDescriptor: MPSGraphExecutionDescriptor?)
```

#### Discussion

It ensures all target operations also executed. This call is asynchronous and will return immediately if a completionHandler is set.

## Parameters

- `commandQueue`: MTL4CommandQueue passed to exectute the graph on.
- `feeds`: Feeds dictionary for the placeholder tensors.
- `targetOperations`: Operations to be completed at the end of the run.
- `resultsDictionary`: MPSGraphTensors dictionary passed by user, these will be filled with graph output data.
- `executionDescriptor`: ExecutionDescriptor to be passed in and used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/runasync(on:feeds:targetoperations:resultsdictionary:executiondescriptor:))*