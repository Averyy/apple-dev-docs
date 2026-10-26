# downloads(for:manifestURL:extensionInfo:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Returns asset-pack downloads to schedule.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func downloads(for request: BAContentRequest, manifestURL: URL, extensionInfo: BAAppExtensionInfo) -> Set<BADownload>
```

#### Return Value

The downloads to schedule.

#### Discussion

> ⚠️ **Warning**: Don’t override this default implementation.

## Parameters

- `request`: The content request.
- `manifestURL`: A file URL to the manifest of asset packs that are available to download.
- `extensionInfo`: Information about the downloader extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-qwaw/downloads(for:manifesturl:extensioninfo:)-60zuh)*