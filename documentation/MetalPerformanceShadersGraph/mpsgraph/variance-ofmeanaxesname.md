# variance(of:mean:axes:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Returns the variance of the first input along the specified axes when the mean has been precomputed.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func variance(of tensor: MPSGraphTensor, mean meanTensor: MPSGraphTensor, axes: [NSNumber], name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object.

## Parameters

- `axes`: A list of axes over which to perform the reduction such that the order of dimensions goes from the slowest moving at axis=0 to the fastest moving dimension.
- `name`: An optional name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/variance(of:mean:axes:name:))*