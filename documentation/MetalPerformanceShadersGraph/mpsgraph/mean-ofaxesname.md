# mean(of:axes:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Returns the mean of the first input along the specified axes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func mean(of tensor: MPSGraphTensor, axes: [NSNumber], name: String?) -> MPSGraphTensor
```

#### Return Value

A valid `MPSGraphTensor` object.

## Parameters

- `axes`: A list of axes over which to perform the reduction. The order of dimensions goes from the slowest moving at axis=0 to the fastest moving dimension.
- `name`: An optional name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/mean(of:axes:name:))*