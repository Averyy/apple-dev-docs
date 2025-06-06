# BEDownloadMonitor.Location

**Framework**: BrowserEngineKit  
**Kind**: class

A class that associates a URL with the bookmark you use to access that URL.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
@objc
(BEDownloadMonitorLocation) class Location
```

#### Discussion

Pass the [`bookmarkData`](bedownloadmonitor-9bwls/location/bookmarkdata.md) to your browser app to resolve the URL in the app. For information on using XPC to share data between your networking extension and browser app, see [`Using XPC to communicate with browser extensions`](using-xpc-to-communicate-with-browser-extensions.md).

The URL bookmark in a `Location` isn’t suitable for storing on disk and resolving in subsequent launches of your app. To do this, create your own bookmark using [`bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:`](https://developer.apple.com/documentation/foundation/nsurl/1417795-bookmarkdatawithoptions), passing the [`withSecurityScope`](https://developer.apple.com/documentation/foundation/nsurl/bookmarkcreationoptions/1413824-withsecurityscope) flag.

## Topics

### Getting information about a location
- [let url: URL](bedownloadmonitor-9bwls/location/url.md)
  The location of the resource.
- [let bookmarkData: Data](bedownloadmonitor-9bwls/location/bookmarkdata.md)
  A bookmark that resolves to the resource’s URL.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func useDownloadsFolder(placeholderType: UTType?, finalFileCreatedHandler: (BEDownloadMonitor.Location?) -> Void)](bedownloadmonitor-9bwls/usedownloadsfolder(placeholdertype:finalfilecreatedhandler:).md)
  Asks the system to create a placeholder for the downloaded file in the person’s Downloads folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9bwls/location)*