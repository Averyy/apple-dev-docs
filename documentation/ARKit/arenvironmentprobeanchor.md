# AREnvironmentProbeAnchor

**Framework**: ARKit  
**Kind**: class

An object that provides environmental lighting information for a specific area of space in a world-tracking AR session.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class AREnvironmentProbeAnchor
```

#### Overview

Environment textures depict the view in all directions from a specific point in a scene. In 3D asset rendering, environment textures are the basis for image-based lighting algorithms where surfaces can realistically reflect light from their surroundings. ARKit can generate environment textures during an AR session using camera imagery, allowing SceneKit or a custom-rendering engine to provide realistic image-based lighting for virtual objects in your AR experience.

To enable texture map generation for an AR session, set the [`environmentTexturing`](arworldtrackingconfiguration/environmenttexturing-swift.property.md) property:

- With [`ARWorldTrackingConfiguration.EnvironmentTexturing.manual`](arworldtrackingconfiguration/environmenttexturing-swift.enum/manual.md) environment texturing, you identify points in the scene for which you want light probe texture maps by creating [`AREnvironmentProbeAnchor`](arenvironmentprobeanchor.md) objects and adding them to the session.
- With [`ARWorldTrackingConfiguration.EnvironmentTexturing.automatic`](arworldtrackingconfiguration/environmenttexturing-swift.enum/automatic.md) environment texturing, ARKit automatically creates, positions, and adds [`AREnvironmentProbeAnchor`](arenvironmentprobeanchor.md) objects to the session.

In both cases, ARKit automatically generates environment textures as the session collects camera imagery. Use a delegate method such as [`session(_:didUpdate:)`](arsessiondelegate/session(_:didupdate:)-3qtt8.md) to find out when a texture is available, and access it from the anchor’s [`environmentTexture`](arenvironmentprobeanchor/environmenttexture.md) property.

If you display AR content using [`ARSCNView`](arscnview.md) and the [`automaticallyUpdatesLighting`](arscnview/automaticallyupdateslighting.md) option, SceneKit automatically retrieves [`AREnvironmentProbeAnchor`](arenvironmentprobeanchor.md) texture maps and uses them to light the scene.

## Topics

### Creating Probe Anchors
- [init(transform: simd_float4x4, extent: simd_float3)](arenvironmentprobeanchor/init(transform:extent:).md)
  Creates a new environment probe anchor.
- [init(name: String, transform: simd_float4x4, extent: simd_float3)](arenvironmentprobeanchor/init(name:transform:extent:).md)
  Creates a new anchor object with a descriptive name.
### Accessing Texture Maps
- [var environmentTexture: (any MTLTexture)?](arenvironmentprobeanchor/environmenttexture.md)
  A cube-map texture that represents the view in all directions from the probe anchor’s position.
### Examining a Probe Anchor
- [var extent: simd_float3](arenvironmentprobeanchor/extent.md)
  The area around the anchor’s position that contains the texture.

## Relationships

### Inherits From
- [ARAnchor](aranchor.md)
### Conforms To
- [ARAnchorCopying](aranchorcopying.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Adding realistic reflections to an AR experience](adding-realistic-reflections-to-an-ar-experience.md)
  Use ARKit to generate environment probe textures from camera imagery and render reflective virtual objects.
- [class ARLightEstimate](arlightestimate.md)
  Estimated scene lighting information associated with a captured video frame in an AR session.
- [class ARDirectionalLightEstimate](ardirectionallightestimate.md)
  Estimated environmental lighting information associated with a captured video frame in a face-tracking AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arenvironmentprobeanchor)*