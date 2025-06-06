# CVMetalTextureGetCleanTexCoords(_:_:_:_:_:)

**Framework**: Core Video  
**Kind**: func

Returns convenient normalized texture coordinates for the part of the image that should be displayed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CVMetalTextureGetCleanTexCoords(_ image: CVMetalTexture, _ lowerLeft: UnsafeMutablePointer<Float>, _ lowerRight: UnsafeMutablePointer<Float>, _ upperRight: UnsafeMutablePointer<Float>, _ upperLeft: UnsafeMutablePointer<Float>)
```

#### Discussion

This function automatically takes into account whether or not the texture is flipped.

## Parameters

- `image`: A CoreVideo Metal texture-based image buffer.

## See Also

- [func CVMetalTextureGetTexture(CVMetalTexture) -> (any MTLTexture)?](cvmetaltexturegettexture(_:).md)
  Returns the Metal texture object for the image buffer.
- [func CVMetalTextureIsFlipped(CVMetalTexture) -> Bool](cvmetaltextureisflipped(_:).md)
  Returns a Boolean value indicating whether the texture image is vertically flipped.
- [func CVMetalTextureGetTypeID() -> CFTypeID](cvmetaltexturegettypeid().md)
  Returns the Core Foundation type identifier for a CoreVideo Metal texture-based image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetaltexturegetcleantexcoords(_:_:_:_:_:))*