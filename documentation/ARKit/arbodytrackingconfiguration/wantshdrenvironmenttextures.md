# wantsHDREnvironmentTextures

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A flag that instructs ARKit to create environment textures in HDR format.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
var wantsHDREnvironmentTextures: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL wantsHDREnvironmentTextures;
```

## Discussion

The default value is [`true`](../../Swift/true.md). If your renderer supports HDR environment textures, this feature effects more realistic reflections.

![Screenshot showing low and high dynamic range environment textures in a side by side comparison.](https://developer.apple.com/tutorials/images/com.apple.arkit/media-3281347@2x.png)

RealityKit and SceneKit both support HDR environment textures. For more information, see [Adding realistic reflections to an AR experience](../adding-realistic-reflections-to-an-ar-experience.md).

## See Also

### Adding Realistic Reflections
- [var environmentTexturing: ARWorldTrackingConfiguration.EnvironmentTexturing](./environmenttexturing.md)
  The behavior ARKit uses for generating environment textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arbodytrackingconfiguration/wantshdrenvironmenttextures)*