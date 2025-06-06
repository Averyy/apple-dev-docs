# MTLReadWriteTextureTier.tier2

**Framework**: Metal  
**Kind**: case

Tier 2 read/write textures are supported.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case tier2
```

#### Discussion

Read/write texture tier 2 supports the following pixel formats in addition to those supported by [`MTLReadWriteTextureTier.tier1`](mtlreadwritetexturetier/tier1.md):

- [`MTLPixelFormat.rgba32Float`](mtlpixelformat/rgba32float.md)
- [`MTLPixelFormat.rgba32Uint`](mtlpixelformat/rgba32uint.md)
- [`MTLPixelFormat.rgba32Sint`](mtlpixelformat/rgba32sint.md)
- [`MTLPixelFormat.rgba16Float`](mtlpixelformat/rgba16float.md)
- [`MTLPixelFormat.rgba16Uint`](mtlpixelformat/rgba16uint.md)
- [`MTLPixelFormat.rgba16Sint`](mtlpixelformat/rgba16sint.md)
- [`MTLPixelFormat.rgba8Unorm`](mtlpixelformat/rgba8unorm.md)
- [`MTLPixelFormat.rgba8Uint`](mtlpixelformat/rgba8uint.md)
- [`MTLPixelFormat.rgba8Sint`](mtlpixelformat/rgba8sint.md)
- [`MTLPixelFormat.r16Float`](mtlpixelformat/r16float.md)
- [`MTLPixelFormat.r16Uint`](mtlpixelformat/r16uint.md)
- [`MTLPixelFormat.r16Sint`](mtlpixelformat/r16sint.md)
- [`MTLPixelFormat.r8Unorm`](mtlpixelformat/r8unorm.md)
- [`MTLPixelFormat.r8Uint`](mtlpixelformat/r8uint.md)
- [`MTLPixelFormat.r8Sint`](mtlpixelformat/r8sint.md)

## See Also

- [MTLReadWriteTextureTier.tier1](mtlreadwritetexturetier/tier1.md)
  Tier 1 read/write textures are supported.
- [MTLReadWriteTextureTier.tierNone](mtlreadwritetexturetier/tiernone.md)
  Read-write textures are not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlreadwritetexturetier/tier2)*