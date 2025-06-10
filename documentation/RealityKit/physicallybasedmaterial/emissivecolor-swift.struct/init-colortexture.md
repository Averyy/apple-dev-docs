# init(color:texture:)

**Framework**: RealityKit  
**Kind**: init

Creates a color of emitted light in iOS.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
init(color: NSColor = .black, texture: MaterialParameters.Texture? = nil)
```

#### Discussion

This initializer creates an object from a color, an image texture, or from both. The `color` property defaults to black, which results in no light emissions. With custom materials, `color` and `texture` are available as inputs in your surface shader, but your surface shader must call `params.surface().set_emissive_color()`, otherwise RealityKit renders no light emission.

The following Metal code demonstrates how to replicate the emissive behavior of [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) in your surface shader code:

```swift
    // Retrieve the emissive color tint from the CustomMaterial.
    half3 emissiveColorTint = (half3)params.material_constants()
                              .emissive_color_tint();

    // Retrieve the primary texture coordinates.
    float2 uv = params.geometry().uv0();

    // Flip the UV coordinate’s y-axis. You only need to do this
    // for models you load from USDZ or .reality files.
    uv.y = 1.0 - uv.y;

    auto tex = params.textures();
    half3 color = (half3)tex.emissive_color()
                  .sample(textureSampler, uv).rgb;

    // Multiply the tint and the sampled value from the texture,
    // and assign the result to the shader's emissive color
    // property.
    color *= emissiveColorTint;
    params.surface().set_emissive_color(color);
```

> **Note**: Unlike [`PhysicallyBasedMaterial`](physicallybasedmaterial.md), [`CustomMaterial`](custommaterial.md) has no [`emissiveIntensity`](physicallybasedmaterial/emissiveintensity.md) value. If you need to pass an emissive intensity value to your surface shader, use the [`custom`](custommaterial/custom-swift.property.md) property or another unused attribute property.

## Parameters

- `color`: The color of the emitted light. Defaults to black.
- `texture`: An optional UV-mapped image texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/emissivecolor-swift.struct/init(color:texture:))*