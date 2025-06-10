# download(for:)

**Framework**: Background Assets  
**Kind**: method

Creates a download object for the asset pack that you schedule using a download manager.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func download(for contentRequest: BAContentRequest?) -> BADownload
```

#### Return Value

A download object.

## Parameters

- `contentRequest`: The content request for the current extension invocation. Pass   if you’re calling this method in your main app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpack/download(for:))*