# PlaneAnchor

**Framework**: ARKit  
**Kind**: struct

An anchor that represents horizontal and vertical planes.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct PlaneAnchor
```

## Topics

### Inspecting a plane anchor
- [var originFromAnchorTransform: simd_float4x4](planeanchor/originfromanchortransform.md)
  The location and orientation of a plane in world space.
- [var alignment: PlaneAnchor.Alignment](planeanchor/alignment-swift.property.md)
  The general orientation of the detected plane with respect to gravity.
- [PlaneAnchor.Alignment](planeanchor/alignment-swift.enum.md)
  Values describing possible general orientations of a detected plane with respect to gravity.
- [var classification: PlaneAnchor.Classification](planeanchor/classification-swift.property.md)
  Get the classification of this plane.
- [PlaneAnchor.Classification](planeanchor/classification-swift.enum.md)
  The kinds of object classification a plane anchor can have.
- [var description: String](planeanchor/description.md)
  A textual representation of this anchor.
### Getting the shape of a plane anchor
- [var geometry: PlaneAnchor.Geometry](planeanchor/geometry-swift.property.md)
  Get the geometry of the plane in the anchor’s coordinate system.
- [PlaneAnchor.Geometry](planeanchor/geometry-swift.struct.md)
  The geometry of a plane anchor.
### Identifying a plane anchor
- [var id: UUID](planeanchor/id.md)
  The unique identifier of this anchor.

## Relationships

### Conforms To
- [Anchor](anchor.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Placing content on detected planes](../visionOS/placing-content-on-detected-planes.md)
  Detect horizontal surfaces like tables and floors, as well as vertical planes like walls and doors.
- [class PlaneDetectionProvider](planedetectionprovider.md)
  A source of live data about planes in a person’s surroundings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/planeanchor)*