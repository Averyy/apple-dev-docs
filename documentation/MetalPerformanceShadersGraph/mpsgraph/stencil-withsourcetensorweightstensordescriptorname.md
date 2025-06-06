# stencil(withSourceTensor:weightsTensor:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a stencil operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func stencil(withSourceTensor source: MPSGraphTensor, weightsTensor weights: MPSGraphTensor, descriptor: MPSGraphStencilOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Performs a weighted reduction operation (See [`reductionMode`](mpsgraphstencilopdescriptor/reductionmode.md)) on the last 4 dimensions of the `source` over the window determined by `weights`, according to the value defined in `descriptor`.

```md
   y[i] = reduction{j \in w} ( x[ i + j ]w[j] )
```

## Parameters

- `source`: The tensor containing the source data. Must be of rank 4 or greater.
- `weights`: A 4-D tensor containing the weights data.
- `descriptor`: The descriptor object that specifies the parameters for the stencil operation.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/stencil(withsourcetensor:weightstensor:descriptor:name:))*