# BEDownloadMonitorLocation

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

A class that associates a URL with the bookmark you use to access that URL.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```objc
@interface BEDownloadMonitorLocation : NSObject
```

#### Overview

Pass the [`bookmarkData`](./bedownloadmonitorlocation/bookmarkdata.md) to your browser app to resolve the URL in the app. For information on using XPC to share data between your networking extension and browser app, see [Using XPC to communicate with browser extensions](./using-xpc-to-communicate-with-browser-extensions.md).

The URL bookmark in a `Location` isn’t suitable for storing on disk and resolving in subsequent launches of your app. To do this, create your own bookmark using [`bookmarkData(options:includingResourceValuesForKeys:relativeTo:)`](../Foundation/nsurl/bookmarkdata%28options,includingresourcevaluesforkeys,relativeto%29.md), passing the [`withSecurityScope`](../Foundation/nsurl/bookmarkcreationoptions/withsecurityscope.md) flag.

## Topics

### Getting information about a location
- [url](./bedownloadmonitorlocation/url.md)
  The location of the resource.
- [bookmarkData](./bedownloadmonitorlocation/bookmarkdata.md)
  A bookmark that resolves to the resource’s URL.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Creating a download placeholder
- [- useDownloadsFolderWithPlaceholderType:finalFileCreatedHandler:](./bedownloadmonitor-9y4hu/usedownloadsfolderwithplaceholdertype_finalfilecreatedhandler_.md)
  Asks the system to create a placeholder for the downloaded file in the person’s Downloads folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitorlocation)*