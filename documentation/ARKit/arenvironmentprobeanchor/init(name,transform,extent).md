# init(name:transform:extent:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Creates a new anchor object with a descriptive name.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
init(name: String, transform: simd_float4x4, extent: simd_float3)
```

```objc
- (instancetype) initWithName:(NSString *) name transform:(simd_float4x4) transform extent:(simd_float3) extent;
```

## Discussion

Use the [`add(anchor:)`](../arsession/add%28anchor%29.md) method to begin tracking your custom anchor in an AR session. After you add an environment probe anchor to the scene, ARKit begins generating environment textures for it. To be notified when the anchor has a new [`environmentTexture`](./environmenttexture.md), implement the [`session(_:didUpdate:)`](../arsessiondelegate/session%28_,didupdate%29-3qtt8.md), [`renderer(_:didUpdate:for:)`](../arscnviewdelegate/renderer%28_,didupdate,for%29.md), or [`view(_:didUpdate:for:)`](../arskviewdelegate/view%28_,didupdate,for%29.md) delegate method.

## Parameters

- `name`: A descriptive name for the anchor. ARKit doesn’t display the name to users, but your app can use it to identify anchors for debugging.
- `transform`: A matrix that encodes the position, orientation, and scale of the anchor, relative to the world coordinate space of the AR session in which you place the anchor.

  World coordinate space in ARKit always follows a right-handed convention, but is oriented based on the session configuration. For details, see [Understanding World Tracking](../understanding-world-tracking.md).
- `extent`: The area around the anchor’s position that contains the textrure.

  An environment probe anchor may have an infinite extent, which indicates that its texture is a global lighting environment, or a finite extent, which indicates that its texture represents the local lighting conditions in a specific area of the scene.

## See Also

### Creating Probe Anchors
- [init(transform: simd_float4x4, extent: simd_float3)](./init%28transform,extent%29.md)
  Creates a new environment probe anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arenvironmentprobeanchor/init(name:transform:extent:))*