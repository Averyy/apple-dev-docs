# BEDownloadMonitor

**Framework**: BrowserEngineKit  
**Kind**: class

An object that reports the status of web downloads to the system.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
@objc
(BEDownloadMonitor) class BEDownloadMonitor
```

## Mentions

- [Downloading files in a web browser with an alternative browser engine](downloading-files-in-a-web-browser.md)

#### Overview

When someone downloads a file in your web browser, create an instance of this class to report progress to the system, and optionally create a placeholder file in the person’s Downloads folder. For more information, see [`Downloading files in a web browser with an alternative browser engine`](downloading-files-in-a-web-browser.md).

## Topics

### Creating a download monitor
- [init(sourceURL: URL, destinationURL: URL, observedProgress: Progress, liveActivityAccessToken: Data)](bedownloadmonitor-9bwls/init(sourceurl:destinationurl:observedprogress:liveactivityaccesstoken:).md)
  Initializes a download monitor to report progress for the specified download.
- [static func createAccessToken() -> Data?](bedownloadmonitor-9bwls/createaccesstoken.md)
  Generates an opaque token that the system uses to keep your networking extension active in the background.
### Creating a download placeholder
- [func useDownloadsFolder(placeholderType: UTType?, finalFileCreatedHandler: (BEDownloadMonitor.Location?) -> Void)](bedownloadmonitor-9bwls/usedownloadsfolder(placeholdertype:finalfilecreatedhandler:).md)
  Asks the system to create a placeholder for the downloaded file in the person’s Downloads folder.
- [BEDownloadMonitor.Location](bedownloadmonitor-9bwls/location.md)
  A class that associates a URL with the bookmark you use to access that URL.
### Reporting progress to the system
- [func beginMonitoring() async throws -> BEDownloadMonitor.Location?](bedownloadmonitor-9bwls/beginmonitoring.md)
  Informs the system to start monitoring the download.
- [func resumeMonitoring(placeholderURL: URL) async throws](bedownloadmonitor-9bwls/resumemonitoring(placeholderurl:).md)
  Informs the system that it needs to resume monitoring the download.
### Getting information about a download
- [let sourceURL: URL](bedownloadmonitor-9bwls/sourceurl.md)
- [let destinationURL: URL](bedownloadmonitor-9bwls/destinationurl.md)
### Identifying a download
- [let id: UUID](bedownloadmonitor-9bwls/id-swift.property.md)
  The stable identity of the entity associated with this instance.
- [BEDownloadMonitor.ID](bedownloadmonitor-9bwls/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Downloading files in a web browser with an alternative browser engine](downloading-files-in-a-web-browser.md)
  Report download progress to the system to keep your networking extension active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9bwls)*