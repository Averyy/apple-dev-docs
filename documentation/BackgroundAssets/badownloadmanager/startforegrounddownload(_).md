# startForegroundDownload(_:)

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method

Schedules an asset download that executes immediately in the foreground.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
func startForegroundDownload(_ download: BADownload) throws
```

```objc
- (BOOL) startForegroundDownload:(BADownload *) download error:(NSError **) error;
```

## Discussion

Use this method to start new asset downloads immediately, or to promote existing, queued downloads that are yet to start. Only use this method in your app; the framework throws an error if you attempt to start a foreground download in your extension.

## Parameters

- `download`: The object that provides the URL of the asset to download.

## See Also

### Managing downloads
- [func scheduleDownload(BADownload) throws](./scheduledownload%28_%29.md)
  Schedules an asset download to execute in the background at a nonspecific time in the future.
- [func cancel(BADownload) throws](./cancel%28_%29.md)
  Cancels an asset download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloadmanager/startforegrounddownload(_:))*