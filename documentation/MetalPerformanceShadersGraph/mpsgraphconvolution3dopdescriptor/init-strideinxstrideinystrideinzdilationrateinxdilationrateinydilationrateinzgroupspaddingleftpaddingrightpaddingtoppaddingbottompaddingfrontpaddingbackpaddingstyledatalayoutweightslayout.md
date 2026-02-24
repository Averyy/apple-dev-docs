# init(strideInX:strideInY:strideInZ:dilationRateInX:dilationRateInY:dilationRateInZ:groups:paddingLeft:paddingRight:paddingTop:paddingBottom:paddingFront:paddingBack:paddingStyle:dataLayout:weightsLayout:)

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
convenience init?(strideInX: Int, strideInY: Int, strideInZ: Int, dilationRateInX: Int, dilationRateInY: Int, dilationRateInZ: Int, groups: Int, paddingLeft: Int, paddingRight: Int, paddingTop: Int, paddingBottom: Int, paddingFront: Int, paddingBack: Int, paddingStyle: MPSGraphPaddingStyle, dataLayout: MPSGraphTensorNamedDataLayout, weightsLayout: MPSGraphTensorNamedDataLayout)
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
- `paddingLeft`: See [`paddingLeft`](mpsgraphconvolution3dopdescriptor/paddingleft.md) property.
- `paddingRight`: See [`paddingRight`](mpsgraphconvolution3dopdescriptor/paddingright.md) property.
- `paddingTop`: See [`paddingTop`](mpsgraphconvolution3dopdescriptor/paddingtop.md) property.
- `paddingBottom`: See [`paddingBottom`](mpsgraphconvolution3dopdescriptor/paddingbottom.md) property.
- `paddingFront`: See [`paddingFront`](mpsgraphconvolution3dopdescriptor/paddingfront.md) property.
- `paddingBack`: See [`paddingBack`](mpsgraphconvolution3dopdescriptor/paddingback.md) property.
- `paddingStyle`: See [`paddingStyle`](mpsgraphconvolution3dopdescriptor/paddingstyle.md) property.
- `dataLayout`: See [`dataLayout`](mpsgraphconvolution3dopdescriptor/datalayout.md) property.
- `weightsLayout`: See [`weightsLayout`](mpsgraphconvolution3dopdescriptor/weightslayout.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution3dopdescriptor/init(strideinx:strideiny:strideinz:dilationrateinx:dilationrateiny:dilationrateinz:groups:paddingleft:paddingright:paddingtop:paddingbottom:paddingfront:paddingback:paddingstyle:datalayout:weightslayout:))*