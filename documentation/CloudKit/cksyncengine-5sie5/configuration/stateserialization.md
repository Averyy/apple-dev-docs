# stateSerialization

**Framework**: CloudKit  
**Kind**: property

The sync engine’s serialized state.

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
var stateSerialization: CKSyncEngine.State.Serialization?
```

#### Discussion

This property returns the value you specify for the initializer’s `stateSerialization` parameter. If you choose to set this property after initialization, assign the state from the most recent [`CKSyncEngine.Event.stateUpdate(_:)`](cksyncengine-5sie5/event/stateupdate(_:).md) event handled by your delegate. However, If this is the first initialization of the associated sync engine, specify `nil` instead.

The default value is `nil`.

## See Also

- [var automaticallySync: Bool](cksyncengine-5sie5/configuration/automaticallysync.md)
  A Boolean value that determines whether the engine syncs automatically.
- [var database: CKDatabase](cksyncengine-5sie5/configuration/database.md)
  The associated database.
- [var subscriptionID: CKSubscription.ID?](cksyncengine-5sie5/configuration/subscriptionid.md)
  The subscription identifier for the associated database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/configuration/stateserialization)*