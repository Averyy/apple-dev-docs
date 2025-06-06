# download(_:finishedWithFileURL:)

**Framework**: Background Assets  
**Kind**: method

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

#### Discussion

Prefer to access downloaded assets in-place, rather than moving or copying them. This enables the system to include those assets when evaluating which files it can safely delete when a person’s device is running low on disk space.

## Parameters

- `download`: The finished asset download.
- `fileURL`: The URL to the downloaded asset’s location in the associated App Group.

## See Also

- [func download(BADownload, failedWithError: any Error)](badownloadmanagerdelegate/download(_:failedwitherror:).md)
  Informs the delegate about a failed asset download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanagerdelegate/download(_:finishedwithfileurl:))*