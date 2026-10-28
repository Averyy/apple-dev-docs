# stateSerialization

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The sync engine’s serialized state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
var stateSerialization: CKSyncEngine.State.Serialization?
```

## Discussion

This property returns the value you specify for the initializer’s `stateSerialization` parameter. If you choose to set this property after initialization, assign the state from the most recent [`CKSyncEngine.Event.stateUpdate(_:)`](../event/stateupdate%28_%29.md) event handled by your delegate. However, if this is the first initialization of the associated sync engine, specify `nil` instead.

The default value is `nil`.

## See Also

### Managing attributes
- [var automaticallySync: Bool](./automaticallysync.md)
  A Boolean value that determines whether the engine syncs automatically.
- [var database: CKDatabase](./database.md)
  The associated database.
- [var subscriptionID: CKSubscription.ID?](./subscriptionid.md)
  The subscription identifier for the associated database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/configuration/stateserialization)*