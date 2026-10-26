# backgroundDownload(_:finishedWithFileURL:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Handles a finished download

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func backgroundDownload(_ finishedDownload: BADownload, finishedWithFileURL fileURL: URL)
```

#### Discussion

> ⚠️ **Warning**: Don’t override this default implementation.

## Parameters

- `finishedDownload`: The finished download.
- `fileURL`: The file URL at which the downloaded asset pack was saved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-qwaw/backgrounddownload(_:finishedwithfileurl:)-4s70i)*