# Algorithm.lzma

**Framework**: Compression  
**Kind**: case

The LZMA compression algorithm, which is recommended for high-compression ratio.

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
case lzma
```

#### Discussion

The Compression library implements the LZMA encoder at level 6 only.  This is the default compression level for open source LZMA, and provides excellent compression.  The LZMA decoder supports decoding data compressed with any compression level.

## See Also

- [var COMPRESSION_LZMA: compression_algorithm](compression_lzma.md)
  The LZMA compression algorithm, which is recommended for high-compression ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/algorithm/lzma)*