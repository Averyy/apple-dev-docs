# init(kernelWidth:kernelHeight:strideInX:strideInY:dilationRateInX:dilationRateInY:paddingLeft:paddingRight:paddingTop:paddingBottom:paddingStyle:dataLayout:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init

Creates a 2D pooling descriptor with given values.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(kernelWidth: Int, kernelHeight: Int, strideInX: Int, strideInY: Int, dilationRateInX: Int, dilationRateInY: Int, paddingLeft: Int, paddingRight: Int, paddingTop: Int, paddingBottom: Int, paddingStyle: MPSGraphPaddingStyle, dataLayout: MPSGraphTensorNamedDataLayout)
```

#### Return Value

The descriptor on autoreleasepool.

## Parameters

- `kernelWidth`: See `kernelWidth` property.
- `kernelHeight`: See `kernelHeight` property.
- `strideInX`: See `strideInX` property.
- `strideInY`: See `strideInY` property.
- `dilationRateInX`: See `dilationRateInX` property.
- `dilationRateInY`: See `dilationRateInY` property.
- `paddingLeft`: See `paddingLeft` property.
- `paddingRight`: See `paddingRight` property.
- `paddingTop`: See `paddingTop` property.
- `paddingBottom`: See `paddingBottom` property.
- `paddingStyle`: See `paddingStyle` property.
- `dataLayout`: See `dataLayout` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling2dopdescriptor/init(kernelwidth:kernelheight:strideinx:strideiny:dilationrateinx:dilationrateiny:paddingleft:paddingright:paddingtop:paddingbottom:paddingstyle:datalayout:))*