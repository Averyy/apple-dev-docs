# init(name:transform:extent:)

**Framework**: ARKit  
**Kind**: init

Creates a new anchor object with a descriptive name.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(name: String, transform: simd_float4x4, extent: simd_float3)
```

#### Discussion

Use the [`add(anchor:)`](arsession/add(anchor:).md) method to begin tracking your custom anchor in an AR session. After you add an environment probe anchor to the scene, ARKit begins generating environment textures for it. To be notified when the anchor has a new [`environmentTexture`](arenvironmentprobeanchor/environmenttexture.md), implement the [`session(_:didUpdate:)`](arsessiondelegate/session(_:didupdate:)-3qtt8.md), [`renderer(_:didUpdate:for:)`](arscnviewdelegate/renderer(_:didupdate:for:).md), or [`view(_:didUpdate:for:)`](arskviewdelegate/view(_:didupdate:for:).md) delegate method.

## Parameters

- `name`: A descriptive name for the anchor. ARKit doesn’t display the name to users, but your app can use it to identify anchors for debugging.
- `transform`: World coordinate space in ARKit always follows a right-handed convention, but is oriented based on the session configuration. For details, see  .
- `extent`: An environment probe anchor may have an infinite extent, which indicates that its texture is a global lighting environment, or a finite extent, which indicates that its texture represents the local lighting conditions in a specific area of the scene.

## See Also

- [init(transform: simd_float4x4, extent: simd_float3)](arenvironmentprobeanchor/init(transform:extent:).md)
  Creates a new environment probe anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arenvironmentprobeanchor/init(name:transform:extent:))*