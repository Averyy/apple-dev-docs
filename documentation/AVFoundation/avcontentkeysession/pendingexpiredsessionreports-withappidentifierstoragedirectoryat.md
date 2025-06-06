# pendingExpiredSessionReports(withAppIdentifier:storageDirectoryAt:)

**Framework**: AVFoundation  
**Kind**: method

Returns the expired session reports for content key sessions created with the specified app identifier.

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
class func pendingExpiredSessionReports(withAppIdentifier appIdentifier: Data, storageDirectoryAt storageURL: URL) -> [Data]
```

#### Return Value

Returns an array of expired session reports.

#### Discussion

The system only returns expired session reports. It doesn’t include reports for active sessions.

## Parameters

- `appIdentifier`: The opaque identifier for the app.
- `storageURL`: The URL that points to the directory containing expired session reports.

## See Also

- [class func removePendingExpiredSessionReports([Data], withAppIdentifier: Data, storageDirectoryAt: URL)](avcontentkeysession/removependingexpiredsessionreports(_:withappidentifier:storagedirectoryat:).md)
  Removes expired session reports from storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/pendingexpiredsessionreports(withappidentifier:storagedirectoryat:))*