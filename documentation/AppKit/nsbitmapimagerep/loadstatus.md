# NSBitmapImageRep.LoadStatus

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that identify the loading status of the image.

**Availability**:
- macOS

## Declaration

```swift
enum LoadStatus
```

```c
enum NSImageRepLoadStatus : NSInteger;
```

## Overview

These status values are returned by [`incrementalLoad(from:complete:)`](./incrementalload%28from,complete%29.md).

## Topics

### Constants
- [NSBitmapImageRep.LoadStatus.unknownType](./loadstatus/unknowntype.md)
  Not enough data to determine image format. You should continue to provide more data.
- [NSBitmapImageRep.LoadStatus.readingHeader](./loadstatus/readingheader.md)
  The image format is known, but not enough data has been read to determine the size, depth, etc., of the image. You should continue to provide more data.
- [NSBitmapImageRep.LoadStatus.willNeedAllData](./loadstatus/willneedalldata.md)
  Incremental loading cannot be supported.
- [NSBitmapImageRep.LoadStatus.invalidData](./loadstatus/invaliddata.md)
  An error occurred during image decompression. The image contains the portions of the data that have already been successfully decompressed, if any
- [NSBitmapImageRep.LoadStatus.unexpectedEOF](./loadstatus/unexpectedeof.md)
  Not enough data was available to fully decompress the image.
- [NSBitmapImageRep.LoadStatus.completed](./loadstatus/completed.md)
  Enough data has been provided to successfully decompress the image (regardless of the complete: flag).
### Initializers
- [init?(rawValue: Int)](./loadstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Loading Images Incrementally
- [func incrementalLoad(from: Data, complete: Bool) -> Int](./incrementalload%28from,complete%29.md)
  Loads the current image data into an incrementally-loaded image representation and returns the current status of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/loadstatus)*