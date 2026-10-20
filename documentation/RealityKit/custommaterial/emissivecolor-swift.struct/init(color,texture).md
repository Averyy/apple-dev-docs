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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/emissivecolor-swift.struct/init(color:texture:))*