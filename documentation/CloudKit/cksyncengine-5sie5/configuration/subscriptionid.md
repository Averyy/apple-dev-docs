# subscriptionID

**Framework**: CloudKit  
**Kind**: property

The subscription identifier for the associated database.

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
var subscriptionID: CKSubscription.ID?
```

#### Discussion

By default, a sync engine attempts to discover an existing subscription for the synced database. If one isn’t found, the engine creates an internal [`CKDatabaseSubscription`](ckdatabasesubscription.md) and uses that to receive notifications about remote record changes.

If you require the sync engine to use a specific database subscription, assign that subscription’s identifier to this property. Doing so enables your app to be backwards compatible if you’re migrating to [`CKSyncEngine`](cksyncengine-5sie5.md) from a custom CloudKit sync implementation.

The default value is `nil`.

## See Also

- [var automaticallySync: Bool](cksyncengine-5sie5/configuration/automaticallysync.md)
  A Boolean value that determines whether the engine syncs automatically.
- [var database: CKDatabase](cksyncengine-5sie5/configuration/database.md)
  The associated database.
- [var stateSerialization: CKSyncEngine.State.Serialization?](cksyncengine-5sie5/configuration/stateserialization.md)
  The sync engine’s serialized state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/configuration/subscriptionid)*