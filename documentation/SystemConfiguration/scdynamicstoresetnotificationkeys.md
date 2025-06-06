# SCDynamicStoreSetNotificationKeys(_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Specifies a set of keys and key patterns that should be monitored for changes.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreSetNotificationKeys(_ store: SCDynamicStore, _ keys: CFArray?, _ patterns: CFArray?) -> Bool
```

#### Return Value

`TRUE` if the set of notification keys and patterns was successfully updated; otherwise, `FALSE`.

## Parameters

- `store`: The dynamic store session being watched.
- `keys`: An array of keys to be monitored or   if no specific keys are to be monitored.
- `patterns`: An array of regex(3) pattern strings used to match keys to be monitored or   if no key patterns are to be monitored.

## See Also

- [func SCDynamicStoreNotifyValue(SCDynamicStore?, CFString) -> Bool](scdynamicstorenotifyvalue(_:_:).md)
  Causes a notification to be delivered for the specified key in the dynamic store.
- [func SCDynamicStoreSetDispatchQueue(SCDynamicStore, dispatch_queue_t?) -> Bool](scdynamicstoresetdispatchqueue(_:_:).md)
  Initiates notifications for the notification keys, using the specified dispatch queue for the callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstoresetnotificationkeys(_:_:_:))*