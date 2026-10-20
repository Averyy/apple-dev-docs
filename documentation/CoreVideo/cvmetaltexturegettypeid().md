# CVMetalTextureGetTypeID()

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns the Core Foundation type identifier for a CoreVideo Metal texture-based image buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CVMetalTextureGetTypeID() -> CFTypeID
```

```c
extern CFTypeID CVMetalTextureGetTypeID();
```

#### Return Value

The Core Foundation type identifier for the `CVMetalTextureRef` type.

## See Also

### Related Documentation
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
- [Metal](../Metal/Metal.md)
  Render advanced 3D graphics and compute data in parallel with graphics processors.
### Inspecting Textures
- [func CVMetalTextureGetTexture(CVMetalTexture) -> (any MTLTexture)?](./cvmetaltexturegettexture%28_%29.md)
  Returns the Metal texture object for the image buffer.
- [func CVMetalTextureGetCleanTexCoords(CVMetalTexture, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>, UnsafeMutablePointer<Float>)](./cvmetaltexturegetcleantexcoords%28_,_,_,_,_%29.md)
  Returns convenient normalized texture coordinates for the part of the image that should be displayed.
- [func CVMetalTextureIsFlipped(CVMetalTexture) -> Bool](./cvmetaltextureisflipped%28_%29.md)
  Returns a Boolean value indicating whether the texture image is vertically flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmetaltexturegettypeid())*