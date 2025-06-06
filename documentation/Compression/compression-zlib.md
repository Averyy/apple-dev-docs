# COMPRESSION_ZLIB

**Framework**: Compression  
**Kind**: var

The zlib compression algorithm, which is recommended for cross-platform compression.

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
var COMPRESSION_ZLIB: compression_algorithm { get }
```

#### Discussion

The Compression library implements the zlib encoder at level 5 only.  This compression level provides a good balance between compression speed and compression ratio.  The zlib decoder supports decoding data compressed with any compression level.

The encoded format is the raw `DEFLATE` format as described in [`IETF RFC 1951`](https://developer.apple.comhttps://www.ietf.org/rfc/rfc1951.txt), the following obtains the equivalent configuration of the encoder:

```c
deflateInit2(zstream,5,Z_DEFLATED,-15,8,Z_DEFAULT_STRATEGY)
```

## See Also

- [var COMPRESSION_LZFSE: compression_algorithm](compression_lzfse.md)
  The LZFSE compression algorithm, which is recommended for use on Apple platforms.
- [var COMPRESSION_LZ4: compression_algorithm](compression_lz4.md)
  The LZ4 compression algorithm for fast compression.
- [var COMPRESSION_LZ4_RAW: compression_algorithm](compression_lz4_raw.md)
  The LZ4 compression algorithm, without frame headers.
- [var COMPRESSION_LZMA: compression_algorithm](compression_lzma.md)
  The LZMA compression algorithm, which is recommended for high-compression ratio.
- [var COMPRESSION_BROTLI: compression_algorithm](compression_brotli.md)
  The Brotli compression algorithm, which is recommended for text compression.
- [var COMPRESSION_LZBITMAP: compression_algorithm](compression_lzbitmap.md)
  The LZBITMAP compression algorithm, which is designed to exploit the vector instruction set of current CPUs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_zlib)*