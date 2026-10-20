# init(reductionMode:offsets:strides:dilationRates:explicitPadding:boundaryMode:paddingStyle:paddingConstant:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init  
**Role**: Initializer

Creates a stencil operation descriptor with given values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(reductionMode: MPSGraphReductionMode, offsets: [NSNumber], strides: [NSNumber], dilationRates: [NSNumber], explicitPadding: [NSNumber], boundaryMode: MPSGraphPaddingMode, paddingStyle: MPSGraphPaddingStyle, paddingConstant: Float)
```

```objc
+ (instancetype) descriptorWithReductionMode:(MPSGraphReductionMode) reductionMode offsets:(MPSShape *) offsets strides:(MPSShape *) strides dilationRates:(MPSShape *) dilationRates explicitPadding:(MPSShape *) explicitPadding boundaryMode:(MPSGraphPaddingMode) boundaryMode paddingStyle:(MPSGraphPaddingStyle) paddingStyle paddingConstant:(float) paddingConstant;
```

#### Return Value

A valid MPSGraphStencilOpDescriptor object

## Parameters

- `reductionMode`: See `reductionMode` property.
- `offsets`: See `offsets` property.
- `strides`: See `strides` property.
- `dilationRates`: See `dilationRates` property.
- `explicitPadding`: See `explicitPadding` property.
- `boundaryMode`: See `boundaryMode` property.
- `paddingStyle`: See `paddingStyle` property.
- `paddingConstant`: See `paddingConstant` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphstencilopdescriptor/init(reductionmode:offsets:strides:dilationrates:explicitpadding:boundarymode:paddingstyle:paddingconstant:))*