# init(transform:extent:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Creates a new environment probe anchor.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
init(transform: simd_float4x4, extent: simd_float3)
```

```objc
- (instancetype) initWithTransform:(simd_float4x4) transform extent:(simd_float3) extent;
```

## Discussion

Use the [`add(anchor:)`](../arsession/add%28anchor%29.md) method to begin tracking your custom anchor in an AR session. After you add an environment probe anchor to the scene, ARKit begins generating environment textures for it. To be notified when the anchor has a new [`environmentTexture`](./environmenttexture.md), implement the [`session(_:didUpdate:)`](../arsessiondelegate/session%28_,didupdate%29-3qtt8.md), [`renderer(_:didUpdate:for:)`](../arscnviewdelegate/renderer%28_,didupdate,for%29.md), or [`view(_:didUpdate:for:)`](../arskviewdelegate/view%28_,didupdate,for%29.md) delegate method.

## Parameters

- `transform`: A matrix that encodes the position, orientation, and scale of the anchor, relative to the world coordinate space of the AR session in which you place the anchor.
- `extent`: The extent (of *bounds*) of the probe anchor.

  World coordinate space in ARKit always follows a right-handed convention, but is oriented based on the session configuration. For details, see [Understanding World Tracking](../understanding-world-tracking.md).

## See Also

### Creating Probe Anchors
- [init(name: String, transform: simd_float4x4, extent: simd_float3)](./init%28name,transform,extent%29.md)
  Creates a new anchor object with a descriptive name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arenvironmentprobeanchor/init(transform:extent:))*