# useDownloadsFolder(placeholderType:finalFileCreatedHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method

Asks the system to create a placeholder for the downloaded file in the person’s Downloads folder.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
@objc
(useDownloadsFolderWithPlaceholderType:finalFileCreatedHandler:) func useDownloadsFolder(placeholderType: UTType? = nil, finalFileCreatedHandler: @escaping (BEDownloadMonitor.Location?) -> Void)
```

## Mentions

- [Downloading files in a web browser with an alternative browser engine](downloading-files-in-a-web-browser.md)

## Parameters

- `placeholderType`: The type of the file for which the system creates a placeholder. If this is  , the system chooses a type based on the download’s filename extension.
- `finalFileCreatedHandler`: A closure you use to receive the location of the downloaded file in the person’s Downloads folder.

## See Also

- [BEDownloadMonitor.Location](bedownloadmonitor-9bwls/location.md)
  A class that associates a URL with the bookmark you use to access that URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9bwls/usedownloadsfolder(placeholdertype:finalfilecreatedhandler:))*