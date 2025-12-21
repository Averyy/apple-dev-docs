# CameraRegionAnchor

**Framework**: ARKit  
**Kind**: struct

Represents a region in space to capture a camera stream of.

**Availability**:
- visionOS 26.0+

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
  The enhancement applied to this anchor’s pixel buffer.
- [var description: String](cameraregionanchor/description.md)
  A textual representation of this anchor.
- [var height: Float](cameraregionanchor/height.md)
  The height of the region, in meters. This is [-height/2, height/2] from the center.
- [var id: UUID](cameraregionanchor/id.md)
  The unique identifier of this anchor.
- [var originFromAnchorTransform: simd_float4x4](cameraregionanchor/originfromanchortransform.md)
  The transform from the anchor to the origin coordinate system.
- [var pixelBuffer: CVReadOnlyPixelBuffer?](cameraregionanchor/pixelbuffer.md)
  The pixel buffer. Can be nil, e.g. for anchors which have not yet been added to the provider.
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

## See Also

- [class CameraRegionProvider](cameraregionprovider.md)
  A camera region provider. An enterprise license is required to use the CameraRegionProvider. The provider will not deliver any data without it. The app must include the following entitlement: `com.apple.developer.arkit.camera-region.allow`


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraregionanchor)*