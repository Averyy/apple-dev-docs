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

Brotli is a general-purpose compression algorithm standardized as IETF RFC 7932. It combines an LZ77-style match finder with Huffman coding and second-order context modeling, and ships with a built-in static dictionary of roughly 120 KB of common web-oriented strings — HTML tags, CSS keywords, JavaScript tokens, and common English words. That dictionary is what makes Brotli particularly effective on short HTTP responses and small text fragments, where conventional LZ77-based algorithms have too little history to build up a strong dictionary of their own.

Brotli is the compression used by HTTP’s `Content-Encoding: br`, and it’s also the basis of the WOFF2 web font format. Including Brotli in the Compression framework lets your app decode data produced by these pipelines directly, for example, responses served with `br` encoding or WOFF2 font payloads, without pulling in a third-party dependency.

The Compression framework implements the Brotli level 2 encoder only. Brotli defines compression levels 0 through 11: higher levels spend substantially more CPU on match finding and modeling to squeeze out a better ratio, while lower levels prioritize speed. Level 2 is a good balance between compression speed and compression ratio and matches the typical use case for on-device encoding. If you need a higher compression ratio — for example, when pre-compressing static web assets at build time — use a higher-level Brotli encoder outside the Compression framework. The Brotli decoder in the Compression framework supports decoding data compressed at any level, so you can always decode assets produced with levels 0 through 11.

Compared to [`COMPRESSION_ZLIB`](compression_zlib.md) at similar settings, Brotli typically achieves a noticeably better compression ratio on textual and web-like content thanks to its static dictionary and richer modeling, which is why it has largely displaced gzip for serving static web assets. For binary payloads or content that doesn’t resemble web data, the gap narrows and the Apple-native algorithms ([`COMPRESSION_LZFSE`](compression_lzfse.md) or [`COMPRESSION_LZMA`](compression_lzma.md)) may perform better for the use case.

Because Brotli’s output format is the standard one defined in RFC 7932, any conforming Brotli implementation on any platform can decode the buffers produced by the Compression framework; there’s no Apple-specific frame wrapped around the raw stream.

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
- [var COMPRESSION_LZMESH: compression_algorithm](compression_lzmesh.md)
  The LZMESH compression algorithm, which is recommended for fast, general-purpose compression on Apple platforms.
- [var COMPRESSION_LZRAVEN: compression_algorithm](compression_lzraven.md)
  The LZRAVEN compression algorithm, which is recommended for high-compression ratio with fast decoding on Apple platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_brotli)*