# NSImage.LoadStatus.cancelled

**Framework**: AppKit  
**Kind**: case

Image loading was canceled.

**Availability**:
- macOS ?+

## Declaration

```swift
case cancelled
```

#### Discussion

The image contains the portions of the data that have already been successfully decompressed, if any.

## See Also

- [NSImage.LoadStatus.completed](nsimage/loadstatus/completed.md)
  Enough data is available to completely decompress the image.
- [NSImage.LoadStatus.invalidData](nsimage/loadstatus/invaliddata.md)
  An error occurred during image decompression.
- [NSImage.LoadStatus.unexpectedEOF](nsimage/loadstatus/unexpectedeof.md)
  Not enough data was available to fully decompress the image.
- [NSImage.LoadStatus.readError](nsimage/loadstatus/readerror.md)
  Not enough data was available for full decompression of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/loadstatus/cancelled)*