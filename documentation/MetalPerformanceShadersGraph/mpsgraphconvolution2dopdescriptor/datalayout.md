# dataLayout

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The named layout of data in the source tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var dataLayout: MPSGraphTensorNamedDataLayout { get set }
```

#### Discussion

It defines the order of named dimensions (Batch, Channel, Height, Width). The convolution operation uses this to interpret data in the source tensor. For example, if `dataLayout` is `MPSGraphTensorNamedDataLayoutNCHW`, frameork interprets data in source tensor as `batch x channels x height x width` with `width` as fastest moving dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution2dopdescriptor/datalayout)*