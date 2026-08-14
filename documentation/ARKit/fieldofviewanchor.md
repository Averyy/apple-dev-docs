# FieldOfViewAnchor

**Framework**: ARKit  
**Kind**: struct

An anchor representing a set of field of view (FoV) boundary polygon points in immersive space.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct FieldOfViewAnchor
```

#### Overview

This anchor provides polygon points that define preset FoV boundaries, allowing applications to visualize these FoVs in the immersive space.

## Topics

### Instance Properties
- [var description: String](fieldofviewanchor/description.md)
  A textual representation of this anchor.
- [var id: UUID](fieldofviewanchor/id.md)
  The unique identifier of this anchor.
- [var leftPolygonPoints: [simd_float4]](fieldofviewanchor/leftpolygonpoints.md)
  Left eye polygon boundary points defining the preset field of view.
- [var originFromAnchorTransform: simd_float4x4](fieldofviewanchor/originfromanchortransform.md)
  The transform from the anchor to the origin coordinate system.
- [var rightPolygonPoints: [simd_float4]](fieldofviewanchor/rightpolygonpoints.md)
  Right eye polygon boundary points defining the preset field of view.
- [var timestamp: TimeInterval](fieldofviewanchor/timestamp.md)
  The timestamp of this anchor.
### Instance Methods
- [func coordinateSpace(correction: ARKitCoordinateSpace.Correction) -> ARKitCoordinateSpace](fieldofviewanchor/coordinatespace(correction:).md)
  The anchor’s coordinate space.

## Relationships

### Conforms To
- [ARKitCoordinateSpaceProviding](arkitcoordinatespaceproviding.md)
- [Anchor](anchor.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class VisualFidelityProvider](visualfidelityprovider.md)
  A data provider that delivers visual fidelity monitoring data.
- [struct VisualFidelityData](visualfidelitydata.md)
  Visual fidelity data containing device fit and field of view verification.
- [enum DeviceFitStatus](devicefitstatus.md)
  Device fit validation status indicating the user’s eye position relative to the optimal device fit range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/fieldofviewanchor)*