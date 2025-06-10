# NSImage.LoadStatus.unexpectedEOF

**Framework**: AppKit  
**Kind**: case

Not enough data was available to fully decompress the image.

**Availability**:
- macOS ?+

## Declaration

```swift
case unexpectedEOF
```

#### Discussion

The image contains the portions of the data that have already been successfully decompressed, if any.

## See Also

- [NSImage.LoadStatus.completed](nsimage/loadstatus/completed.md)
  Enough data is available to completely decompress the image.
- [NSImage.LoadStatus.cancelled](nsimage/loadstatus/cancelled.md)
  Image loading was canceled.
- [NSImage.LoadStatus.invalidData](nsimage/loadstatus/invaliddata.md)
  An error occurred during image decompression.
- [NSImage.LoadStatus.readError](nsimage/loadstatus/readerror.md)
  Not enough data was available for full decompression of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/loadstatus/unexpectedeof)*