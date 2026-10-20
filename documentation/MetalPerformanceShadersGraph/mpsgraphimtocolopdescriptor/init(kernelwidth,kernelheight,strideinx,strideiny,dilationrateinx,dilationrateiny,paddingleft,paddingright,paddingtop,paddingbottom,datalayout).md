# init(kernelWidth:kernelHeight:strideInX:strideInY:dilationRateInX:dilationRateInY:paddingLeft:paddingRight:paddingTop:paddingBottom:dataLayout:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (instancetype) descriptorWithKernelWidth:(NSUInteger) kernelWidth kernelHeight:(NSUInteger) kernelHeight strideInX:(NSUInteger) strideInX strideInY:(NSUInteger) strideInY dilationRateInX:(NSUInteger) dilationRateInX dilationRateInY:(NSUInteger) dilationRateInY paddingLeft:(NSUInteger) paddingLeft paddingRight:(NSUInteger) paddingRight paddingTop:(NSUInteger) paddingTop paddingBottom:(NSUInteger) paddingBottom dataLayout:(MPSGraphTensorNamedDataLayout) dataLayout;
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
- `paddingLeft`: See `paddingLeft` property.
- `paddingRight`: See `paddingRight` property.
- `paddingTop`: See `paddingTop` property.
- `paddingBottom`: See `paddingBottom` property.
- `dataLayout`: See `dataLayout` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphimtocolopdescriptor/init(kernelwidth:kernelheight:strideinx:strideiny:dilationrateinx:dilationrateiny:paddingleft:paddingright:paddingtop:paddingbottom:datalayout:))*