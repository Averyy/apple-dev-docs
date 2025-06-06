# opacityThreshold

**Framework**: RealityKit  
**Kind**: property

The minimum opacity value to treat as fully opaque.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
var opacityThreshold: Float? { get set }
```

#### Discussion

In a custom material, `opacityThreshold` helps define how RealityKit renders transparency when using a texture (known as an ) to control opacity. This property is available as an input to the material’s surface shader, but RealityKit doesn’t automatically use this value to render your entity. To render an entity transparent, call `params.surface().set_opacity()` from the surface shader.

When `opacityThreshold` is set, [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) uses the opacity texture as a mask. RealityKit discards pixels with opacity values less than the `opacityThreshold`, and renders opacity values greater than or equal to `opacityThreshold` fully opaque.

The following Metal code replicates the behavior of the [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) shaders:

```cpp
// Retrieve the threshold from the CustomMaterial.
float opacityThreshold = params.material_constants().opacity_threshold();

// Retrieve the entity's texture coordinates.
float2 uv = params.geometry().uv0();

// Entities loaded from USDZ or .reality files use texture coordinates with
// a flipped y-axis. This adjusts for that.
uv.y = 1.0 - uv.y;

// Retrieve the opacity texture from the material.
auto tex = params.textures();

// Sample the value from the opacity texture.
half opacity = tex.opacity().sample(textureSampler, uv).r;

// When the opacity threshold is used, set the opacity to either
// 1.0 or 0.0 depending on the value of the opacity threshold for
// the masking behavior.
opacity = (opacity <= opacityThreshold) ? 0.0 : 1.0;

// Use the calculated value to set the opacity for rendering.
params.surface().set_opacity(opacity);
```

## See Also

- [var blending: CustomMaterial.Blending](custommaterial/blending-swift.property.md)
  The transparency of an entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/opacitythreshold)*