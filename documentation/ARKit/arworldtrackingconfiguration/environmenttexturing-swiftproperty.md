# environmentTexturing

**Framework**: ARKit  
**Kind**: property

An option that determines how the framework generates environment textures.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var environmentTexturing: ARWorldTrackingConfiguration.EnvironmentTexturing { get set }
```

#### Discussion

Environment textures are cube-map textures that depict the view in all directions from a specific point in a scene. In 3D asset rendering, environment textures are the basis for image-based lighting algorithms where surfaces can realistically reflect light from their surroundings. ARKit generates environment textures during an AR session using camera imagery, allowing SceneKit or a custom-rendering engine to provide realistic image-based lighting for virtual objects in your AR experience.

To enable texture map generation for your configuration, change this property (from its default value of [`ARWorldTrackingConfiguration.EnvironmentTexturing.none`](arworldtrackingconfiguration/environmenttexturing-swift.enum/none.md)):

- With [`ARWorldTrackingConfiguration.EnvironmentTexturing.manual`](arworldtrackingconfiguration/environmenttexturing-swift.enum/manual.md) environment texturing, you identify points in the scene for which you want light probe texture maps by creating [`AREnvironmentProbeAnchor`](arenvironmentprobeanchor.md) objects and adding them to the session.
- With [`ARWorldTrackingConfiguration.EnvironmentTexturing.automatic`](arworldtrackingconfiguration/environmenttexturing-swift.enum/automatic.md) environment texturing, ARKit automatically creates, positions, and adds [`AREnvironmentProbeAnchor`](arenvironmentprobeanchor.md) objects to the session.

In both cases, ARKit automatically generates environment textures as the session collects camera imagery. Use a delegate method such as [`session(_:didUpdate:)`](arsessiondelegate/session(_:didupdate:)-3qtt8.md) to find out when a texture is available, and access it from the anchor’s [`environmentTexture`](arenvironmentprobeanchor/environmenttexture.md) property.

If you display AR content using [`ARSCNView`](arscnview.md) and the [`automaticallyUpdatesLighting`](arscnview/automaticallyupdateslighting.md) option, SceneKit automatically retrieves [`AREnvironmentProbeAnchor`](arenvironmentprobeanchor.md) texture maps and uses them to light the scene.

## See Also

- [ARWorldTrackingConfiguration.EnvironmentTexturing](arworldtrackingconfiguration/environmenttexturing-swift.enum.md)
  The available environment texturing options for world tracking.
- [class AREnvironmentProbeAnchor](arenvironmentprobeanchor.md)
  An object that provides environmental lighting information for a specific area of space in a world-tracking AR session.
- [var wantsHDREnvironmentTextures: Bool](arworldtrackingconfiguration/wantshdrenvironmenttextures.md)
  A flag that instructs the framework to create environment textures in HDR format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/environmenttexturing-swift.property)*