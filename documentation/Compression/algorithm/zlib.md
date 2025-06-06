# Algorithm.zlib

**Framework**: Compression  
**Kind**: case

The zlib compression algorithm, which is recommended for cross-platform compression.

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
case zlib
```

#### Discussion

The Compression library implements the zlib encoder at level 5 only.  This compression level provides a good balance between compression speed and compression ratio.  The zlib decoder supports decoding data compressed with any compression level.

The encoded format is the raw `DEFLATE` format as described in [`IETF RFC 1951`](https://developer.apple.comhttps://www.ietf.org/rfc/rfc1951.txt), the following obtains the equivalent configuration of the encoder:

```c
deflateInit2(zstream,5,Z_DEFLATED,-15,8,Z_DEFAULT_STRATEGY)
```

## See Also

- [var COMPRESSION_ZLIB: compression_algorithm](compression_zlib.md)
  The zlib compression algorithm, which is recommended for cross-platform compression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/algorithm/zlib)*