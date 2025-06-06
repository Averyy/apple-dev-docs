# init(kernelWidth:kernelHeight:strideInX:strideInY:paddingStyle:dataLayout:)

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
convenience init?(kernelWidth: Int, kernelHeight: Int, strideInX: Int, strideInY: Int, paddingStyle: MPSGraphPaddingStyle, dataLayout: MPSGraphTensorNamedDataLayout)
```

#### Return Value

The descriptor on autoreleasepool.

## Parameters

- `kernelWidth`: See   property.
- `kernelHeight`: See `kernelHeight`` property.
- `strideInX`: See   property.
- `strideInY`: See   property.
- `paddingStyle`: See   property.
- `dataLayout`: See   property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling2dopdescriptor/init(kernelwidth:kernelheight:strideinx:strideiny:paddingstyle:datalayout:))*