# automaticallySync

**Framework**: CloudKit  
**Kind**: property

A Boolean value that determines whether the engine syncs automatically.

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
var automaticallySync: Bool
```

#### Discussion

By default, the sync engine uses the system scheduler to automatically schedule both send and fetch operations. If an operation fails due to a recoverable error, such as a network failure or when the server is enforcing request limits, the engine reschedules those operations as necessary. Unless you have a specific need, prefer to use the default behavior in your app.

If you set this property’s value to [`false`](https://developer.apple.com/documentation/Swift/false), use [`fetchChanges(_:)`](cksyncengine-5sie5/fetchchanges(_:).md) and [`sendChanges(_:)`](cksyncengine-5sie5/sendchanges(_:).md) to invoke immediate sync operations, allowing for more control over when your app syncs its records. For example, you may want to sync at a specific time of day or deterministically simulate certain conditions in your unit tests.

The default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var database: CKDatabase](cksyncengine-5sie5/configuration/database.md)
  The associated database.
- [var subscriptionID: CKSubscription.ID?](cksyncengine-5sie5/configuration/subscriptionid.md)
  The subscription identifier for the associated database.
- [var stateSerialization: CKSyncEngine.State.Serialization?](cksyncengine-5sie5/configuration/stateserialization.md)
  The sync engine’s serialized state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/configuration/automaticallysync)*