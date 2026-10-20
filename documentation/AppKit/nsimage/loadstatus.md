# NSImage.LoadStatus

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Status values for incremental image loading.

**Availability**:
- macOS

## Declaration

```swift
enum LoadStatus
```

```c
enum NSImageLoadStatus : NSUInteger;
```

## Topics

### Load Status Values
- [NSImage.LoadStatus.completed](./loadstatus/completed.md)
  Enough data is available to completely decompress the image.
- [NSImage.LoadStatus.cancelled](./loadstatus/cancelled.md)
  Image loading was canceled.
- [NSImage.LoadStatus.invalidData](./loadstatus/invaliddata.md)
  An error occurred during image decompression.
- [NSImage.LoadStatus.unexpectedEOF](./loadstatus/unexpectedeof.md)
  Not enough data was available to fully decompress the image.
- [NSImage.LoadStatus.readError](./loadstatus/readerror.md)
  Not enough data was available for full decompression of the image.
### Initializers
- [init?(rawValue: UInt)](./loadstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/loadstatus)*