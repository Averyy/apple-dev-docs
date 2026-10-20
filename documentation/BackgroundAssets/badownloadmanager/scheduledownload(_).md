# scheduleDownload(_:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) scheduleDownload:(BADownload *) download error:(NSError **) error;
```

## Parameters

- `download`: The object that provides the URL of the asset to download.

## See Also

### Managing downloads
- [func startForegroundDownload(BADownload) throws](./startforegrounddownload%28_%29.md)
  Schedules an asset download that executes immediately in the foreground.
- [func cancel(BADownload) throws](./cancel%28_%29.md)
  Cancels an asset download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanager/scheduledownload(_:))*