# extent

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The area around the anchor’s position that contains the texture.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
var extent: simd_float3 { get }
```

```objc
@property (nonatomic, readonly) simd_float3 extent;
```

## Discussion

Rendering reflective objects may involve projecting the [`environmentTexture`](./environmenttexture.md) onto a proxy geometry centered on the anchor’s position, then sampling from the projected texture.

An environment probe anchor may have an infinite extent, which indicates that its texture is a global lighting environment, or a finite extent, which indicates that its texture represents the local lighting conditions in a specific area of the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arenvironmentprobeanchor/extent)*