# NSImage.LoadStatus.invalidData

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

An error occurred during image decompression.

**Availability**:
- macOS

## Declaration

```swift
case invalidData
```

```c
NSImageLoadStatusInvalidData
```

## Discussion

The image data is probably corrupt. The image contains the portions of the data that have already been successfully decompressed, if any.

## See Also

### Load Status Values
- [NSImage.LoadStatus.completed](./completed.md)
  Enough data is available to completely decompress the image.
- [NSImage.LoadStatus.cancelled](./cancelled.md)
  Image loading was canceled.
- [NSImage.LoadStatus.unexpectedEOF](./unexpectedeof.md)
  Not enough data was available to fully decompress the image.
- [NSImage.LoadStatus.readError](./readerror.md)
  Not enough data was available for full decompression of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/loadstatus/invaliddata)*