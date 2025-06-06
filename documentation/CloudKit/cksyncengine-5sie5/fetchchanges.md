# fetchChanges(_:)

**Framework**: CloudKit  
**Kind**: method

Fetches pending remote changes from the server.

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
final func fetchChanges(_ options: CKSyncEngine.FetchChangesOptions = .init()) async throws
```

#### Discussion

Use this method to ensure the sync engine immediately fetches all pending remote changes before your app continues. This isn’t necessary in normal use, as the engine automatically syncs your app’s records. It is useful, however, in scenarios where you require more control over sync, such as pull-to-refresh or unit tests.

> **Note**:  [`fetchChanges(_:)`](cksyncengine-5sie5/fetchchanges(_:).md) returns only after your sync delegate finishes processing all related fetch events.

 [`fetchChanges(_:)`](cksyncengine-5sie5/fetchchanges(_:).md) returns only after your sync delegate finishes processing all related fetch events.

## Parameters

- `options`: The options to use when fetching changes. For more information, see  .

## See Also

- [CKSyncEngine.FetchChangesOptions](cksyncengine-5sie5/fetchchangesoptions.md)
  A set of options to use with a fetch operation.
- [func sendChanges(CKSyncEngine.SendChangesOptions) async throws](cksyncengine-5sie5/sendchanges(_:).md)
  Sends pending local changes to the server.
- [CKSyncEngine.SendChangesOptions](cksyncengine-5sie5/sendchangesoptions.md)
  A set of options to use with a send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/fetchchanges(_:))*