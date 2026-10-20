# ARKitCoordinateSpace.Correction

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

A correction type to apply on coordinate spaces returned from ARKit APIs.

**Availability**:
- macOS 27.0+
- visionOS 26.0+

## Declaration

```swift
@frozen
enum Correction
```

## Topics

### Enumeration Cases
- [ARKitCoordinateSpace.Correction.none](./correction/none.md)
  Coordinate spaces are unaltered and represent actual locations.
- [ARKitCoordinateSpace.Correction.rendered](./correction/rendered.md)
  Coordinate spaces are corrected to render over physical objects in passthrough displays.
### Instance Properties
- [var description: String](./correction/description.md)
  Textual description of this correction type.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arkitcoordinatespace/correction)*