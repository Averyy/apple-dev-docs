# NSBitmapImageRep.LoadStatus.unexpectedEOF

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Not enough data was available to fully decompress the image.

**Availability**:
- macOS

## Declaration

```swift
case unexpectedEOF
```

```c
NSImageRepLoadStatusUnexpectedEOF
```

#### Discussion

[`incrementalLoad(from:complete:)`](../incrementalload%28from,complete%29.md) was called with [`true`](../../../Swift/true.md), but not enough data was available for decompression. The image contains the portions of the data that have already been successfully decompressed, if any.

## See Also

### Constants
- [NSBitmapImageRep.LoadStatus.unknownType](./unknowntype.md)
  Not enough data to determine image format. You should continue to provide more data.
- [NSBitmapImageRep.LoadStatus.readingHeader](./readingheader.md)
  The image format is known, but not enough data has been read to determine the size, depth, etc., of the image. You should continue to provide more data.
- [NSBitmapImageRep.LoadStatus.willNeedAllData](./willneedalldata.md)
  Incremental loading cannot be supported.
- [NSBitmapImageRep.LoadStatus.invalidData](./invaliddata.md)
  An error occurred during image decompression. The image contains the portions of the data that have already been successfully decompressed, if any
- [NSBitmapImageRep.LoadStatus.completed](./completed.md)
  Enough data has been provided to successfully decompress the image (regardless of the complete: flag).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/loadstatus/unexpectedeof)*