# weightsLayout

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The named layout of data in the weights tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var weightsLayout: MPSGraphTensorNamedDataLayout { get set }
```

#### Discussion

It defines the order of named dimensions (Output channels, Input channels, Kernel height, Kernel width). The convolution operation uses this to interpret data in the weights tensor. For example, if `weightsLayout` is `MPSGraphTensorNamedDataLayoutOIHW`, frameork interprets data in weights tensor as `outputChannels x inputChannels x kernelHeight x kernelWidth` with `kernelWidth` as fastest moving dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution2dopdescriptor/weightslayout)*