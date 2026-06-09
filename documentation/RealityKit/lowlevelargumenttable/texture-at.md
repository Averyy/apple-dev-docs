# texture(at:)

**Framework**: RealityKit  
**Kind**: method

Returns the texture bound at the given index, or `nil` if the slot is unset.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func texture(at index: Int) -> LowLevelTextureResource?
```

#### Return Value

The texture resource at `index`, or `nil` if the slot is unoccupied.

## Parameters

- `index`: The slot index within the argument table’s texture array.

## See Also

- [func setTexture(LowLevelTextureResource, at: Int) throws(LowLevelRenderContextError)](lowlevelargumenttable/settexture(_:at:).md)
  Binds a texture to the slot at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelargumenttable/texture(at:))*