# MTLPixelFormat.rgb32Uint

**Framework**: Metal  
**Kind**: case

An ordinary format with three components of 32-bit unsigned integer values in RGB order.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case rgb32Uint
```

#### Discussion

The order of the color components in this format are red, green and blue.

You can apply this format to a texture you create only with an [`MTLTextureDescriptor`](mtltexturedescriptor.md) instance with all of the following property configurations:

- The [`usage`](mtltexturedescriptor/usage.md) property can’t include the [`shaderWrite`](mtltextureusage/shaderwrite.md) option.
- The [`textureType`](mtltexturedescriptor/texturetype.md) property needs to be equal to [`MTLTextureType.typeTextureBuffer`](mtltexturetype/typetexturebuffer.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpixelformat/rgb32uint)*