# downloadSize

**Framework**: Background Assets  
**Kind**: property

The size of the download file containing the asset pack in bytes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let downloadSize: Int
```

#### Discussion

This is different than the installation size, which could be larger.

## See Also

- [func download(for: BAContentRequest?) -> BADownload](assetpack/download(for:).md)
  Creates a download object for the asset pack that you schedule using a download manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpack/downloadsize)*