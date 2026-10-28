# CKSyncEngineStateUpdateEvent

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

The sync engine state was updated, and you should persist it locally.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@interface CKSyncEngineStateUpdateEvent : CKSyncEngineEvent
```

## Overview

In order to function properly and efficiently, `CKSyncEngine` tracks some state internally. When the sync engine state changes, it gives you the latest serialized version in a [`CKSyncEngine.Event.StateUpdate`](./cksyncengine-5sie5/event/stateupdate.md). This event happens occasionally when the sync engine modifies the state internally during normal sync operation. This event also happens when you change the state yourself.

The sync engine does not persist this state to disk, so you need to persist it alongside your own local data. The next time your process launches, use this latest state serialization in [`stateSerialization`](./cksyncengineconfiguration/stateserialization.md) to initialize your sync engine.

This state is directly tied to the changes you fetch and send with the sync engine. You should persist this state alongside any changes fetched prior to receiving this state.

## Topics

### Accessing the state
- [stateSerialization](./cksyncenginestateupdateevent/stateserialization.md)
  The current state of the sync engine.
- [CKSyncEngineStateSerialization](./cksyncenginestateserialization.md)
  An opaque object that contains the serialized representation of a sync engine’s current state.

## Relationships

### Inherits From
- [CKSyncEngineEvent](./cksyncengineevent.md)

## See Also

### Accessing state updates
- [stateUpdateEvent](./cksyncengineevent/stateupdateevent.md)
  The event downcast to the subclass that represents an update to the sync engine’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginestateupdateevent)*