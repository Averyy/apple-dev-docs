# wantsHDREnvironmentTextures

**Framework**: ARKit  
**Kind**: property

A flag that instructs the framework to create environment textures in HDR format.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var wantsHDREnvironmentTextures: Bool { get set }
```

#### Discussion

If you set [`environmentTexturing`](arworldtrackingconfiguration/environmenttexturing-swift.property.md) to `.automatic` in iOS 12 or later, ARKit gives you environment textures you cast on your app’s virtual content to create realistic reflections. By default, the framework sets [`wantsHDREnvironmentTextures`](arworldtrackingconfiguration/wantshdrenvironmenttextures.md) to [`true`](https://developer.apple.com/documentation/swift/true). When your renderer supports HDR environment textures in iOS 13, it enables your lighting engine to output more colors, with a more realistic result.

![Screenshot showing low and high dynamic range environment textures in a side by side comparison.](https://docs-assets.developer.apple.com/published/ad953b8a0aa6dd1314efee5175eab5df/media-3231020%402x.png)

Both [`ARView`](https://developer.apple.com/documentation/RealityKit/ARView) and [`ARSCNView`](arscnview.md) support HDR environment textures. For more information, see [`Adding realistic reflections to an AR experience`](adding-realistic-reflections-to-an-ar-experience.md).

For a Metal app that doesn’t yet support HDR environment textures, you can use the following code to receive LDR environment textures until you’re ready to update your renderer for HDR.

```swift
if #available(iOS 13, *) { 
    configuration.wantsHDREnvironmentTextures = false
}
```

## See Also

- [var environmentTexturing: ARWorldTrackingConfiguration.EnvironmentTexturing](arworldtrackingconfiguration/environmenttexturing-swift.property.md)
  An option that determines how the framework generates environment textures.
- [ARWorldTrackingConfiguration.EnvironmentTexturing](arworldtrackingconfiguration/environmenttexturing-swift.enum.md)
  The available environment texturing options for world tracking.
- [class AREnvironmentProbeAnchor](arenvironmentprobeanchor.md)
  An object that provides environmental lighting information for a specific area of space in a world-tracking AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/wantshdrenvironmenttextures)*