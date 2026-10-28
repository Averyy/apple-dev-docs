# init(kernelSizes:strides:dilationRates:paddingValues:paddingStyle:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init  
**Role**: Initializer

Creates a 4D pooling descriptor with given values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(kernelSizes: [NSNumber], strides: [NSNumber], dilationRates: [NSNumber], paddingValues: [NSNumber], paddingStyle: MPSGraphPaddingStyle)
```

```objc
+ (instancetype) descriptorWithKernelSizes:(NSArray<NSNumber *> *) kernelSizes strides:(NSArray<NSNumber *> *) strides dilationRates:(NSArray<NSNumber *> *) dilationRates paddingValues:(NSArray<NSNumber *> *) paddingValues paddingStyle:(MPSGraphPaddingStyle) paddingStyle;
```

## Return Value

The descriptor on autoreleasepool.

## Parameters

- `kernelSizes`: See `kernelSizes` property.
- `strides`: See `strides` property.
- `dilationRates`: See `dilationRates` property.
- `paddingValues`: See `paddingValues` property.
- `paddingStyle`: See `paddingStyle` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling4dopdescriptor/init(kernelsizes:strides:dilationrates:paddingvalues:paddingstyle:))*