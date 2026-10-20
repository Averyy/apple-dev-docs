# run(with:feeds:targetOperations:resultsDictionary:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Runs the graph for the given feeds and returns the target tensor values in the results dictionary provided by the user.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func run(with commandQueue: any MTLCommandQueue, feeds: [MPSGraphTensor : MPSGraphTensorData], targetOperations: [MPSGraphOperation]?, resultsDictionary: [MPSGraphTensor : MPSGraphTensorData])
```

```objc
- (void) runWithMTLCommandQueue:(id<MTLCommandQueue>) commandQueue feeds:(MPSGraphTensorDataDictionary *) feeds targetOperations:(NSArray<MPSGraphOperation *> *) targetOperations resultsDictionary:(MPSGraphTensorDataDictionary *) resultsDictionary;
```

#### Discussion

It also ensures all target operations also executed. This call blocks until execution has completed.

## Parameters

- `commandQueue`: CommandQueue passed to exectute the graph on.
- `feeds`: Feeds dictionary for the placeholder tensors.
- `targetOperations`: Operations to be completed at the end of the run.
- `resultsDictionary`: MPSGraphTensors dictionary passed by user, these will be filled with graph output data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/run(with:feeds:targetoperations:resultsdictionary:))*