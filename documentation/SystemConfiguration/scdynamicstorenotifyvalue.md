# SCDynamicStoreNotifyValue(_:_:)

**Framework**: System Configuration  
**Kind**: func

Causes a notification to be delivered for the specified key in the dynamic store.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreNotifyValue(_ store: SCDynamicStore?, _ key: CFString) -> Bool
```

#### Return Value

`TRUE` if the notification was processed; `FALSE` if an error occurred.

## Parameters

- `store`: The dynamic store session.
- `key`: The key that should be flagged as changed. All dynamic store sessions that are monitoring this key will receive a notification. Note that the key’s value is not updated.

## See Also

- [func SCDynamicStoreSetNotificationKeys(SCDynamicStore, CFArray?, CFArray?) -> Bool](scdynamicstoresetnotificationkeys(_:_:_:).md)
  Specifies a set of keys and key patterns that should be monitored for changes.
- [func SCDynamicStoreSetDispatchQueue(SCDynamicStore, dispatch_queue_t?) -> Bool](scdynamicstoresetdispatchqueue(_:_:).md)
  Initiates notifications for the notification keys, using the specified dispatch queue for the callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorenotifyvalue(_:_:))*