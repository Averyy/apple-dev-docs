# sendChanges(_:)

**Framework**: CloudKit  
**Kind**: method

Sends pending local changes to the server.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
final func sendChanges(_ options: CKSyncEngine.SendChangesOptions = .init()) async throws
```

#### Discussion

Use this method to ensure the sync engine sends all pending local changes to the server before your app continues. This isn’t necessary in normal use, as the engine automatically syncs your app’s records. It is useful, however, in scenarios where you require greater control over sync, such as a “Backup now” button or unit tests.

> **Note**:  [`sendChanges(_:)`](cksyncengine-5sie5/sendchanges(_:).md) returns only after your sync delegate finishes processing all related send events.

## Parameters

- `options`: The options to use when sending changes. For more information, see  .

## See Also

- [func fetchChanges(CKSyncEngine.FetchChangesOptions) async throws](cksyncengine-5sie5/fetchchanges(_:).md)
  Fetches pending remote changes from the server.
- [CKSyncEngine.FetchChangesOptions](cksyncengine-5sie5/fetchchangesoptions.md)
  A set of options to use with a fetch operation.
- [CKSyncEngine.SendChangesOptions](cksyncengine-5sie5/sendchangesoptions.md)
  A set of options to use with a send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/sendchanges(_:))*