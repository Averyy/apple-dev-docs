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

LZFSE is Apple’s proprietary compression algorithm, matching the compression ratio of zlib level 5, but with much higher energy efficiency and speed (between 2x and 3x) for both encode and decode operations.

Use LZFSE when compressing a payload for iOS, macOS, watchOS, and tvOS. If you need to compress a payload for another platform (for example, Linux or Windows), use LZ4, LZMA, or zlib.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_lzfse)*