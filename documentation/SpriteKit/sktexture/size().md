# size()

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Gets the size of the texture.

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
func size() -> CGSize
```

```objc
- (CGSize) size;
```

## Mentions

- [Loading and Using Textures](../loading-and-using-textures.md)

#### Return Value

The dimensions of the texture, measured in points.

#### Discussion

If the texture was created using an image file and that image file hasn’t been loaded, calling this method forces the texture data to be loaded from the file.

## See Also

### Reading a Texture’s Size and Optional Source Location
- [func textureRect() -> CGRect](./texturerect%28%29.md)
  Gets a rectangle that defines the portion of the texture used to render its image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/size())*