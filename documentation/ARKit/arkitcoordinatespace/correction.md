# ARKitCoordinateSpace.Correction

**Framework**: ARKit  
**Kind**: enum

A correction type to apply on coordinate spaces returned from ARKit APIs.

**Availability**:
- macOS 27.0+ (Beta)
- visionOS 26.0+

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
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitcoordinatespace/correction)*