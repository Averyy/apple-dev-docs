# allDownloads(for:)

**Framework**: Background Assets  
**Kind**: method

Creates download objects for every asset pack, which can be scheduled with the download manager.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func allDownloads(for contentRequest: BAContentRequest?) -> Set<BADownload>
```

#### Return Value

A collection of download objects.

## Parameters

- `contentRequest`: The content request for the current extension invocation. Pass   if you’re calling this method in your main app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/assetpackmanifest/alldownloads(for:))*