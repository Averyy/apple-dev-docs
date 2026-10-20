# CVMetalTextureIsFlipped(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns a Boolean value indicating whether the texture image is vertically flipped.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CVMetalTextureIsFlipped(_ image: CVMetalTexture) -> Bool
```

```c
extern Boolean CVMetalTextureIsFlipped(CVMetalTextureRef image);
```

#### Return Value

If `True`, the texture coordinate `{0,0}` represents the upper left of the texture; if `False`, the texture coordinate `{0,0}` represents the lower left of the texture.

## Parameters

- `image`: A CoreVideo Metal texture-based image buffer.

## See Also

### Inspecting Textures
- [func CVMetalTextureGetTexture(CVMetalTexture) -> (any MTLTexture)?](./cvmetaltexturegettexture%28_%29.md)
  Returns the Metal texture object for the image buffer.
- [func CVMetalTextureGetCleanTexCoords(CVMetalTexture, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>)](./cvmetaltexturegetcleantexcoords%28_,_,_,_,_%29.md)
  Returns convenient normalized texture coordinates for the part of the image that should be displayed.
- [func CVMetalTextureGetTypeID() -> CFTypeID](./cvmetaltexturegettypeid%28%29.md)
  Returns the Core Foundation type identifier for a CoreVideo Metal texture-based image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetaltextureisflipped(_:))*