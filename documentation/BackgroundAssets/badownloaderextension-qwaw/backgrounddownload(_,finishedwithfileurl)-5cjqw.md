# backgroundDownload(_:finishedWithFileURL:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

This method is called when a download has finished but there is no `BADownloadManager` delegate to handle the completion event.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
func backgroundDownload(_ finishedDownload: BADownload, finishedWithFileURL fileURL: URL)
```

## Discussion

When a download succeeds, this method will be invoked; however it is only invoked if there is no other client using `BADownloadManager` with a hooked in `delegate`. The file located at `fileURL` must be moved before this method exits scope, or it will be deleted. It is strongly advised to move the file to its permanent destination rather than copy it.

> ⚠️ **Warning**: The file is marked by the system for deletion when the device becomes low on storage. Avoid copying or modifying the file, as this may remove the system’s ability to delete the file.

## Parameters

- `finishedDownload`: Download that has completed successfully.
- `fileURL`: A location to the file that has been downloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-qwaw/backgrounddownload(_:finishedwithfileurl:)-5cjqw)*