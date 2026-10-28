# texture(at:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns the texture bound at the given index, or `nil` if the slot is unset.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func texture(at index: Int) -> LowLevelTextureResource?
```

## Return Value

The texture resource at `index`, or `nil` if the slot is unoccupied.

## Parameters

- `index`: The slot index within the argument table’s texture array.

## See Also

### Accessing textures
- [func setTexture(LowLevelTextureResource, at: Int) throws(LowLevelRenderContextError)](./settexture%28_,at%29.md)
  Binds a texture to the slot at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelargumenttable/texture(at:))*