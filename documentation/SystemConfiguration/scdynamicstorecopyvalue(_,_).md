# SCDynamicStoreCopyValue(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the value associated with the specified key.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreCopyValue(_ store: SCDynamicStore?, _ key: CFString) -> CFPropertyList?
```

```c
CFPropertyListRefSCDynamicStoreCopyValue(SCDynamicStoreRef store, CFStringRef key);
```

#### Return Value

The value associated with the specified key, or `NULL` if no value was located or if an error occurred. You must release the returned value.

## Parameters

- `store`: The dynamic store session.
- `key`: The key associated with the desired value.

## See Also

### Getting Keys and Values
- [func SCDynamicStoreCopyKeyList(SCDynamicStore?, CFString) -> CFArray?](./scdynamicstorecopykeylist%28_,_%29.md)
  Returns the keys that represent the current dynamic store entries that match the specified pattern.
- [func SCDynamicStoreCopyMultiple(SCDynamicStore?, CFArray?, CFArray?) -> CFDictionary?](./scdynamicstorecopymultiple%28_,_,_%29.md)
  Returns the key-value pairs that match the specified keys and key patterns.
- [func SCDynamicStoreCopyNotifiedKeys(SCDynamicStore) -> CFArray?](./scdynamicstorecopynotifiedkeys%28_%29.md)
  Returns the keys that have changed since the last call to this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecopyvalue(_:_:))*