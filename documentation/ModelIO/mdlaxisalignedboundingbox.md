# MDLAxisAlignedBoundingBox

**Framework**: Model I/O  
**Kind**: struct

The minimal volume containing an object, used by the [`boundingBox(atTime:)`](mdlobject/boundingbox(attime:).md) method.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct MDLAxisAlignedBoundingBox
```

## Topics

### Initializers
- [init()](mdlaxisalignedboundingbox/init.md)
- [init(maxBounds: vector_float3, minBounds: vector_float3)](mdlaxisalignedboundingbox/init(maxbounds:minbounds:).md)
### Instance Properties
- [var maxBounds: vector_float3](mdlaxisalignedboundingbox/maxbounds.md)
  The corner of the bounding box with the highest x-, y-, and z-coordinate values.
- [var minBounds: vector_float3](mdlaxisalignedboundingbox/minbounds.md)
  The corner of the bounding box with the lowest x-, y-, and z-coordinate values.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlaxisalignedboundingbox)*