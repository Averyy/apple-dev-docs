# init(color:texture:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a color of emitted light in macOS.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(color: NSColor = .black, texture: CustomMaterial.Texture? = nil)
```

**Other overloads**:

```swift
init(color: UIColor = .black, texture: CustomMaterial.Texture? = nil)
```

## Parameters

- `color`: The color of the emitted light. Defaults to black.
- `texture`: An optional UV-mapped image texture.

## See Also

### Creating an emissive color object
- [init(PhysicallyBasedMaterial.EmissiveColor)](./init%28_%29.md)
  Creates a color of emitted light based on the emissive color property from a physically based material.
- [init(color: UIColor, texture: CustomMaterial.Texture?)](./init%28color,texture%29-81kgh.md)
  Creates a color of emitted light in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/emissivecolor-swift.struct/init(color:texture:)-xkh3)*