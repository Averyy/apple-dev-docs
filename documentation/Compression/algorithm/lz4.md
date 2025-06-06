# Algorithm.lz4

**Framework**: Compression  
**Kind**: case

The LZ4 compression algorithm, which is recommended for fast compression.

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
case lz4
```

#### Discussion

LZ4 is a high-performance compressor. The encoded format that the Compression library produces and consumes is compatible with the open source version, apart from the addition of a very simple frame to the raw stream to allow some additional validation and functionality.

An LZ4-encoded buffer is a sequence of blocks, each of which begins with a header. The following description of the headers is provided so that you can wrap another LZ4 encoder or decoder to produce or consume the same data stream:

- A compressed block header consists of the octets `0x62`, `0x76`, `0x34`, and `0x31`, followed by the size in bytes of the decoded (plaintext) data represented by the block and the size (in bytes) of the encoded data stored in the block.  The headers stores both size fields as (possibly unaligned) 32-bit little-endian values. The actual LZ4-encoded data stream immediately follows the compressed block header.
- An uncompressed block header consists of the octets `0x62`, `0x76`, `0x34`, and `0x2d`, followed by two sizes: the number of bytes of the decoded (plaintext) data represented by the block and the number of bytes of the encoded data stored in the block.
- An end of stream block header consists of the octets `0x62`, `0x76`, `0x34`, and `0x24` and marks the end of the LZ4 frame.  Do not read or write any further data beyond this header.

If you are implementing a wrapper for a raw LZ4 decoder, keep in mind that a compressed block may refer to data from the previous block, so the (decoded) previous block must be available to the decoder.

## See Also

- [var COMPRESSION_LZ4: compression_algorithm](compression_lz4.md)
  The LZ4 compression algorithm for fast compression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/algorithm/lz4)*