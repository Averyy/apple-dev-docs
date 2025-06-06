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

- `strideInX`: See   property.
- `strideInY`: See   property.
- `strideInZ`: See   property.
- `dilationRateInX`: See   property.
- `dilationRateInY`: See   property.
- `dilationRateInZ`: See   property.
- `groups`: See   property.
- `paddingLeft`: See   property.
- `paddingRight`: See   property.
- `paddingTop`: See   property.
- `paddingBottom`: See   property.
- `paddingFront`: See   property.
- `paddingBack`: See   property.
- `paddingStyle`: See   property.
- `dataLayout`: See   property.
- `weightsLayout`: See   property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution3dopdescriptor/init(strideinx:strideiny:strideinz:dilationrateinx:dilationrateiny:dilationrateinz:groups:paddingleft:paddingright:paddingtop:paddingbottom:paddingfront:paddingback:paddingstyle:datalayout:weightslayout:))*