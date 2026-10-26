# initWithDatabase:stateSerialization:delegate:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Creates a configuration for the specified database and serialized state.

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
- (instancetype) initWithDatabase:(CKDatabase *) database stateSerialization:(CKSyncEngineStateSerialization *) stateSerialization delegate:(id<CKSyncEngineDelegate>) delegate;
```

#### Return Value

An initialized configuration instance.

## Parameters

- `database`: The database to sync — either a person’s private database or their shared database.
- `stateSerialization`: If this is the first initialization of the associated sync engine, specify `nil`; otherwise, specify the state from the most recent [`CKSyncEngineStateUpdateEvent`](../cksyncenginestateupdateevent.md) that your delegate handled.
- `delegate`: The object that provides the records to sync and handles any related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengineconfiguration/initwithdatabase:stateserialization:delegate:)*