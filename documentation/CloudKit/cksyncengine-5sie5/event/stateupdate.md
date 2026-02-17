# CKSyncEngine.Event.StateUpdate

**Framework**: CloudKit  
**Kind**: struct

The sync engine state was updated, and you should persist it locally.

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
struct StateUpdate
```

#### Overview

In order to function properly and efficiently, [`CKSyncEngine`](cksyncengine-5sie5.md) tracks some state internally. When the sync engine state changes, it gives you the latest serialized version in a [`CKSyncEngine.Event.StateUpdate`](cksyncengine-5sie5/event/stateupdate.md) event. This event happens occasionally when the sync engine modifies the state internally during normal sync operation. This event also happens when you change the state yourself.

The sync engine does not persist this state to disk, so you need to persist it in alongside your own local data. The next time your process launches, use this latest state serialization in [`stateSerialization`](cksyncengine-5sie5/configuration/stateserialization.md) to initialize your sync engine.

This state is directly tied to the changes you fetch and send with the sync engine. You should persist this state alongside any changes fetched prior to receiving this state.

## Topics

### Accessing the state
- [let stateSerialization: CKSyncEngine.State.Serialization](cksyncengine-5sie5/event/stateupdate/stateserialization.md)
  The current state of the sync engine.
### Debugging the event
- [var description: String](cksyncengine-5sie5/event/stateupdate/description.md)
  A textual description of the event that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](cksyncengine-5sie5/event/stateupdate/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case stateUpdate(CKSyncEngine.Event.StateUpdate)](cksyncengine-5sie5/event/stateupdate(_:).md)
  The sync engine updated its state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/stateupdate)*