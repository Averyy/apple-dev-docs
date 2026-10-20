# downloadingError

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

An object describing an error that occurred while downloading the item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var downloadingError: (any Error)? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSError * downloadingError;
```

## See Also

### Monitoring File Transfers
- [var isUploading: Bool](./isuploading.md)
  A Boolean value that indicates whether the item is currently uploading to your remote server.
- [var isUploaded: Bool](./isuploaded.md)
  A Boolean value that indicates whether the item has been uploaded to your remote server.
- [var uploadingError: (any Error)?](./uploadingerror.md)
  An object describing an error that occurred while uploading the item.
- [var isDownloading: Bool](./isdownloading.md)
  A Boolean value that indicates whether the item is currently downloading from your remote server.
- [var isDownloaded: Bool](./isdownloaded.md)
  A Boolean value that indicates whether the item has been downloaded from your remote server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/downloadingerror)*