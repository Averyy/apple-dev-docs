# removePendingExpiredSessionReports(_:withAppIdentifier:storageDirectoryAt:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Removes expired session reports from storage.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class func removePendingExpiredSessionReports(_ expiredSessionReports: [Data], withAppIdentifier appIdentifier: Data, storageDirectoryAt storageURL: URL)
```

```objc
+ (void) removePendingExpiredSessionReports:(NSArray<NSData *> *) expiredSessionReports withAppIdentifier:(NSData *) appIdentifier storageDirectoryAtURL:(NSURL *) storageURL;
```

## Parameters

- `expiredSessionReports`: An array of expired session reports to delete.
- `appIdentifier`: The opaque identifier for the app.
- `storageURL`: The URL that points to the directory containing expired session reports.

## See Also

### Handling expired session reports
- [class func pendingExpiredSessionReports(withAppIdentifier: Data, storageDirectoryAt: URL) -> [Data]](./pendingexpiredsessionreports%28withappidentifier,storagedirectoryat%29.md)
  Returns the expired session reports for content key sessions created with the specified app identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/removependingexpiredsessionreports(_:withappidentifier:storagedirectoryat:))*