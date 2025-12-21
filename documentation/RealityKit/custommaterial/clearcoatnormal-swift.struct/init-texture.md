# init(texture:)

**Framework**: RealityKit  
**Kind**: init

Construct a `CustomMaterial.ClearcoatNormal` object from a texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+

## Declaration

```swift
init(texture: CustomMaterial.Texture? = nil)
```

#### Discussion

```swift
if let textureResource = try? TextureResource.load(named: "entity_cc_normalMap") {
    let ccNormalMap = CustomMaterial.Texture(textureResource)
    let clearcoatNormal = CustomMaterial.ClearcoatNormal(texture: ccNormalMap)
}
```

## Parameters

- `texture`: The clearcoat normals as the texture of a UV-mapped image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/clearcoatnormal-swift.struct/init(texture:))*