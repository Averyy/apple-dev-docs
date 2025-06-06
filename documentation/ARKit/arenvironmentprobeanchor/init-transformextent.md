# init(transform:extent:)

**Framework**: ARKit  
**Kind**: init

Creates a new environment probe anchor.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(transform: simd_float4x4, extent: simd_float3)
```

#### Discussion

Use the [`add(anchor:)`](arsession/add(anchor:).md) method to begin tracking your custom anchor in an AR session. After you add an environment probe anchor to the scene, ARKit begins generating environment textures for it. To be notified when the anchor has a new [`environmentTexture`](arenvironmentprobeanchor/environmenttexture.md), implement the [`session(_:didUpdate:)`](arsessiondelegate/session(_:didupdate:)-3qtt8.md), [`renderer(_:didUpdate:for:)`](arscnviewdelegate/renderer(_:didupdate:for:).md), or [`view(_:didUpdate:for:)`](arskviewdelegate/view(_:didupdate:for:).md) delegate method.

## Parameters

- `transform`: A matrix that encodes the position, orientation, and scale of the anchor, relative to the world coordinate space of the AR session in which you place the anchor.
- `extent`: World coordinate space in ARKit always follows a right-handed convention, but is oriented based on the session configuration. For details, see  .

## See Also

- [init(name: String, transform: simd_float4x4, extent: simd_float3)](arenvironmentprobeanchor/init(name:transform:extent:).md)
  Creates a new anchor object with a descriptive name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arenvironmentprobeanchor/init(transform:extent:))*