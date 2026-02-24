# init(database:stateSerialization:delegate:)

**Framework**: CloudKit  
**Kind**: init

Creates a configuration for the specified database and serialized state.

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
init(database: CKDatabase, stateSerialization: CKSyncEngine.State.Serialization?, delegate: any CKSyncEngineDelegate)
```

## Parameters

- `database`: The database to sync — either a person’s private database or their shared database.
- `stateSerialization`: If this is the first initialization of the associated sync engine, specify `nil`; otherwise, specify the state from the most recent [`CKSyncEngine.Event.stateUpdate(_:)`](cksyncengine-5sie5/event/stateupdate(_:).md) event that your delegate handled.
- `delegate`: The object that provides the records to sync and handles any related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/configuration/init(database:stateserialization:delegate:))*