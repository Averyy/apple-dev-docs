# ARWorldTrackingConfiguration.EnvironmentTexturing.automatic

**Framework**: ARKit  
**Kind**: case

The framework automatically determines when and where to generate environment textures.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case automatic
```

#### Discussion

When you use this [`environmentTexturing`](arworldtrackingconfiguration/environmenttexturing-swift.property.md) option, ARKit automatically chooses positions in the scene to generate environment textures based on the camera imagery it has collected and the other anchors you’ve placed.

If you display AR content using [`ARSCNView`](arscnview.md), SceneKit automatically retrieves texture maps from probe anchors and uses them to light the scene. Otherwise, use a delegate method such as [`session(_:didUpdate:)`](arsessiondelegate/session(_:didupdate:)-3qtt8.md) to find out when the probe anchor’s texture has been updated and access the [`environmentTexture`](arenvironmentprobeanchor/environmenttexture.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/environmenttexturing-swift.enum/automatic)*