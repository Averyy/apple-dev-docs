# setObjectTexture(_:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Assigns a texture to an entry in the object shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setObjectTexture(_ texture: (any MTLTexture)?, index: Int)
```

```objc
- (void) setObjectTexture:(id<MTLTexture>) texture atIndex:(NSUInteger) index;
```

#### Discussion

By default, the texture at each index is `nil`.

## Parameters

- `texture`: An [`MTLTexture`](../mtltexture.md) instance the command assigns to an entry in the object shader argument table for textures.
- `index`: An integer that represents the entry in the object shader argument table for textures that stores a record of `texture`.

## See Also

### Assigning textures for object shaders
- [func setObjectTextures([(any MTLTexture)?], range: Range<Int>)](./setobjecttextures%28_,range%29.md)
  Assigns multiple textures to a range of entries in the object shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjecttexture(_:index:))*