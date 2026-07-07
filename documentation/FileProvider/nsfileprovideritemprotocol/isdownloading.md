# isDownloading

**Framework**: File Provider  
**Kind**: property

A Boolean value that indicates whether the item is currently downloading from your remote server.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var isDownloading: Bool { get }
```

## See Also

- [var isUploading: Bool](nsfileprovideritemprotocol/isuploading.md)
  A Boolean value that indicates whether the item is currently uploading to your remote server.
- [var isUploaded: Bool](nsfileprovideritemprotocol/isuploaded.md)
  A Boolean value that indicates whether the item has been uploaded to your remote server.
- [var uploadingError: (any Error)?](nsfileprovideritemprotocol/uploadingerror.md)
  An object describing an error that occurred while uploading the item.
- [var isDownloaded: Bool](nsfileprovideritemprotocol/isdownloaded.md)
  A Boolean value that indicates whether the item has been downloaded from your remote server.
- [var downloadingError: (any Error)?](nsfileprovideritemprotocol/downloadingerror.md)
  An object describing an error that occurred while downloading the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/isdownloading)*