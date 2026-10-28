# download(for:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Creates a download object for the asset pack that you schedule using a download manager.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func download(for contentRequest: BAContentRequest?) -> BADownload
```

## Return Value

A download object.

## Parameters

- `contentRequest`: The content request for the current extension invocation. Pass `nil` if you’re calling this method in your main app.

## See Also

### Downloading assets
- [let downloadSize: Int](./downloadsize.md)
  The size of the download file containing the asset pack in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpack/download(for:))*