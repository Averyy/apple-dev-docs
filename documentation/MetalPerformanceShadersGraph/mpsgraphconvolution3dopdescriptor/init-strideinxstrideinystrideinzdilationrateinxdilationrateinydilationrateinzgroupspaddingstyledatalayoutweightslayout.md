# init(strideInX:strideInY:strideInZ:dilationRateInX:dilationRateInY:dilationRateInZ:groups:paddingStyle:dataLayout:weightsLayout:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init

Creates a convolution descriptor with given values for parameters.

**Availability**:
- iOS 16.3+
- iPadOS 16.3+
- Mac Catalyst 16.3+
- macOS 13.2+
- tvOS 16.3+
- visionOS 1.0+

## Declaration

```swift
convenience init?(strideInX: Int, strideInY: Int, strideInZ: Int, dilationRateInX: Int, dilationRateInY: Int, dilationRateInZ: Int, groups: Int, paddingStyle: MPSGraphPaddingStyle, dataLayout: MPSGraphTensorNamedDataLayout, weightsLayout: MPSGraphTensorNamedDataLayout)
```

#### Return Value

The `MPSGraphConvolution3DOpDescriptor` on autoreleasepool.

## Parameters

- `strideInX`: See [`strideInX`](mpsgraphconvolution3dopdescriptor/strideinx.md) property.
- `strideInY`: See [`strideInY`](mpsgraphconvolution3dopdescriptor/strideiny.md) property.
- `strideInZ`: See [`strideInZ`](mpsgraphconvolution3dopdescriptor/strideinz.md) property.
- `dilationRateInX`: See [`dilationRateInX`](mpsgraphconvolution3dopdescriptor/dilationrateinx.md) property.
- `dilationRateInY`: See [`dilationRateInY`](mpsgraphconvolution3dopdescriptor/dilationrateiny.md) property.
- `dilationRateInZ`: See [`dilationRateInZ`](mpsgraphconvolution3dopdescriptor/dilationrateinz.md) property.
- `groups`: See [`groups`](mpsgraphconvolution3dopdescriptor/groups.md) property.
- `paddingStyle`: See [`paddingStyle`](mpsgraphconvolution3dopdescriptor/paddingstyle.md) property.
- `dataLayout`: See [`dataLayout`](mpsgraphconvolution3dopdescriptor/datalayout.md) property.
- `weightsLayout`: See [`weightsLayout`](mpsgraphconvolution3dopdescriptor/weightslayout.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution3dopdescriptor/init(strideinx:strideiny:strideinz:dilationrateinx:dilationrateiny:dilationrateinz:groups:paddingstyle:datalayout:weightslayout:))*