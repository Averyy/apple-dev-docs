# setTexture(_:at:)

**Framework**: RealityKit  
**Kind**: method

Binds a texture to the slot at the given index.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func setTexture(_ texture: LowLevelTextureResource, at index: Int) throws(LowLevelRenderContextError)
```

#### Discussion

> **Note**: [`LowLevelRenderContextError`](lowlevelrendercontexterror.md) if `index` is out of range or `texture` is incompatible with the slot.

## Parameters

- `texture`: The texture resource to bind to the slot.
- `index`: The slot index within the argument table’s texture array.

## See Also

- [func texture(at: Int) -> LowLevelTextureResource?](lowlevelargumenttable/texture(at:).md)
  Returns the texture bound at the given index, or `nil` if the slot is unset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelargumenttable/settexture(_:at:))*