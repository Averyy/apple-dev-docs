# ARKitCoordinateSpace.Correction

**Framework**: ARKit  
**Kind**: enum

A correction type to apply on coordinate spaces returned from ARKit APIs.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
@frozen
enum Correction
```

## Topics

### Enumeration Cases
- [ARKitCoordinateSpace.Correction.none](arkitcoordinatespace/correction/none.md)
  Coordinate spaces are unaltered and represent actual locations.
- [ARKitCoordinateSpace.Correction.rendered](arkitcoordinatespace/correction/rendered.md)
  Coordinate spaces are corrected to render over physical objects in passthrough displays.
### Instance Properties
- [var description: String](arkitcoordinatespace/correction/description.md)
  Textual description of this correction type.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitcoordinatespace/correction)*