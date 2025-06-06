# dataLayout

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The named layout of data in the source tensor.

**Availability**:
- iOS 16.3+
- iPadOS 16.3+
- Mac Catalyst 16.3+
- macOS 13.2+
- tvOS 16.3+
- visionOS 1.0+

## Declaration

```swift
var dataLayout: MPSGraphTensorNamedDataLayout { get set }
```

#### Discussion

It defines the order of named dimensions (Batch, Channel, Depth, Height, Width). The convolution operation uses this to interpret data in the source tensor. For example, if `dataLayout` is `MPSGraphTensorNamedDataLayoutNCDHW`, frameork interprets data in source tensor as `batch x channels x depth x height x width` with `width` as fastest moving dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution3dopdescriptor/datalayout)*