# NEURLFilterPrefilter

**Framework**: Network Extension  
**Kind**: struct

A structure containing a prefilter returned by a filter control provider.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
struct NEURLFilterPrefilter
```

#### Overview

You return this type from the [`fetchPrefilter(existingPrefilterTag:)`](neurlfiltercontrolprovider/fetchprefilter(existingprefiltertag:).md) method of [`NEURLFilterControlProvider`](neurlfiltercontrolprovider.md). The returned `NEURLFilterPrefilter` must contain a Bloom filter built with the 32-bit FNV-1a and 32-bit MurmurHash3 hash functions, with double hashing. Depending on the size of the Bloom filter data, it can be passed as data or the path of a file containing the data.

## Topics

### Creating a prefilter
- [init(data: NEURLFilterPrefilter.PrefilterData, tag: String, bitCount: Int, hashCount: Int, murmurSeed: UInt32)](neurlfilterprefilter/init(data:tag:bitcount:hashcount:murmurseed:).md)
  Initializes a new prefilter with the given parameters.
### Working with prefilter properties
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
- [let murmurSeed: UInt32](neurlfilterprefilter/murmurseed.md)
  The seed used for the hashing function.

## See Also

- [func fetchPrefilter(existingPrefilterTag: String?) async throws -> NEURLFilterPrefilter?](neurlfiltercontrolprovider/fetchprefilter(existingprefiltertag:).md)
  Fetches prefilter data, in response to a call from the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfilterprefilter)*