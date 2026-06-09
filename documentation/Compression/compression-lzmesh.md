# COMPRESSION_LZMESH

**Framework**: Compression  
**Kind**: var

The LZMESH compression algorithm, which is recommended for fast, general-purpose compression on Apple platforms.

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
var COMPRESSION_LZMESH: compression_algorithm { get }
```

#### Discussion

LZMESH is the Apple general-purpose compression algorithm, designed to replace both [`COMPRESSION_LZFSE`](compression_lzfse.md) and [`COMPRESSION_ZLIB`](compression_zlib.md) across Apple platforms. It combines LZ77 with length-limited Huffman coding and a lazy match parser to deliver better compression ratio than both [`COMPRESSION_LZFSE`](compression_lzfse.md) and [`COMPRESSION_ZLIB`](compression_zlib.md) while encoding significantly faster than either. LZMESH decodes 3.5x faster than [`COMPRESSION_ZLIB`](compression_zlib.md) on Apple silicon.

An LZMESH-encoded buffer is a sequence of blocks terminated by an end-of-stream marker. There are three block types:

- **Raw block**: A header followed by uncompressed bytes. The encoder emits raw blocks when the data is incompressible, so the output is never significantly larger than the input.
- **Compressed block**: A header followed by LZMESH-encoded data. Each block can represent up to 4 GB of uncompressed content.
- **End-of-stream block**: A single-byte marker that terminates the stream.

Each compressed block includes a footer that records block encoding parameters. Both headers and footers reserve flag bits for future format extensions.

LZMESH is available through the buffer API only — [`compression_encode_buffer(_:_:_:_:_:_:)`](compression_encode_buffer(_:_:_:_:_:_:).md) and [`compression_decode_buffer(_:_:_:_:_:_:)`](compression_decode_buffer(_:_:_:_:_:_:).md).

The decoder requires only 64 KB of scratch memory, making it well suited for memory-constrained environments.

> **Note**: The `COMPRESSION_LZMESH` algorithm is available in version 27 or later of Apple operating systems.

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
- [var COMPRESSION_LZRAVEN: compression_algorithm](compression_lzraven.md)
  The LZRAVEN compression algorithm, which is recommended for high-compression ratio with fast decoding on Apple platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_lzmesh)*