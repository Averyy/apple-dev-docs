# NSBitmapImageRep.LoadStatus.readingHeader

**Framework**: AppKit  
**Kind**: case

The image format is known, but not enough data has been read to determine the size, depth, etc., of the image. You should continue to provide more data.

**Availability**:
- macOS ?+

## Declaration

```swift
case readingHeader
```

## See Also

- [NSBitmapImageRep.LoadStatus.unknownType](nsbitmapimagerep/loadstatus/unknowntype.md)
  Not enough data to determine image format. You should continue to provide more data.
- [NSBitmapImageRep.LoadStatus.willNeedAllData](nsbitmapimagerep/loadstatus/willneedalldata.md)
  Incremental loading cannot be supported.
- [NSBitmapImageRep.LoadStatus.invalidData](nsbitmapimagerep/loadstatus/invaliddata.md)
  An error occurred during image decompression. The image contains the portions of the data that have already been successfully decompressed, if any
- [NSBitmapImageRep.LoadStatus.unexpectedEOF](nsbitmapimagerep/loadstatus/unexpectedeof.md)
  [`incrementalLoad(from:complete:)`](nsbitmapimagerep/incrementalload(from:complete:).md) was called with [`true`](https://developer.apple.com/documentation/swift/true), but not enough data was available for decompression. The image contains the portions of the data that have already been successfully decompressed, if any.
- [NSBitmapImageRep.LoadStatus.completed](nsbitmapimagerep/loadstatus/completed.md)
  Enough data has been provided to successfully decompress the image (regardless of the complete: flag).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/loadstatus/readingheader)*