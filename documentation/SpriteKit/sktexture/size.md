# size()

**Framework**: SpriteKit  
**Kind**: method

Gets the size of the texture.

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
func size() -> CGSize
```

## Mentions

- [Loading and Using Textures](loading-and-using-textures.md)

#### Return Value

The dimensions of the texture, measured in points.

#### Discussion

If the texture was created using an image file and that image file hasn’t been loaded, calling this method forces the texture data to be loaded from the file.

## See Also

- [func textureRect() -> CGRect](sktexture/texturerect.md)
  Gets a rectangle that defines the portion of the texture used to render its image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sktexture/size())*