# downloads(for:manifestURL:extensionInfo:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Invoked by the system when the extension should check for updated content. This method will be invoked by the system upon requested events defined in `BAContentRequest`. This method should return a set of all `BAURLDownload`’s that your extension would like to schedule. During the invocation of this method, `BADownloadManager` will prohibit the ability to schedule additional downloads until this method exits scope. Therefore, all downloads needing to be scheduled should be returned here. If a download fails, it can be rescheduled using `BADownloadManager` in any other method in this protocol.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
func downloads(for request: BAContentRequest, manifestURL: URL, extensionInfo: BAAppExtensionInfo) -> Set<BADownload>
```

#### Return Value

A set of unique `BAURLDownload` objects that the extension should schedule for download.

#### Discussion

> ⚠️ **Warning**: You cannot use `BADownloadManager` to manually schedule downloads using this method. All downloads to enqueue must be returned.

## Parameters

- `request`: The content request event that occured that caused this method to be invoked.
- `manifestURL`: A file URL to the local manifest that was pre-downloaded and specified in your App’s Info.plist under the `BAManifestURL`. The file is read-only and will be deleted after this method returns. If you wish to keep it, you must copy it out.
- `extensionInfo`: Information about your extension that may be useful for making a decision about what content needs to be scheduled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-qwaw/downloads(for:manifesturl:extensioninfo:)-7zv3a)*