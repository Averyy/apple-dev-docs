# CVMetalTextureGetTexture(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns the Metal texture object for the image buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CVMetalTextureGetTexture(_ image: CVMetalTexture) -> (any MTLTexture)?
```

```c
extern id<MTLTexture>CVMetalTextureGetTexture(CVMetalTextureRef image);
```

## Return Value

The [`MTLTexture`](../Metal/mtltexture.md) object corresponding to the image buffer.

## Parameters

- `image`: A CoreVideo Metal texture-based image buffer.

## See Also

### Inspecting Textures
- [func CVMetalTextureGetCleanTexCoords(CVMetalTexture, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>)](./cvmetaltexturegetcleantexcoords%28_,_,_,_,_%29.md)
  Returns convenient normalized texture coordinates for the part of the image that should be displayed.
- [func CVMetalTextureIsFlipped(CVMetalTexture) -> Bool](./cvmetaltextureisflipped%28_%29.md)
  Returns a Boolean value indicating whether the texture image is vertically flipped.
- [func CVMetalTextureGetTypeID() -> CFTypeID](./cvmetaltexturegettypeid%28%29.md)
  Returns the Core Foundation type identifier for a CoreVideo Metal texture-based image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetaltexturegettexture(_:))*