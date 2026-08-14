# wantsHDREnvironmentTextures

**Framework**: ARKit  
**Kind**: property

A flag that instructs ARKit to create environment textures in HDR format.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var wantsHDREnvironmentTextures: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/swift/true). If your renderer supports HDR environment textures, this feature effects more realistic reflections.

![Screenshot showing low and high dynamic range environment textures in a side by side comparison.](/images/com.apple.arkit/media-3281347@2x.png)

RealityKit and SceneKit both support HDR environment textures. For more information, see [`Adding realistic reflections to an AR experience`](adding-realistic-reflections-to-an-ar-experience.md).

## See Also

- [var environmentTexturing: ARWorldTrackingConfiguration.EnvironmentTexturing](arbodytrackingconfiguration/environmenttexturing.md)
  The behavior ARKit uses for generating environment textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arbodytrackingconfiguration/wantshdrenvironmenttextures)*