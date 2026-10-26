# BEDownloadMonitor

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

An object that reports the status of web downloads to the system.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```objc
@interface BEDownloadMonitor : NSObject
```

#### Overview

When someone downloads a file in your web browser, create an instance of this class to report progress to the system, and optionally create a placeholder file in the person’s Downloads folder. For more information, see [Downloading files in a web browser with an alternative browser engine](./downloading-files-in-a-web-browser.md).

## Topics

### Creating a download monitor
- [- initWithSourceURL:destinationURL:observedProgress:liveActivityAccessToken:](./bedownloadmonitor-9y4hu/initwithsourceurl_destinationurl_observedprogress_liveactivityaccesstoken_.md)
  Initializes a download monitor to report progress for the specified download.
- [+ createAccessToken](./bedownloadmonitor-9y4hu/createaccesstoken.md)
  Generates an opaque token that the system uses to keep your networking extension active in the background.
### Creating a download placeholder
- [- useDownloadsFolderWithPlaceholderType:finalFileCreatedHandler:](./bedownloadmonitor-9y4hu/usedownloadsfolderwithplaceholdertype_finalfilecreatedhandler_.md)
  Asks the system to create a placeholder for the downloaded file in the person’s Downloads folder.
- [BEDownloadMonitorLocation](./bedownloadmonitorlocation.md)
  A class that associates a URL with the bookmark you use to access that URL.
### Reporting progress to the system
- [- beginMonitoring:](./bedownloadmonitor-9y4hu/beginmonitoring_.md)
  Informs the system to start monitoring the download.
- [- resumeMonitoring:completionHandler:](./bedownloadmonitor-9y4hu/resumemonitoring_completionhandler_.md)
  Informs the system that it needs to resume monitoring the download.
### Getting information about a download
- [sourceURL](./bedownloadmonitor-9y4hu/sourceurl.md)
  A URL to a remote file to download.
- [destinationURL](./bedownloadmonitor-9y4hu/destinationurl.md)
  A local file path to the downloaded file.
### Identifying a download
- [identifier](./bedownloadmonitor-9y4hu/identifier.md)
  The stable identity of the entity associated with this instance.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Downloads
- [Downloading files in a web browser with an alternative browser engine](./downloading-files-in-a-web-browser.md)
  Report download progress to the system to keep your networking extension active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9y4hu)*