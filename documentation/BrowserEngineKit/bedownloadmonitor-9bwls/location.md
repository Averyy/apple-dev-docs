# BEDownloadMonitor.Location

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

A class that associates a URL with the bookmark you use to access that URL.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
@objc(BEDownloadMonitorLocation)
class Location
```

## Overview

Pass the [`bookmarkData`](./location/bookmarkdata.md) to your browser app to resolve the URL in the app. For information on using XPC to share data between your networking extension and browser app, see [Using XPC to communicate with browser extensions](../using-xpc-to-communicate-with-browser-extensions.md).

The URL bookmark in a `Location` isn’t suitable for storing on disk and resolving in subsequent launches of your app. To do this, create your own bookmark using [`bookmarkData(options:includingResourceValuesForKeys:relativeTo:)`](../../Foundation/nsurl/bookmarkdata%28options,includingresourcevaluesforkeys,relativeto%29.md), passing the [`withSecurityScope`](../../Foundation/nsurl/bookmarkcreationoptions/withsecurityscope.md) flag.

## Topics

### Getting information about a location
- [let url: URL](./location/url.md)
  The location of the resource.
- [let bookmarkData: Data](./location/bookmarkdata.md)
  A bookmark that resolves to the resource’s URL.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a download placeholder
- [func useDownloadsFolder(placeholderType: UTType?, finalFileCreatedHandler: (BEDownloadMonitor.Location?) -> Void)](./usedownloadsfolder%28placeholdertype,finalfilecreatedhandler%29.md)
  Asks the system to create a placeholder for the downloaded file in the person’s Downloads folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9bwls/location)*