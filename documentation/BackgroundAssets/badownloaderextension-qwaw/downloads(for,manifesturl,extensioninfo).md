# downloads(for:manifestURL:extensionInfo:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

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

## Default Implementations

### BADownloaderExtension Implementations
- [func downloads(for: BAContentRequest, manifestURL: URL, extensionInfo: BAAppExtensionInfo) -> Set<BADownload>](./downloads%28for,manifesturl,extensioninfo%29-60zuh.md)
  Returns asset-pack downloads to schedule.
- [func downloads(for: BAContentRequest, manifestURL: URL, extensionInfo: BAAppExtensionInfo) -> Set<BADownload>](./downloads%28for,manifesturl,extensioninfo%29-7zv3a.md)
  Invoked by the system when the extension should check for updated content. This method will be invoked by the system upon requested events defined in `BAContentRequest`. This method should return a set of all `BAURLDownload`’s that your extension would like to schedule. During the invocation of this method, `BADownloadManager` will prohibit the ability to schedule additional downloads until this method exits scope. Therefore, all downloads needing to be scheduled should be returned here. If a download fails, it can be rescheduled using `BADownloadManager` in any other method in this protocol.

## See Also

### Checking for asset updates
- [enum BAContentRequest](../bacontentrequest.md)
  A type that indicates the purpose of a content download request.
- [class BAAppExtensionInfo](../baappextensioninfo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-qwaw/downloads(for:manifesturl:extensioninfo:))*