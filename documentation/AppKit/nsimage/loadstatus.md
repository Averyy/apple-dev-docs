# NSImage.LoadStatus

**Framework**: AppKit  
**Kind**: enum

Status values for incremental image loading.

**Availability**:
- macOS ?+

## Declaration

```swift
enum LoadStatus
```

## Topics

### Load Status Values
- [NSImage.LoadStatus.completed](nsimage/loadstatus/completed.md)
  Enough data is available to completely decompress the image.
- [NSImage.LoadStatus.cancelled](nsimage/loadstatus/cancelled.md)
  Image loading was canceled.
- [NSImage.LoadStatus.invalidData](nsimage/loadstatus/invaliddata.md)
  An error occurred during image decompression.
- [NSImage.LoadStatus.unexpectedEOF](nsimage/loadstatus/unexpectedeof.md)
  Not enough data was available to fully decompress the image.
- [NSImage.LoadStatus.readError](nsimage/loadstatus/readerror.md)
  Not enough data was available for full decompression of the image.
### Initializers
- [init?(rawValue: UInt)](nsimage/loadstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/loadstatus)*