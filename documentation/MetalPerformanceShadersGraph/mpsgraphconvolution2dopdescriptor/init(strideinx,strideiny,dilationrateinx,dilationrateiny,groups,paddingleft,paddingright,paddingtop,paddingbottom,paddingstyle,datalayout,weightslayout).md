# init(strideInX:strideInY:dilationRateInX:dilationRateInY:groups:paddingLeft:paddingRight:paddingTop:paddingBottom:paddingStyle:dataLayout:weightsLayout:)

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
convenience init?(strideInX: Int, strideInY: Int, dilationRateInX: Int, dilationRateInY: Int, groups: Int, paddingLeft: Int, paddingRight: Int, paddingTop: Int, paddingBottom: Int, paddingStyle: MPSGraphPaddingStyle, dataLayout: MPSGraphTensorNamedDataLayout, weightsLayout: MPSGraphTensorNamedDataLayout)
```

```objc
+ (instancetype) descriptorWithStrideInX:(NSUInteger) strideInX strideInY:(NSUInteger) strideInY dilationRateInX:(NSUInteger) dilationRateInX dilationRateInY:(NSUInteger) dilationRateInY groups:(NSUInteger) groups paddingLeft:(NSUInteger) paddingLeft paddingRight:(NSUInteger) paddingRight paddingTop:(NSUInteger) paddingTop paddingBottom:(NSUInteger) paddingBottom paddingStyle:(MPSGraphPaddingStyle) paddingStyle dataLayout:(MPSGraphTensorNamedDataLayout) dataLayout weightsLayout:(MPSGraphTensorNamedDataLayout) weightsLayout;
```

#### Return Value

The `MPSGraphConvolution2DOpDescriptor` on autoreleasepool.

## Parameters

- `strideInX`: See [`strideInX`](./strideinx.md) property.
- `strideInY`: See [`strideInY`](./strideiny.md) property.
- `dilationRateInX`: See [`dilationRateInX`](./dilationrateinx.md) property.
- `dilationRateInY`: See [`dilationRateInY`](./dilationrateiny.md) property.
- `groups`: See [`groups`](./groups.md) property.
- `paddingLeft`: See [`paddingLeft`](./paddingleft.md) property.
- `paddingRight`: See [`paddingRight`](./paddingright.md) property.
- `paddingTop`: See [`paddingTop`](./paddingtop.md) property.
- `paddingBottom`: See [`paddingBottom`](./paddingbottom.md) property.
- `paddingStyle`: See [`paddingStyle`](./paddingstyle.md) property.
- `dataLayout`: See [`dataLayout`](./datalayout.md) property.
- `weightsLayout`: See [`weightsLayout`](./weightslayout.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution2dopdescriptor/init(strideinx:strideiny:dilationrateinx:dilationrateiny:groups:paddingleft:paddingright:paddingtop:paddingbottom:paddingstyle:datalayout:weightslayout:))*