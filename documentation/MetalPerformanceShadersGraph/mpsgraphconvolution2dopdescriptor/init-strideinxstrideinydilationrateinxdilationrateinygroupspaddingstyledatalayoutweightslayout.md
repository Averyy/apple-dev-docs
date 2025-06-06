# init(strideInX:strideInY:dilationRateInX:dilationRateInY:groups:paddingStyle:dataLayout:weightsLayout:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init

Creates a convolution descriptor with given values for parameters.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(strideInX: Int, strideInY: Int, dilationRateInX: Int, dilationRateInY: Int, groups: Int, paddingStyle: MPSGraphPaddingStyle, dataLayout: MPSGraphTensorNamedDataLayout, weightsLayout: MPSGraphTensorNamedDataLayout)
```

#### Return Value

The `MPSGraphConvolution2DOpDescriptor` on autoreleasepool.

## Parameters

- `strideInX`: See   property.
- `strideInY`: See   property.
- `dilationRateInX`: See   property.
- `dilationRateInY`: See   property.
- `groups`: See   property.
- `paddingStyle`: See   property.
- `dataLayout`: See   property.
- `weightsLayout`: See   property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution2dopdescriptor/init(strideinx:strideiny:dilationrateinx:dilationrateiny:groups:paddingstyle:datalayout:weightslayout:))*