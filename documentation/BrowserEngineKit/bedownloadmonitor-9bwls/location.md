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

#### Overview

Pass the [`bookmarkData`](bedownloadmonitor-9bwls/location/bookmarkdata.md) to your browser app to resolve the URL in the app. For information on using XPC to share data between your networking extension and browser app, see [`Using XPC to communicate with browser extensions`](using-xpc-to-communicate-with-browser-extensions.md).

The URL bookmark in a `Location` isn’t suitable for storing on disk and resolving in subsequent launches of your app. To do this, create your own bookmark using [`bookmarkData(options:includingResourceValuesForKeys:relativeTo:)`](https://developer.apple.com/documentation/foundation/nsurl/bookmarkdata(options:includingresourcevaluesforkeys:relativeto:)), passing the [`withSecurityScope`](https://developer.apple.com/documentation/foundation/nsurl/bookmarkcreationoptions/withsecurityscope) flag.

## Topics

### Getting information about a location
- [let url: URL](bedownloadmonitor-9bwls/location/url.md)
  The location of the resource.
- [let bookmarkData: Data](bedownloadmonitor-9bwls/location/bookmarkdata.md)
  A bookmark that resolves to the resource’s URL.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func useDownloadsFolder(placeholderType: UTType?, finalFileCreatedHandler: (BEDownloadMonitor.Location?) -> Void)](bedownloadmonitor-9bwls/usedownloadsfolder(placeholdertype:finalfilecreatedhandler:).md)
  Asks the system to create a placeholder for the downloaded file in the person’s Downloads folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9bwls/location)*