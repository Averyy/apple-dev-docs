# textureRect()

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Gets a rectangle that defines the portion of the texture used to render its image.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func textureRect() -> CGRect
```

```objc
- (CGRect) textureRect;
```

#### Return Value

A rectangle in the unit coordinate space.

#### Discussion

The default value is a rectangle that covers the entire texture `(0,0)` - `(1,1)`. You cannot set this value directly; to use only a portion of a texture, use the [`init(rect:in:)`](./init%28rect,in%29.md) method to create a new texture.

## See Also

### Reading a Texture’s Size and Optional Source Location
- [func size() -> CGSize](./size%28%29.md)
  Gets the size of the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/texturerect())*