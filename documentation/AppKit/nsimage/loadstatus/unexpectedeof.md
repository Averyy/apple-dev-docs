# NSImage.LoadStatus.unexpectedEOF

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
NSImageLoadStatusUnexpectedEOF
```

#### Discussion

The image contains the portions of the data that have already been successfully decompressed, if any.

## See Also

### Load Status Values
- [NSImage.LoadStatus.completed](./completed.md)
  Enough data is available to completely decompress the image.
- [NSImage.LoadStatus.cancelled](./cancelled.md)
  Image loading was canceled.
- [NSImage.LoadStatus.invalidData](./invaliddata.md)
  An error occurred during image decompression.
- [NSImage.LoadStatus.readError](./readerror.md)
  Not enough data was available for full decompression of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/loadstatus/unexpectedeof)*