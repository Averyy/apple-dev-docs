# download(_:finishedWithFileURL:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Informs the delegate about a finished asset download and provides the on-disk location.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
optional func download(_ download: BADownload, finishedWithFileURL fileURL: URL)
```

```objc
- (void) download:(BADownload *) download finishedWithFileURL:(NSURL *) fileURL;
```

## Discussion

Prefer to access downloaded assets in-place, rather than moving or copying them. This enables the system to include those assets when evaluating which files it can safely delete when a person’s device is running low on disk space.

## Parameters

- `download`: The finished asset download.
- `fileURL`: The URL to the downloaded asset’s location in the associated App Group.

## See Also

### Processing concluded downloads
- [func download(BADownload, failedWithError: any Error)](./download%28_,failedwitherror%29.md)
  Informs the delegate about a failed asset download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanagerdelegate/download(_:finishedwithfileurl:))*