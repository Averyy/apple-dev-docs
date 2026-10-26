# useDownloadsFolderWithPlaceholderType:finalFileCreatedHandler:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Asks the system to create a placeholder for the downloaded file in the person’s Downloads folder.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```objc
- (void) useDownloadsFolderWithPlaceholderType:(UTType *) type finalFileCreatedHandler:(void (^)(BEDownloadMonitorLocation *finalLocation)) finalFileCreatedHandler;
```

## Parameters

- `type`: The type of the file for which the system creates a placeholder. If this is `nil`, the system chooses a type based on the download’s filename extension.
- `finalFileCreatedHandler`: A closure you use to receive the location of the downloaded file in the person’s Downloads folder.

## See Also

### Creating a download placeholder
- [BEDownloadMonitorLocation](../bedownloadmonitorlocation.md)
  A class that associates a URL with the bookmark you use to access that URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9y4hu/usedownloadsfolderwithplaceholdertype:finalfilecreatedhandler:)*