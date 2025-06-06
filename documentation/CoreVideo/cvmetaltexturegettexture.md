# CVMetalTextureGetTexture(_:)

**Framework**: Core Video  
**Kind**: func

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

#### Return Value

The [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture) object corresponding to the image buffer.

## Parameters

- `image`: A CoreVideo Metal texture-based image buffer.

## See Also

- [func CVMetalTextureGetCleanTexCoords(CVMetalTexture, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>)](cvmetaltexturegetcleantexcoords(_:_:_:_:_:).md)
  Returns convenient normalized texture coordinates for the part of the image that should be displayed.
- [func CVMetalTextureIsFlipped(CVMetalTexture) -> Bool](cvmetaltextureisflipped(_:).md)
  Returns a Boolean value indicating whether the texture image is vertically flipped.
- [func CVMetalTextureGetTypeID() -> CFTypeID](cvmetaltexturegettypeid().md)
  Returns the Core Foundation type identifier for a CoreVideo Metal texture-based image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetaltexturegettexture(_:))*