# ARWorldTrackingConfiguration.EnvironmentTexturing.manual

**Framework**: ARKit  
**Kind**: case

The framework generates environment textures only for probe anchors you explicitly add to the session.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case manual
```

#### Discussion

When you use this [`environmentTexturing`](arworldtrackingconfiguration/environmenttexturing-swift.property.md) option, you must manually choose when and where to generate environment map textures:

1. Create an [`AREnvironmentProbeAnchor`](arenvironmentprobeanchor.md) object with a `transform` indicating its position in the scene.
2. Add the probe anchor to the session with the [`add(anchor:)`](arsession/add(anchor:).md) method.

If you display AR content using [`ARSCNView`](arscnview.md), SceneKit automatically retrieves texture maps from probe anchors and uses them to light the scene. Otherwise, use a delegate method such as [`session(_:didUpdate:)`](arsessiondelegate/session(_:didupdate:)-3qtt8.md) to find out when the probe anchor’s texture has been updated and access the [`environmentTexture`](arenvironmentprobeanchor/environmenttexture.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/environmenttexturing-swift.enum/manual)*