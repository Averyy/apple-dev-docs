# init(strideInX:strideInY:dilationRateInX:dilationRateInY:groups:paddingStyle:dataLayout:weightsLayout:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (instancetype) descriptorWithStrideInX:(NSUInteger) strideInX strideInY:(NSUInteger) strideInY dilationRateInX:(NSUInteger) dilationRateInX dilationRateInY:(NSUInteger) dilationRateInY groups:(NSUInteger) groups paddingStyle:(MPSGraphPaddingStyle) paddingStyle dataLayout:(MPSGraphTensorNamedDataLayout) dataLayout weightsLayout:(MPSGraphTensorNamedDataLayout) weightsLayout;
```

#### Return Value

The `MPSGraphConvolution2DOpDescriptor` on autoreleasepool.

## Parameters

- `strideInX`: See [`strideInX`](./strideinx.md) property.
- `strideInY`: See [`strideInY`](./strideiny.md) property.
- `dilationRateInX`: See [`dilationRateInX`](./dilationrateinx.md) property.
- `dilationRateInY`: See [`dilationRateInY`](./dilationrateiny.md) property.
- `groups`: See [`groups`](./groups.md) property.
- `paddingStyle`: See [`paddingStyle`](./paddingstyle.md) property.
- `dataLayout`: See [`dataLayout`](./datalayout.md) property.
- `weightsLayout`: See [`weightsLayout`](./weightslayout.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution2dopdescriptor/init(strideinx:strideiny:dilationrateinx:dilationrateiny:groups:paddingstyle:datalayout:weightslayout:))*