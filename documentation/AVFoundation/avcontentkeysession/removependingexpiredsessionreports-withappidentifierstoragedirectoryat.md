# removePendingExpiredSessionReports(_:withAppIdentifier:storageDirectoryAt:)

**Framework**: AVFoundation  
**Kind**: method

Removes expired session reports from storage.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func removePendingExpiredSessionReports(_ expiredSessionReports: [Data], withAppIdentifier appIdentifier: Data, storageDirectoryAt storageURL: URL)
```

## Parameters

- `expiredSessionReports`: An array of expired session reports to delete.
- `appIdentifier`: The opaque identifier for the app.
- `storageURL`: The URL that points to the directory containing expired session reports.

## See Also

- [class func pendingExpiredSessionReports(withAppIdentifier: Data, storageDirectoryAt: URL) -> [Data]](avcontentkeysession/pendingexpiredsessionreports(withappidentifier:storagedirectoryat:).md)
  Returns the expired session reports for content key sessions created with the specified app identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/removependingexpiredsessionreports(_:withappidentifier:storagedirectoryat:))*