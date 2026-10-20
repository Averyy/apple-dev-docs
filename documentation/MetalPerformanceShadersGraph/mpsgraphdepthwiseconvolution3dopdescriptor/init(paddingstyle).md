# init(paddingStyle:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init  
**Role**: Initializer

Creates a 3D depthwise convolution descriptor with default values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(paddingStyle: MPSGraphPaddingStyle)
```

```objc
+ (instancetype) descriptorWithPaddingStyle:(MPSGraphPaddingStyle) paddingStyle;
```

#### Return Value

The descriptor on autoreleasepool.

## Parameters

- `paddingStyle`: See `paddingStyle` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphdepthwiseconvolution3dopdescriptor/init(paddingstyle:))*