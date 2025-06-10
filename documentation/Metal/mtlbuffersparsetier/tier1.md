# MTLBufferSparseTier.tier1

**Framework**: Metal  
**Kind**: case

Indicates support for sparse buffers tier 1.

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

Tier 1 sparse buffers allow the following:

- Partial memory backing at sparse page granularity.
- Defined behavior for accessing an  buffer range.

An unbacked buffer range indicates a range within the buffer that doesn’t have memory backing at a given point in time. Accessing an unbacked buffer range of a sparse buffer produces the following results:

- Reading return zero.
- Writing produces no result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlbuffersparsetier/tier1)*