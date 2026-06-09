# COMPRESSION_LZFSE

**Framework**: Compression  
**Kind**: var

The LZFSE compression algorithm, which is recommended for use on Apple platforms.

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
var COMPRESSION_LZFSE: compression_algorithm { get }
```

#### Discussion

LZFSE is the Apple proprietary, general-purpose compression algorithm. It pairs an LZ77-style match finder with Finite State Entropy (FSE, a variant of tabled Asymmetric Numeral Systems) to encode literals and match metadata, which lets it match the compression ratio of [`COMPRESSION_ZLIB`](compression_zlib.md) (zlib level 5) while running 2x to 3x faster for both encoding and decoding. LZFSE is also substantially more energy-efficient than [`COMPRESSION_ZLIB`](compression_zlib.md), which makes it a good default for mobile and battery-powered devices.

LZFSE sits at a balanced point in the speed-ratio tradeoff: it compresses better than [`COMPRESSION_LZ4`](compression_lz4.md) and runs faster than [`COMPRESSION_ZLIB`](compression_zlib.md) or [`COMPRESSION_LZMA`](compression_lzma.md), but doesn’t match the ratio of [`COMPRESSION_LZMA`](compression_lzma.md) or the raw throughput of [`COMPRESSION_LZ4`](compression_lz4.md). For new Apple-only code, prefer [`COMPRESSION_LZMESH`](compression_lzmesh.md) — it typically compresses a bit better than LZFSE, encodes significantly faster, and decodes slightly faster.

If a payload needs to be decoded on another platform such as Linux or Windows, use [`COMPRESSION_LZ4`](compression_lz4.md), [`COMPRESSION_LZMA`](compression_lzma.md), or [`COMPRESSION_ZLIB`](compression_zlib.md) instead. Apple does publish an open-source LZFSE reference implementation, but it isn’t as widely available as [`COMPRESSION_ZLIB`](compression_zlib.md) or [`COMPRESSION_LZMA`](compression_lzma.md).

LZFSE is supported by both the buffer API — [`compression_encode_buffer(_:_:_:_:_:_:)`](compression_encode_buffer(_:_:_:_:_:_:).md) and [`compression_decode_buffer(_:_:_:_:_:_:)`](compression_decode_buffer(_:_:_:_:_:_:).md) — and the streaming API via [`compression_stream_init(_:_:_:)`](compression_stream_init(_:_:_:).md), so you can use it for in-memory payloads or for processing data incrementally as it arrives.

## See Also

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
- [var COMPRESSION_LZRAVEN: compression_algorithm](compression_lzraven.md)
  The LZRAVEN compression algorithm, which is recommended for high-compression ratio with fast decoding on Apple platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_lzfse)*