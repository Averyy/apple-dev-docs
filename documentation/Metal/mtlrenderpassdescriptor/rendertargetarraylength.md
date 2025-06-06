# renderTargetArrayLength

**Framework**: Metal  
**Kind**: property

The number of active layers that all attachments must have for layered rendering.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
var renderTargetArrayLength: Int { get set }
```

## Mentions

- [Rendering to Multiple Texture Slices in a Draw Command](rendering-to-multiple-texture-slices-in-a-draw-command.md)

#### Discussion

The default value is `0`, indicating that the GPU does not use layered rendering on this render pass.

The table below gives typical values you might set, depending on the type of texture being used as attachments in the render pass. Your vertex shader must select the render target array index between `0` and the array length minus `1`.

| Texture Type | Typical Length |
| --- | --- |
| [`MTLTextureType.type1DArray`](mtltexturetype/type1darray.md) or [`MTLTextureType.type2DArray`](mtltexturetype/type2darray.md) | The length of the texture array ([`arrayLength`](mtltexture/arraylength.md)) |
| [`MTLTextureType.typeCube`](mtltexturetype/typecube.md) | 6 |
| [`MTLTextureType.typeCubeArray`](mtltexturetype/typecubearray.md) | 6 times the length of the texture array ([`arrayLength`](mtltexture/arraylength.md)) |

## See Also

- [var renderTargetWidth: Int](mtlrenderpassdescriptor/rendertargetwidth.md)
  The width, in pixels, to constrain the render target to.
- [var renderTargetHeight: Int](mtlrenderpassdescriptor/rendertargetheight.md)
  The height, in pixels, to constrain the render target to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor/rendertargetarraylength)*