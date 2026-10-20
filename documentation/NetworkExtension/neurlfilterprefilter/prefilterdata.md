# NEURLFilterPrefilter.PrefilterData

**Framework**: Network Extension  
**Kind**: enum  
**Role**: Enumeration

An enumeration that represents Bloom filter data, as used by a prefilter.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
enum PrefilterData
```

## Topics

### Accessing prefilter data
- [NEURLFilterPrefilter.PrefilterData.smallFilter(_:)](./prefilterdata/smallfilter%28_%29.md)
  A prefilter data enumeration case that contains the prefilter data as the associated value.
- [NEURLFilterPrefilter.PrefilterData.temporaryFilepath(_:)](./prefilterdata/temporaryfilepath%28_%29.md)
  A prefilter data enumeration case that contains a temporary file path to the prefilter data as the associated value.

## See Also

### Working with prefilter properties
- [let data: NEURLFilterPrefilter.PrefilterData](./data.md)
  The Bloom filter data.
- [let tag: String](./tag.md)
  The tag of the Bloom filter data, such as the SHA-256 hash of the Bloom filter data.
- [let bitCount: Int](./bitcount.md)
  The number of bits in the Bloom filter.
- [let hashCount: Int](./hashcount.md)
  The number of hashes for the Bloom filter.
- [let murmurSeed: UInt32](./murmurseed.md)
  The seed used for the hashing function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfilterprefilter/prefilterdata)*