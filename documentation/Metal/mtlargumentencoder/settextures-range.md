# setTextures(_:range:)

**Framework**: Metal  
**Kind**: method

Encodes references to an array of textures into the argument buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst ?+
- macOS 10.13+
- tvOS 11.0+
- visionOS ?+

## Declaration

```swift
func setTextures(_ textures: [(any MTLTexture)?], range: Range<Int>)
```

## Parameters

- `textures`: An array of textures the method encodes.
- `range`: A range of indices within the argument buffer for each element in  .   The values correspond to either the index IDs of declarations in   Metal Shading Language (MSL) or the   property   of   instances.

## See Also

- [func setTexture((any MTLTexture)?, index: Int)](mtlargumentencoder/settexture(_:index:).md)
  Encodes a reference to a texture into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/settextures(_:range:))*