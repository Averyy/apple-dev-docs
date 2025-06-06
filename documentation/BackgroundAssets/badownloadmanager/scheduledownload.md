# scheduleDownload(_:)

**Framework**: Background Assets  
**Kind**: method

Schedules an asset download to execute in the background at a nonspecific time in the future.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
func scheduleDownload(_ download: BADownload) throws
```

## Parameters

- `download`: The object that provides the URL of the asset to download.

## See Also

- [func startForegroundDownload(BADownload) throws](badownloadmanager/startforegrounddownload(_:).md)
  Schedules an asset download that executes immediately in the foreground.
- [func cancel(BADownload) throws](badownloadmanager/cancel(_:).md)
  Cancels an asset download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanager/scheduledownload(_:))*