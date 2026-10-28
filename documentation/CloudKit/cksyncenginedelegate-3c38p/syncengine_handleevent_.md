# syncEngine:handleEvent:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate to handle the specified sync event.

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
- (void) syncEngine:(CKSyncEngine *) syncEngine handleEvent:(CKSyncEngineEvent *) event;
```

## Discussion

> ❗ **Important**: If `event` is an instance of [`CKSyncEngineStateUpdateEvent`](../cksyncenginestateupdateevent.md), you must persist the attached state to disk alongside your app data. The sync engine requires you to provide it with the most recent serialized state at initialization, and it’s your responsibility to make sure this is available across app launches.

The sync engine provides events serially; your delegate won’t receive the subsequent event until it finishes processing the current one and returns from this method.

## Parameters

- `syncEngine`: The sync engine that generates the event.
- `event`: Information about the event. An event may occur for a number of reasons, such as when new data is available or when the device’s iCloud account changes. For more information, see [`CKSyncEngineEvent`](../cksyncengineevent.md).

## See Also

### Handling sync events
- [CKSyncEngineEvent](../cksyncengineevent.md)
  An event that occurs during a sync operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginedelegate-3c38p/syncengine:handleevent:)*