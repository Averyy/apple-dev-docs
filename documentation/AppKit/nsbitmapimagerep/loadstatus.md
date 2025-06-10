# NSBitmapImageRep.LoadStatus

**Framework**: AppKit  
**Kind**: enum

Constants that identify the loading status of the image.

**Availability**:
- macOS ?+

## Declaration

```swift
enum LoadStatus
```

#### Overview

These status values are returned by [`incrementalLoad(from:complete:)`](nsbitmapimagerep/incrementalload(from:complete:).md).

## Topics

### Constants
- [NSBitmapImageRep.LoadStatus.unknownType](nsbitmapimagerep/loadstatus/unknowntype.md)
  Not enough data to determine image format. You should continue to provide more data.
- [NSBitmapImageRep.LoadStatus.readingHeader](nsbitmapimagerep/loadstatus/readingheader.md)
  The image format is known, but not enough data has been read to determine the size, depth, etc., of the image. You should continue to provide more data.
- [NSBitmapImageRep.LoadStatus.willNeedAllData](nsbitmapimagerep/loadstatus/willneedalldata.md)
  Incremental loading cannot be supported.
- [NSBitmapImageRep.LoadStatus.invalidData](nsbitmapimagerep/loadstatus/invaliddata.md)
  An error occurred during image decompression. The image contains the portions of the data that have already been successfully decompressed, if any
- [NSBitmapImageRep.LoadStatus.unexpectedEOF](nsbitmapimagerep/loadstatus/unexpectedeof.md)
  [`incrementalLoad(from:complete:)`](nsbitmapimagerep/incrementalload(from:complete:).md) was called with [`true`](https://developer.apple.com/documentation/swift/true), but not enough data was available for decompression. The image contains the portions of the data that have already been successfully decompressed, if any.
- [NSBitmapImageRep.LoadStatus.completed](nsbitmapimagerep/loadstatus/completed.md)
  Enough data has been provided to successfully decompress the image (regardless of the complete: flag).
### Initializers
- [init?(rawValue: Int)](nsbitmapimagerep/loadstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func incrementalLoad(from: Data, complete: Bool) -> Int](nsbitmapimagerep/incrementalload(from:complete:).md)
  Loads the current image data into an incrementally-loaded image representation and returns the current status of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/loadstatus)*