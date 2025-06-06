# init(kernelWidth:kernelHeight:strideInX:strideInY:dilationRateInX:dilationRateInY:paddingLeft:paddingRight:paddingTop:paddingBottom:dataLayout:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init

Creates an image to column descriptor with given values for parameters.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(kernelWidth: Int, kernelHeight: Int, strideInX: Int, strideInY: Int, dilationRateInX: Int, dilationRateInY: Int, paddingLeft: Int, paddingRight: Int, paddingTop: Int, paddingBottom: Int, dataLayout: MPSGraphTensorNamedDataLayout)
```

#### Return Value

A valid MPSGraphImToColOpDescriptor on autoreleasepool.

## Parameters

- `kernelWidth`: See   property.
- `kernelHeight`: See   property.
- `strideInX`: See   property.
- `strideInY`: See   property.
- `dilationRateInX`: See   property.
- `dilationRateInY`: See   property.
- `paddingLeft`: See   property.
- `paddingRight`: See   property.
- `paddingTop`: See   property.
- `paddingBottom`: See   property.
- `dataLayout`: See   property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphimtocolopdescriptor/init(kernelwidth:kernelheight:strideinx:strideiny:dilationrateinx:dilationrateiny:paddingleft:paddingright:paddingtop:paddingbottom:datalayout:))*