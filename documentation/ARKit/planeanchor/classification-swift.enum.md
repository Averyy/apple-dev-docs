# PlaneAnchor.Classification

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

The kinds of object classification a plane anchor can have.

**Availability**:
- visionOS 1.0+ - Deprecated in 26.0 (renamed: SurfaceClassification)

## Declaration

```swift
enum Classification
```

## Topics

### Getting known classifications
- [PlaneAnchor.Classification.ceiling](./classification-swift.enum/ceiling.md)
  A ceiling.
- [PlaneAnchor.Classification.door](./classification-swift.enum/door.md)
  A door.
- [PlaneAnchor.Classification.floor](./classification-swift.enum/floor.md)
  A floor.
- [PlaneAnchor.Classification.seat](./classification-swift.enum/seat.md)
  A seat.
- [PlaneAnchor.Classification.table](./classification-swift.enum/table.md)
  A table.
- [PlaneAnchor.Classification.wall](./classification-swift.enum/wall.md)
  A wall.
- [PlaneAnchor.Classification.window](./classification-swift.enum/window.md)
  A window.
### Getting unknown classifications
- [PlaneAnchor.Classification.notAvailable](./classification-swift.enum/notavailable.md)
  A plane classification is currently unavailable.
- [PlaneAnchor.Classification.undetermined](./classification-swift.enum/undetermined.md)
  A plane classification hasn’t been determined yet.
- [PlaneAnchor.Classification.unknown](./classification-swift.enum/unknown.md)
  A plane classification isn’t one of the known classes.
### Instance Properties
- [var description: String](./classification-swift.enum/description.md)
  A textual representation of PlaneAnchor.Classification

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting a plane anchor
- [var originFromAnchorTransform: simd_float4x4](./originfromanchortransform.md)
  The location and orientation of a plane in world space.
- [var alignment: PlaneAnchor.Alignment](./alignment-swift.property.md)
  The general orientation of the detected plane with respect to gravity.
- [PlaneAnchor.Alignment](./alignment-swift.enum.md)
  Values describing possible general orientations of a detected plane with respect to gravity.
- [var classification: PlaneAnchor.Classification](./classification-swift.property.md)
  Get the classification of this plane.
- [var description: String](./description.md)
  A textual representation of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planeanchor/classification-swift.enum)*