# NSBitmapImageRep.LoadStatus.willNeedAllData

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Incremental loading cannot be supported.

**Availability**:
- macOS

## Declaration

```swift
case willNeedAllData
```

```c
NSImageRepLoadStatusWillNeedAllData
```

#### Discussion

Until you call [`incrementalLoad(from:complete:)`](../incrementalload%28from,complete%29.md) with [`true`](../../../Swift/true.md), this status will be returned. You can continue to call the method but no decompression will take place. Once you do call the method with [`true`](../../../Swift/true.md), then the image will be decompressed and one of the final three status messages will be returned.

## See Also

### Constants
- [NSBitmapImageRep.LoadStatus.unknownType](./unknowntype.md)
  Not enough data to determine image format. You should continue to provide more data.
- [NSBitmapImageRep.LoadStatus.readingHeader](./readingheader.md)
  The image format is known, but not enough data has been read to determine the size, depth, etc., of the image. You should continue to provide more data.
- [NSBitmapImageRep.LoadStatus.invalidData](./invaliddata.md)
  An error occurred during image decompression. The image contains the portions of the data that have already been successfully decompressed, if any
- [NSBitmapImageRep.LoadStatus.unexpectedEOF](./unexpectedeof.md)
  Not enough data was available to fully decompress the image.
- [NSBitmapImageRep.LoadStatus.completed](./completed.md)
  Enough data has been provided to successfully decompress the image (regardless of the complete: flag).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/loadstatus/willneedalldata)*