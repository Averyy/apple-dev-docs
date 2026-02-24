# init(kernelWidth:kernelHeight:strideInX:strideInY:dilationRateInX:dilationRateInY:dataLayout:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init

Creates column to image descriptor with given values for parameters.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(kernelWidth: Int, kernelHeight: Int, strideInX: Int, strideInY: Int, dilationRateInX: Int, dilationRateInY: Int, dataLayout: MPSGraphTensorNamedDataLayout)
```

#### Return Value

A valid MPSGraphImToColOpDescriptor on autoreleasepool.

## Parameters

- `kernelWidth`: See `kernelWidth` property.
- `kernelHeight`: See `kernelHeight` property.
- `strideInX`: See `strideInX` property.
- `strideInY`: See `strideInY` property.
- `dilationRateInX`: See `dilationRateInX` property.
- `dilationRateInY`: See `dilationRateInY` property.
- `dataLayout`: See `dataLayout` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphimtocolopdescriptor/init(kernelwidth:kernelheight:strideinx:strideiny:dilationrateinx:dilationrateiny:datalayout:))*