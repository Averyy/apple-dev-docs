# wantsHDREnvironmentTextures

**Framework**: ARKit  
**Kind**: property

A flag that instructs ARKit to create environment textures in HDR format.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var wantsHDREnvironmentTextures: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/Swift/true). If your renderer supports HDR environment textures, this feature effects more realistic reflections.

![Screenshot showing low and high dynamic range environment textures in a side by side comparison.](https://docs-assets.developer.apple.com/published/ad953b8a0aa6dd1314efee5175eab5df/media-3281347%402x.png)

RealityKit and SceneKit both support HDR environment textures. For more information, see [`Adding realistic reflections to an AR experience`](adding-realistic-reflections-to-an-ar-experience.md).

## See Also

- [var environmentTexturing: ARWorldTrackingConfiguration.EnvironmentTexturing](arbodytrackingconfiguration/environmenttexturing.md)
  The behavior ARKit uses for generating environment textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arbodytrackingconfiguration/wantshdrenvironmenttextures)*