# SCDynamicStoreCopyNotifiedKeys(_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the keys that have changed since the last call to this function.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreCopyNotifiedKeys(_ store: SCDynamicStore) -> CFArray?
```

```c
CFArrayRefSCDynamicStoreCopyNotifiedKeys(SCDynamicStoreRef store);
```

## Return Value

The keys that have changed, or `NULL` if an error occurred. You must release the returned value.

## Discussion

If possible, your application should use the notification functions instead of polling for the list of changed keys returned by this function.

## Parameters

- `store`: The dynamic store session.

## See Also

### Getting Keys and Values
- [func SCDynamicStoreCopyKeyList(SCDynamicStore?, CFString) -> CFArray?](./scdynamicstorecopykeylist%28_,_%29.md)
  Returns the keys that represent the current dynamic store entries that match the specified pattern.
- [func SCDynamicStoreCopyMultiple(SCDynamicStore?, CFArray?, CFArray?) -> CFDictionary?](./scdynamicstorecopymultiple%28_,_,_%29.md)
  Returns the key-value pairs that match the specified keys and key patterns.
- [func SCDynamicStoreCopyValue(SCDynamicStore?, CFString) -> CFPropertyList?](./scdynamicstorecopyvalue%28_,_%29.md)
  Returns the value associated with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecopynotifiedkeys(_:))*