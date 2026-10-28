# SCDynamicStoreSetNotificationKeys(_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Specifies a set of keys and key patterns that should be monitored for changes.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreSetNotificationKeys(_ store: SCDynamicStore, _ keys: CFArray?, _ patterns: CFArray?) -> Bool
```

```c
Boolean SCDynamicStoreSetNotificationKeys(SCDynamicStoreRef store, CFArrayRef keys, CFArrayRef patterns);
```

## Return Value

`TRUE` if the set of notification keys and patterns was successfully updated; otherwise, `FALSE`.

## Parameters

- `store`: The dynamic store session being watched.
- `keys`: An array of keys to be monitored or `NULL` if no specific keys are to be monitored.
- `patterns`: An array of regex(3) pattern strings used to match keys to be monitored or `NULL` if no key patterns are to be monitored.

## See Also

### Monitoring Keys and Values
- [func SCDynamicStoreNotifyValue(SCDynamicStore?, CFString) -> Bool](./scdynamicstorenotifyvalue%28_,_%29.md)
  Causes a notification to be delivered for the specified key in the dynamic store.
- [func SCDynamicStoreSetDispatchQueue(SCDynamicStore, dispatch_queue_t?) -> Bool](./scdynamicstoresetdispatchqueue%28_,_%29.md)
  Initiates notifications for the notification keys, using the specified dispatch queue for the callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstoresetnotificationkeys(_:_:_:))*