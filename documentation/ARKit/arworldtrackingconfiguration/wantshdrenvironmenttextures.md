# wantsHDREnvironmentTextures

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A flag that instructs the framework to create environment textures in HDR format.

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

If you set [`environmentTexturing`](./environmenttexturing-swift.property.md) to `.automatic` in iOS 12 or later, ARKit gives you environment textures you cast on your app’s virtual content to create realistic reflections. By default, the framework sets [`wantsHDREnvironmentTextures`](./wantshdrenvironmenttextures.md) to [`true`](../../Swift/true.md). When your renderer supports HDR environment textures in iOS 13, it enables your lighting engine to output more colors, with a more realistic result.

![Screenshot showing low and high dynamic range environment textures in a side by side comparison.](https://developer.apple.com/tutorials/images/com.apple.arkit/media-3231020@2x.png)

Both [`ARView`](../../RealityKit/arview.md) and [`ARSCNView`](../arscnview.md) support HDR environment textures. For more information, see [Adding realistic reflections to an AR experience](../adding-realistic-reflections-to-an-ar-experience.md).

For a Metal app that doesn’t yet support HDR environment textures, you can use the following code to receive LDR environment textures until you’re ready to update your renderer for HDR.

```swift
if #available(iOS 13, *) { 
    configuration.wantsHDREnvironmentTextures = false
}
```

## See Also

### Creating Realistic Reflections
- [var environmentTexturing: ARWorldTrackingConfiguration.EnvironmentTexturing](./environmenttexturing-swift.property.md)
  An option that determines how the framework generates environment textures.
- [ARWorldTrackingConfiguration.EnvironmentTexturing](./environmenttexturing-swift.enum.md)
  The available environment texturing options for world tracking.
- [class AREnvironmentProbeAnchor](../arenvironmentprobeanchor.md)
  An object that provides environmental lighting information for a specific area of space in a world-tracking AR session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration/wantshdrenvironmenttextures)*