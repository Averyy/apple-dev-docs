# COMPRESSION_LZ4

**Framework**: Compression  
**Kind**: var

The LZ4 compression algorithm for fast compression.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var COMPRESSION_LZ4: compression_algorithm { get }
```

#### Discussion

LZ4 is a high-performance compressor. The encoded format that the Compression library produces and consumes is compatible with the open source version, apart from the addition of a very simple frame to the raw stream to enable additional validation and functionality.

An LZ4-encoded buffer is a sequence of blocks, each beginning with a header. Use the following header descriptions when wrapping another LZ4 encoder (or decoder) to enable it to produce or consume the same data stream:

- A compressed block header consists of the octets `0x62`, `0x76`, `0x34`, and `0x31`. Following that is the size (in bytes) of the decoded (plaintext) data the block represents, and the size (in bytes) of the encoded data stored in the block. The header stores both sizes as (potentially unaligned) 32-bit little-endian values. The actual LZ4-encoded data stream immediately follows the compressed block header.
- An uncompressed block header consists of the octets `0x62`, `0x76`, `0x34`, and `0x2d`. Following that is a single 32-bit little-endian value representing the plaintext data’s size (in bytes), and then the plaintext data itself.
- An end of stream block header consists of the octets `0x62`, `0x76`, `0x34`, and `0x24` and identifies the end of the LZ4 frame.  Don’t attempt to read or write data beyond this header.

If you’re implementing a wrapper for a raw LZ4 decoder, keep in mind that a compressed block may refer to data from the previous block, so the (decoded) previous block must be available to the decoder.

## See Also

- [var COMPRESSION_LZFSE: compression_algorithm](compression_lzfse.md)
  The LZFSE compression algorithm, which is recommended for use on Apple platforms.
- [var COMPRESSION_LZ4_RAW: compression_algorithm](compression_lz4_raw.md)
  The LZ4 compression algorithm, without frame headers.
- [var COMPRESSION_LZMA: compression_algorithm](compression_lzma.md)
  The LZMA compression algorithm, which is recommended for high-compression ratio.
- [var COMPRESSION_ZLIB: compression_algorithm](compression_zlib.md)
  The zlib compression algorithm, which is recommended for cross-platform compression.
- [var COMPRESSION_BROTLI: compression_algorithm](compression_brotli.md)
  The Brotli compression algorithm, which is recommended for text compression.
- [var COMPRESSION_LZBITMAP: compression_algorithm](compression_lzbitmap.md)
  The LZBITMAP compression algorithm, which is designed to exploit the vector instruction set of current CPUs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_lz4)*