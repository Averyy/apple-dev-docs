# handleEvent(_:syncEngine:)

**Framework**: CloudKit  
**Kind**: method  
**Required**: Yes

Tells the delegate to handle the specified sync event.

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
func handleEvent(_ event: CKSyncEngine.Event, syncEngine: CKSyncEngine) async
```

#### Discussion

> ❗ **Important**:  On receipt of a [`CKSyncEngine.Event.stateUpdate(_:)`](cksyncengine-5sie5/event/stateupdate(_:).md) event, you must persist the attached state to disk alongside your app data. The sync engine requires you to provide it with the most recent serialized state at initialization, and it’s your responsibility to make sure this is available across app launches.

The sync engines provides events serially; your delegate won’t receive the subsequent event until it finishes processing the current one and returns from this method.

## Parameters

- `event`: Information about the event. An event may occur for a number of reasons, such as when new data is available or when the device’s iCloud account changes. For more information, see  .
- `syncEngine`: The sync engine that generates the event.

## See Also

- [CKSyncEngine.Event](cksyncengine-5sie5/event.md)
  Describes an event that occurs during a sync operation.
- [enum CKSyncEngineEventType](cksyncengineeventtype.md)
  Describes an event that occurs during a sync operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginedelegate-1q7g8/handleevent(_:syncengine:))*