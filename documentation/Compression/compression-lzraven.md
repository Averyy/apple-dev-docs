# COMPRESSION_LZRAVEN

**Framework**: Compression  
**Kind**: var

The LZRAVEN compression algorithm, which is recommended for high-compression ratio with fast decoding on Apple platforms.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS ?+
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var COMPRESSION_LZRAVEN: compression_algorithm { get }
```

#### Discussion

LZRAVEN is the Apple high-compression algorithm, designed to replace [`COMPRESSION_LZMA`](compression_lzma.md) across Apple platforms. It combines LZ77 with modern entropy coding, adaptive context-sensitive modeling, and near-optimal parsing to often achieve a slightly better compression ratio than [`COMPRESSION_LZMA`](compression_lzma.md). LZRAVEN uses an 8 MB dictionary and encodes faster than [`COMPRESSION_LZMA`](compression_lzma.md) while decoding 3x faster on Apple silicon, where the decoder leverages vector units to process multiple symbols per operation.

An LZRAVEN-encoded buffer begins with a stream header that encodes global encoder parameters, defines the quantized size of the LZ dictionary, and provides reserved feature flags for future extensions. The stream header is followed by a sequence of compressed or uncompressed blocks that are terminated by an empty block.

Each block begins with a header that encodes the block’s compressed size and feature flags. A block can be either compressed or stored uncompressed when compression would provide no benefit. LZRAVEN is practical for latency-sensitive workloads where [`COMPRESSION_LZMA`](compression_lzma.md) decode speed would be prohibitive.

LZRAVEN is available through the buffer API only — [`compression_encode_buffer(_:_:_:_:_:_:)`](compression_encode_buffer(_:_:_:_:_:_:).md) and [`compression_decode_buffer(_:_:_:_:_:_:)`](compression_decode_buffer(_:_:_:_:_:_:).md).

The decoder requires approximately 36 KB of scratch memory, making it well suited for memory-constrained environments.

> **Note**: The `COMPRESSION_LZRAVEN` algorithm is available in version 27 or later of Apple operating systems.

## See Also

- [var COMPRESSION_LZFSE: compression_algorithm](compression_lzfse.md)
  The LZFSE compression algorithm, which is recommended for use on Apple platforms.
- [var COMPRESSION_LZ4: compression_algorithm](compression_lz4.md)
  The LZ4 compression algorithm for fast compression.
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
- [var COMPRESSION_LZMESH: compression_algorithm](compression_lzmesh.md)
  The LZMESH compression algorithm, which is recommended for fast, general-purpose compression on Apple platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_lzraven)*