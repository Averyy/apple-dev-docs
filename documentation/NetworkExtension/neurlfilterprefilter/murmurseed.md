# murmurSeed

**Framework**: Network Extension  
**Kind**: property

The seed used for the hashing function.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
let murmurSeed: UInt32
```

#### Discussion

The prefilter uses the MurmurHash3 function.

## See Also

- [let data: NEURLFilterPrefilter.PrefilterData](neurlfilterprefilter/data.md)
  The Bloom filter data.
- [NEURLFilterPrefilter.PrefilterData](neurlfilterprefilter/prefilterdata.md)
  An enumeration that represents Bloom filter data, as used by a prefilter.
- [let tag: String](neurlfilterprefilter/tag.md)
  The tag of the Bloom filter data, such as the SHA-256 hash of the Bloom filter data.
- [let bitCount: Int](neurlfilterprefilter/bitcount.md)
  The number of bits in the Bloom filter.
- [let hashCount: Int](neurlfilterprefilter/hashcount.md)
  The number of hashes for the Bloom filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfilterprefilter/murmurseed)*