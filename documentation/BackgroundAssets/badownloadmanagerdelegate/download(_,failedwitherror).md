# download(_:failedWithError:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Informs the delegate about a failed asset download.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
optional func download(_ download: BADownload, failedWithError error: any Error)
```

```objc
- (void) download:(BADownload *) download failedWithError:(NSError *) error;
```

## Parameters

- `download`: The failed asset download.
- `error`: An object that provides detailed information about why the framework isn’t able to download the asset.

## See Also

### Processing concluded downloads
- [func download(BADownload, finishedWithFileURL: URL)](./download%28_,finishedwithfileurl%29.md)
  Informs the delegate about a finished asset download and provides the on-disk location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanagerdelegate/download(_:failedwitherror:))*