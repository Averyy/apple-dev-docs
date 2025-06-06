# init(color:texture:)

**Framework**: RealityKit  
**Kind**: init

Creates a color of emitted light in macOS.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
init(color: UIColor = .black, texture: CustomMaterial.Texture? = nil)
```

## Parameters

- `color`: The color of the emitted light. Defaults to black.
- `texture`: An optional UV-mapped image texture.

## See Also

- [init(PhysicallyBasedMaterial.EmissiveColor)](custommaterial/emissivecolor-swift.struct/init(_:).md)
  Creates a color of emitted light based on the emissive color property from a physically based material.
- [init(color: NSColor, texture: CustomMaterial.Texture?)](custommaterial/emissivecolor-swift.struct/init(color:texture:)-xkh3.md)
  Creates a color of emitted light in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/emissivecolor-swift.struct/init(color:texture:)-81kgh)*