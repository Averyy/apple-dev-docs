# SCDynamicStoreSetDispatchQueue(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Initiates notifications for the notification keys, using the specified dispatch queue for the callback.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func SCDynamicStoreSetDispatchQueue(_ store: SCDynamicStore, _ queue: dispatch_queue_t?) -> Bool
```

```c
Boolean SCDynamicStoreSetDispatchQueue(SCDynamicStoreRef store, dispatch_queue_t queue);
```

#### Return Value

`TRUE` if notifications were successfully initiated; otherwise, `FALSE`.

## Parameters

- `store`: The dynamic store session.
- `queue`: The dispatch queue on which to run the callback function. Pass `NULL` to disable notifications and release the queue.

## See Also

### Monitoring Keys and Values
- [func SCDynamicStoreNotifyValue(SCDynamicStore?, CFString) -> Bool](./scdynamicstorenotifyvalue%28_,_%29.md)
  Causes a notification to be delivered for the specified key in the dynamic store.
- [func SCDynamicStoreSetNotificationKeys(SCDynamicStore, CFArray?, CFArray?) -> Bool](./scdynamicstoresetnotificationkeys%28_,_,_%29.md)
  Specifies a set of keys and key patterns that should be monitored for changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstoresetdispatchqueue(_:_:))*