# setTexture(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a reference to a texture into the argument buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setTexture(_ texture: (any MTLTexture)?, index: Int)
```

## Parameters

- `texture`: A texture the method encodes.
- `index`: The index of a texture within the argument buffer.   The value corresponds to either the index ID of a declaration in   Metal Shading Language (MSL) or the   property of   an   instance.

## See Also

- [func setTextures([(any MTLTexture)?], range: Range<Int>)](mtlargumentencoder/settextures(_:range:).md)
  Encodes references to an array of textures into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/settexture(_:index:))*