# CVMetalTextureIsFlipped(_:)

**Framework**: Core Video  
**Kind**: func

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

#### Return Value

If `True`, the texture coordinate `{0,0}` represents the upper left of the texture; if `False`, the texture coordinate `{0,0}` represents the lower left of the texture.

## Parameters

- `image`: A CoreVideo Metal texture-based image buffer.

## See Also

- [func CVMetalTextureGetTexture(CVMetalTexture) -> (any MTLTexture)?](cvmetaltexturegettexture(_:).md)
  Returns the Metal texture object for the image buffer.
- [func CVMetalTextureGetCleanTexCoords(CVMetalTexture, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>)](cvmetaltexturegetcleantexcoords(_:_:_:_:_:).md)
  Returns convenient normalized texture coordinates for the part of the image that should be displayed.
- [func CVMetalTextureGetTypeID() -> CFTypeID](cvmetaltexturegettypeid().md)
  Returns the Core Foundation type identifier for a CoreVideo Metal texture-based image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetaltextureisflipped(_:))*