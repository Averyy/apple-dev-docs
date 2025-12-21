# NSBitmapImageRep.LoadStatus.completed

**Framework**: AppKit  
**Kind**: case

Enough data has been provided to successfully decompress the image (regardless of the complete: flag).

**Availability**:
- macOS ?+

## Declaration

```swift
case completed
```

## See Also

- [NSBitmapImageRep.LoadStatus.unknownType](nsbitmapimagerep/loadstatus/unknowntype.md)
  Not enough data to determine image format. You should continue to provide more data.
- [NSBitmapImageRep.LoadStatus.readingHeader](nsbitmapimagerep/loadstatus/readingheader.md)
  The image format is known, but not enough data has been read to determine the size, depth, etc., of the image. You should continue to provide more data.
- [NSBitmapImageRep.LoadStatus.willNeedAllData](nsbitmapimagerep/loadstatus/willneedalldata.md)
  Incremental loading cannot be supported.
- [NSBitmapImageRep.LoadStatus.invalidData](nsbitmapimagerep/loadstatus/invaliddata.md)
  An error occurred during image decompression. The image contains the portions of the data that have already been successfully decompressed, if any
- [NSBitmapImageRep.LoadStatus.unexpectedEOF](nsbitmapimagerep/loadstatus/unexpectedeof.md)
  Not enough data was available to fully decompress the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/loadstatus/completed)*