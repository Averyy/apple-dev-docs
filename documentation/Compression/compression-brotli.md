# COMPRESSION_BROTLI

**Framework**: Compression  
**Kind**: var

The Brotli compression algorithm, which is recommended for text compression.

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
var COMPRESSION_BROTLI: compression_algorithm { get }
```

#### Discussion

The Brotli compression algorithm is a widely adopted content encoding method for the web. The Compression framework includes Brotli to provide decoding capabilities.

The Compression framework implements the Brotli level 2 encoder only. This compression level provides a good balance between compression speed and compression ratio. The Brotli decoder supports decoding data compressed with any compression level.

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
- [var COMPRESSION_LZBITMAP: compression_algorithm](compression_lzbitmap.md)
  The LZBITMAP compression algorithm, which is designed to exploit the vector instruction set of current CPUs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_brotli)*