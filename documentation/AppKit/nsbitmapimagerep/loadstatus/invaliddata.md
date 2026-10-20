# NSBitmapImageRep.LoadStatus.invalidData

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

An error occurred during image decompression. The image contains the portions of the data that have already been successfully decompressed, if any

**Availability**:
- macOS

## Declaration

```swift
case invalidData
```

```c
NSImageRepLoadStatusInvalidData
```

## See Also

### Constants
- [NSBitmapImageRep.LoadStatus.unknownType](./unknowntype.md)
  Not enough data to determine image format. You should continue to provide more data.
- [NSBitmapImageRep.LoadStatus.readingHeader](./readingheader.md)
  The image format is known, but not enough data has been read to determine the size, depth, etc., of the image. You should continue to provide more data.
- [NSBitmapImageRep.LoadStatus.willNeedAllData](./willneedalldata.md)
  Incremental loading cannot be supported.
- [NSBitmapImageRep.LoadStatus.unexpectedEOF](./unexpectedeof.md)
  Not enough data was available to fully decompress the image.
- [NSBitmapImageRep.LoadStatus.completed](./completed.md)
  Enough data has been provided to successfully decompress the image (regardless of the complete: flag).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/loadstatus/invaliddata)*