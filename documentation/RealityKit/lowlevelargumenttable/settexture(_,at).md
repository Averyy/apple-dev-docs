# setTexture(_:at:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Binds a texture to the slot at the given index.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func setTexture(_ texture: LowLevelTextureResource, at index: Int) throws(LowLevelRenderContextError)
```

## Discussion

> **Throws**: [`LowLevelRenderContextError`](../lowlevelrendercontexterror.md) if `index` is out of range or `texture` is incompatible with the slot.

## Parameters

- `texture`: The texture resource to bind to the slot.
- `index`: The slot index within the argument table’s texture array.

## See Also

### Accessing textures
- [func texture(at: Int) -> LowLevelTextureResource?](./texture%28at%29.md)
  Returns the texture bound at the given index, or `nil` if the slot is unset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelargumenttable/settexture(_:at:))*