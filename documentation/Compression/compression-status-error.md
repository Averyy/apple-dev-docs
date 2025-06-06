# COMPRESSION_STATUS_ERROR

**Framework**: Compression  
**Kind**: var

Indicates an error with stream compression.

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
var COMPRESSION_STATUS_ERROR: compression_status { get }
```

#### Discussion

If there’s an error with stream compression or decompression, for example if the encoded data is corrupted, [`compression_stream_process(_:_:)`](compression_stream_process(_:_:).md) returns [`COMPRESSION_STATUS_ERROR`](compression_status_error.md).

## See Also

- [var COMPRESSION_STATUS_OK: compression_status](compression_status_ok.md)
  Indicates the stream has consumed all data in the source buffer, or used all space in the destination buffer.
- [var COMPRESSION_STATUS_END: compression_status](compression_status_end.md)
  Indicates the stream has read all input from the source, and written all output to the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_status_error)*