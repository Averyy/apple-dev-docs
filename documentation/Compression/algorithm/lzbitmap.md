# Algorithm.lzbitmap

**Framework**: Compression  
**Kind**: case

The LZBITMAP compression algorithm, which is designed to exploit the vector instruction set of current CPUs.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
case lzbitmap
```

#### Discussion

The LZBITMAP compression algorithm provides compression ratios as close as possible to [`COMPRESSION_ZLIB`](compression_zlib.md) and [`COMPRESSION_LZFSE`](compression_lzfse.md), with a lower compression cost. This compression algorithm is available only for the Compression buffer API functions, [`compression_encode_buffer(_:_:_:_:_:_:)`](compression_encode_buffer(_:_:_:_:_:_:).md) and [`compression_decode_buffer(_:_:_:_:_:_:)`](compression_decode_buffer(_:_:_:_:_:_:).md).

[`COMPRESSION_LZBITMAP`](compression_lzbitmap.md) is available only on Apple devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/algorithm/lzbitmap)*