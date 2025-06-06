# PlaneAnchor.Classification

**Framework**: ARKit  
**Kind**: enum

The kinds of object classification a plane anchor can have.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum Classification
```

## Topics

### Getting known classifications
- [PlaneAnchor.Classification.ceiling](planeanchor/classification-swift.enum/ceiling.md)
  A ceiling.
- [PlaneAnchor.Classification.door](planeanchor/classification-swift.enum/door.md)
  A door.
- [PlaneAnchor.Classification.floor](planeanchor/classification-swift.enum/floor.md)
  A floor.
- [PlaneAnchor.Classification.seat](planeanchor/classification-swift.enum/seat.md)
  A seat.
- [PlaneAnchor.Classification.table](planeanchor/classification-swift.enum/table.md)
  A table.
- [PlaneAnchor.Classification.wall](planeanchor/classification-swift.enum/wall.md)
  A wall.
- [PlaneAnchor.Classification.window](planeanchor/classification-swift.enum/window.md)
  A window.
### Getting unknown classifications
- [PlaneAnchor.Classification.notAvailable](planeanchor/classification-swift.enum/notavailable.md)
  A plane classification is currently unavailable.
- [PlaneAnchor.Classification.undetermined](planeanchor/classification-swift.enum/undetermined.md)
  A plane classification hasn’t been determined yet.
- [PlaneAnchor.Classification.unknown](planeanchor/classification-swift.enum/unknown.md)
  A plane classification isn’t one of the known classes.
### Instance Properties
- [var description: String](planeanchor/classification-swift.enum/description.md)
  A textual representation of PlaneAnchor.Classification

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var originFromAnchorTransform: simd_float4x4](planeanchor/originfromanchortransform.md)
  The location and orientation of a plane in world space.
- [var alignment: PlaneAnchor.Alignment](planeanchor/alignment-swift.property.md)
  The general orientation of the detected plane with respect to gravity.
- [PlaneAnchor.Alignment](planeanchor/alignment-swift.enum.md)
  Values describing possible general orientations of a detected plane with respect to gravity.
- [var classification: PlaneAnchor.Classification](planeanchor/classification-swift.property.md)
  Get the classification of this plane.
- [var description: String](planeanchor/description.md)
  A textual representation of this anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planeanchor/classification-swift.enum)*