# run(feeds:targetTensors:targetOperations:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Runs the graph for the given feeds and returns the target tensor values, ensuring all target operations also executed.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func run(feeds: [MPSGraphTensor : MPSGraphTensorData], targetTensors: [MPSGraphTensor], targetOperations: [MPSGraphOperation]?) -> [MPSGraphTensor : MPSGraphTensorData]
```

#### Return Value

A valid MPSGraphTensor : MPSGraphTensorData dictionary with results synchronized to the CPU memory.

#### Discussion

This call blocks until execution has completed.

## Parameters

- `feeds`: Feeds dictionary for the placeholder tensors.
- `targetTensors`: Tensors for which the caller wishes MPSGraphTensorData to be returned.
- `targetOperations`: Operations to be completed at the end of the run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/run(feeds:targettensors:targetoperations:))*