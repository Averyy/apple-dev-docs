# init(color:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates an unlit material with the given base color.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(color: NSColor)
```

**Other overloads**:

```swift
init(color: UIColor)
```

#### Discussion

> **Note**: The blending mode of `UnlitMaterial` materials should be configured explicitly with the [`blending`](./blending-swift.property.md) property for transparent or translucent surfaces.  The `opaque` mode is used when unset.

## Parameters

- `color`: The base color for the new material.

## See Also

### Creating an unlit material
- [init()](./init%28%29.md)
  Creates an unlit material.
- [init(applyPostProcessToneMap: Bool)](./init%28applypostprocesstonemap%29.md)
  Creates an UnlitMaterial with the given tone mapping setting
- [init(color: NSColor, applyPostProcessToneMap: Bool)](./init%28color,applypostprocesstonemap%29-899er.md)
  Creates an UnlitMaterial with the given color and tone mapping setting
- [init(program: UnlitMaterial.Program)](./init%28program%29.md)
- [init(texture: TextureResource)](./init%28texture%29.md)
  Creates a new unlit material with the provided color texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/unlitmaterial/init(color:)-8xgq2)*