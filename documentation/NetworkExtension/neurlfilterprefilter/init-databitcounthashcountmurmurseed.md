# init(data:bitCount:hashCount:murmurSeed:)

**Framework**: Network Extension  
**Kind**: init

Initializes a new prefilter with the given parameters.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
init(data: NEURLFilterPrefilter.PrefilterData, bitCount: Int, hashCount: Int, murmurSeed: UInt32)
```

## Parameters

- `data`: The Bloom filter data, as a   instance.
- `bitCount`: The number of bits in the Bloom filter.
- `hashCount`: The number of hashes for the Bloom filter.
- `murmurSeed`: The seed used for the MurmurHash3 function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfilterprefilter/init(data:bitcount:hashcount:murmurseed:))*