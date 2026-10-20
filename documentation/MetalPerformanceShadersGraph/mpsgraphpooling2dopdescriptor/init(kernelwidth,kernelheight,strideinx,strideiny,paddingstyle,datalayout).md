# init(kernelWidth:kernelHeight:strideInX:strideInY:paddingStyle:dataLayout:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (instancetype) descriptorWithKernelWidth:(NSUInteger) kernelWidth kernelHeight:(NSUInteger) kernelHeight strideInX:(NSUInteger) strideInX strideInY:(NSUInteger) strideInY paddingStyle:(MPSGraphPaddingStyle) paddingStyle dataLayout:(MPSGraphTensorNamedDataLayout) dataLayout;
```

#### Return Value

The descriptor on autoreleasepool.

## Parameters

- `kernelWidth`: See `kernelWidth` property.
- `kernelHeight`: See `kernelHeight`` property.
- `strideInX`: See `strideInX` property.
- `strideInY`: See `strideInY` property.
- `paddingStyle`: See `paddingStyle` property.
- `dataLayout`: See `dataLayout` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling2dopdescriptor/init(kernelwidth:kernelheight:strideinx:strideiny:paddingstyle:datalayout:))*