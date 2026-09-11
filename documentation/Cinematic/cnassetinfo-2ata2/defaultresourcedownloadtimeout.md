# defaultResourceDownloadTimeout

**Framework**: Cinematic  
**Kind**: property

Default timeout value for resource download for: `public static func downloadResources(versions: Set<CNCinematicResourceVersion> = [], timeout: TimeInterval = defaultResourceDownloadTimeout, subprogress: consuming Subprogress? = nil) async throws` `public func downloadResources(timeout: TimeInterval = defaultResourceDownloadTimeout, subprogress: consuming Subprogress? = nil) async throws -> CNAssetInfo`

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst ?+
- macOS 27.0+

## Declaration

```swift
static var defaultResourceDownloadTimeout: TimeInterval { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetinfo-2ata2/defaultresourcedownloadtimeout)*