# downloadResources(timeout:subprogress:)

**Framework**: Cinematic  
**Kind**: method

Downloads the resources required to render cinematic effects for the given asset Resources are device-wide and are cached once downloaded

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst ?+
- macOS 27.0+

## Declaration

```swift
@discardableResult
func downloadResources(timeout: TimeInterval = defaultResourceDownloadTimeout, subprogress: consuming Subprogress? = nil) async throws -> CNAssetInfo
```

#### Discussion

Cancellation: this method responds to Swift Task cancellation. If the calling task is cancelled, the download stops; any partially downloaded resources are discarded.

## Parameters

- `subprogress`: Monitors the download progress


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetinfo-2ata2/downloadresources(timeout:subprogress:))*