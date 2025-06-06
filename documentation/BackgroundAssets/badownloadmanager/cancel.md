# cancel(_:)

**Framework**: Background Assets  
**Kind**: method

Cancels an asset download.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
func cancel(_ download: BADownload) throws
```

## Parameters

- `download`: The object that identifies the scheduled or in-progress download to cancel.

## See Also

- [func scheduleDownload(BADownload) throws](badownloadmanager/scheduledownload(_:).md)
  Schedules an asset download to execute in the background at a nonspecific time in the future.
- [func startForegroundDownload(BADownload) throws](badownloadmanager/startforegrounddownload(_:).md)
  Schedules an asset download that executes immediately in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanager/cancel(_:))*