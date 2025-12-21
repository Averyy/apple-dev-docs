# NSBitmapImageRep.LoadStatus.unknownType

**Framework**: AppKit  
**Kind**: case

Not enough data to determine image format. You should continue to provide more data.

**Availability**:
- macOS ?+

## Declaration

```swift
case unknownType
```

## See Also

- [NSBitmapImageRep.LoadStatus.readingHeader](nsbitmapimagerep/loadstatus/readingheader.md)
  The image format is known, but not enough data has been read to determine the size, depth, etc., of the image. You should continue to provide more data.
- [NSBitmapImageRep.LoadStatus.willNeedAllData](nsbitmapimagerep/loadstatus/willneedalldata.md)
  Incremental loading cannot be supported.
- [NSBitmapImageRep.LoadStatus.invalidData](nsbitmapimagerep/loadstatus/invaliddata.md)
  An error occurred during image decompression. The image contains the portions of the data that have already been successfully decompressed, if any
- [NSBitmapImageRep.LoadStatus.unexpectedEOF](nsbitmapimagerep/loadstatus/unexpectedeof.md)
  Not enough data was available to fully decompress the image.
- [NSBitmapImageRep.LoadStatus.completed](nsbitmapimagerep/loadstatus/completed.md)
  Enough data has been provided to successfully decompress the image (regardless of the complete: flag).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/loadstatus/unknowntype)*