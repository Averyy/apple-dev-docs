# isUploading

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the item is currently uploading to your remote server.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var isUploading: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isUploading) BOOL uploading;
```

## See Also

### Monitoring File Transfers
- [var isUploaded: Bool](./isuploaded.md)
  A Boolean value that indicates whether the item has been uploaded to your remote server.
- [var uploadingError: (any Error)?](./uploadingerror.md)
  An object describing an error that occurred while uploading the item.
- [var isDownloading: Bool](./isdownloading.md)
  A Boolean value that indicates whether the item is currently downloading from your remote server.
- [var isDownloaded: Bool](./isdownloaded.md)
  A Boolean value that indicates whether the item has been downloaded from your remote server.
- [var downloadingError: (any Error)?](./downloadingerror.md)
  An object describing an error that occurred while downloading the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/isuploading)*