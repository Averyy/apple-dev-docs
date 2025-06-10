# MTLTextureSparseTier.tier1

**Framework**: Metal  
**Kind**: case

Indicates support for sparse textures tier 1.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
case tier1
```

#### Discussion

Tier 1 sparse textures allow the following:

- Partial memory backing at sparse tile granularity.
- Defined behavior for accessing an unbacked texture region.
- Shader feedback on texture access to determine memory backing.

An unbacked texture region indicates a region within the texture that doesn’t have memory backing at a given point in time. Accessing an unbacked texture region produces the following results:

- Reading returns zero (transparent black) for pixel formats with an alpha (A) channel.
- Reading return zero in RGB and one in alpha (A) channels (opaque black) otherwise.
- Writing produces no result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltexturesparsetier/tier1)*