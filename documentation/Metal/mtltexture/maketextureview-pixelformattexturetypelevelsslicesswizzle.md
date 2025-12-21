# makeTextureView(pixelFormat:textureType:levels:slices:swizzle:)

**Framework**: Metal  
**Kind**: method

Creates a new view of the texture, reinterpreting a subset of its data using a different type, pixel format, and swizzle pattern.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
func makeTextureView(pixelFormat: MTLPixelFormat, textureType: MTLTextureType, levels levelRange: Range<Int>, slices sliceRange: Range<Int>, swizzle: MTLTextureSwizzleChannels) -> (any MTLTexture)?
```

#### Discussion

For more information on texture views, see [`makeTextureView(pixelFormat:textureType:levels:slices:)`](mtltexture/maketextureview(pixelformat:texturetype:levels:slices:).md)

The swizzle pattern of the view is combined with that of the parent texture to generate the final swizzle pattern. For example: An `[R,G,A,B]` swizzle of a texture with a `[R,1,1,G]` swizzle pattern is `[R,1,G,1]`.

## Parameters

- `pixelFormat`: A new pixel format, which needs to be compatible with the original pixel format.
- `textureType`: A new texture type.
- `levelRange`: A new base level range that restricts which mipmap levels are visible in the new texture.
- `sliceRange`: A new base slice range that restricts which array slices are visible in the new texture.
- `swizzle`: The swizzle pattern the GPU uses to reorder the data when sampling or reading the texture.

## See Also

- [func makeTextureView(pixelFormat: MTLPixelFormat) -> (any MTLTexture)?](mtltexture/maketextureview(pixelformat:).md)
  Creates a new view of the texture, reinterpreting its data using a different pixel format.
- [func makeTextureView(pixelFormat: MTLPixelFormat, textureType: MTLTextureType, levels: Range<Int>, slices: Range<Int>) -> (any MTLTexture)?](mtltexture/maketextureview(pixelformat:texturetype:levels:slices:).md)
  Creates a new view of the texture, reinterpreting a subset of its data using a different type and pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexture/maketextureview(pixelformat:texturetype:levels:slices:swizzle:))*