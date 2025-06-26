# CameraRegionAnchor

**Framework**: ARKit  
**Kind**: struct

Represents a camera region anchor.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct CameraRegionAnchor
```

## Topics

### Initializers
- [init(originFromAnchorTransform: simd_float4x4, width: Float, height: Float, cameraEnhancement: CameraRegionAnchor.CameraEnhancement)](cameraregionanchor/init(originfromanchortransform:width:height:cameraenhancement:).md)
  Initialize a camera region anchor.
### Instance Properties
- [var cameraEnhancement: CameraRegionAnchor.CameraEnhancement](cameraregionanchor/cameraenhancement-swift.property.md)
  The camera enhancement used with this anchor.
- [var description: String](cameraregionanchor/description.md)
  A textual representation of this anchor.
- [var height: Float](cameraregionanchor/height.md)
  The height of the region, in meters. This is [-height/2, height/2] from the center.
- [var id: UUID](cameraregionanchor/id.md)
  The unique identifier of this anchor.
- [var originFromAnchorTransform: simd_float4x4](cameraregionanchor/originfromanchortransform.md)
  The transform from the anchor to the origin coordinate system.
- [var pixelBuffer: CVReadOnlyPixelBuffer?](cameraregionanchor/pixelbuffer.md)
  The pixel buffer, or nil if not set.
- [var width: Float](cameraregionanchor/width.md)
  The width of the region, in meters. This is [-width/2, width/2] from the center.
### Enumerations
- [CameraRegionAnchor.CameraEnhancement](cameraregionanchor/cameraenhancement-swift.enum.md)
  Enhancements to be used with each anchor.

## Relationships

### Conforms To
- [Anchor](anchor.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraregionanchor)*