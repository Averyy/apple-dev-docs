# textureRect()

**Framework**: SpriteKit  
**Kind**: method

Gets a rectangle that defines the portion of the texture used to render its image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func textureRect() -> CGRect
```

#### Return Value

A rectangle in the unit coordinate space.

#### Discussion

The default value is a rectangle that covers the entire texture `(0,0)` - `(1,1)`. You cannot set this value directly; to use only a portion of a texture, use the [`init(rect:in:)`](sktexture/init(rect:in:).md) method to create a new texture.

## See Also

- [func size() -> CGSize](sktexture/size.md)
  Gets the size of the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/texturerect())*