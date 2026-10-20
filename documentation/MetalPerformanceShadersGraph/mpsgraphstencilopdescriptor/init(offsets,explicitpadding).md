# init(offsets:explicitPadding:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: init  
**Role**: Initializer

Creates a stencil operation descriptor with default values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(offsets: [NSNumber], explicitPadding: [NSNumber])
```

```objc
+ (instancetype) descriptorWithOffsets:(MPSShape *) offsets explicitPadding:(MPSShape *) explicitPadding;
```

#### Return Value

A valid MPSGraphStencilOpDescriptor object

## Parameters

- `offsets`: See `offsets` property.
- `explicitPadding`: See `explicitPadding` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphstencilopdescriptor/init(offsets:explicitpadding:))*