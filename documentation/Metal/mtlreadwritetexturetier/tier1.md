# MTLReadWriteTextureTier.tier1

**Framework**: Metal  
**Kind**: case

Indicates the system supports tier 1 read-write textures.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case tier1
```

#### Discussion

Tier 1 read-write textures support the following pixel formats:

- [`MTLPixelFormat.r32Float`](mtlpixelformat/r32float.md)
- [`MTLPixelFormat.r32Uint`](mtlpixelformat/r32uint.md)
- [`MTLPixelFormat.r32Sint`](mtlpixelformat/r32sint.md)

## See Also

- [MTLReadWriteTextureTier.tier2](mtlreadwritetexturetier/tier2.md)
  Indicates the system supports tier 2 read-write textures.
- [MTLReadWriteTextureTier.tierNone](mtlreadwritetexturetier/tiernone.md)
  Indicates the system doesn’t support read-write textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlreadwritetexturetier/tier1)*