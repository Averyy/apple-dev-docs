# uploadingError

**Framework**: File Provider  
**Kind**: property

An object describing an error that occurred while uploading the item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var uploadingError: (any Error)? { get }
```

## Mentions

- [Handling Errors with User-Driven Actions](handling-errors-with-user-driven-actions.md)

## See Also

- [var isUploading: Bool](nsfileprovideritemprotocol/isuploading.md)
  A Boolean value that indicates whether the item is currently uploading to your remote server.
- [var isUploaded: Bool](nsfileprovideritemprotocol/isuploaded.md)
  A Boolean value that indicates whether the item has been uploaded to your remote server.
- [var isDownloading: Bool](nsfileprovideritemprotocol/isdownloading.md)
  A Boolean value that indicates whether the item is currently downloading from your remote server.
- [var isDownloaded: Bool](nsfileprovideritemprotocol/isdownloaded.md)
  A Boolean value that indicates whether the item has been downloaded from your remote server.
- [var downloadingError: (any Error)?](nsfileprovideritemprotocol/downloadingerror.md)
  An object describing an error that occurred while downloading the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/uploadingerror)*