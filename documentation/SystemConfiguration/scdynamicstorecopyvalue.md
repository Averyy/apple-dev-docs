# SCDynamicStoreCopyValue(_:_:)

**Framework**: System Configuration  
**Kind**: func

Returns the value associated with the specified key.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreCopyValue(_ store: SCDynamicStore?, _ key: CFString) -> CFPropertyList?
```

#### Return Value

The value associated with the specified key, or `NULL` if no value was located or if an error occurred. You must release the returned value.

## Parameters

- `store`: The dynamic store session.
- `key`: The key associated with the desired value.

## See Also

- [func SCDynamicStoreCopyKeyList(SCDynamicStore?, CFString) -> CFArray?](scdynamicstorecopykeylist(_:_:).md)
  Returns the keys that represent the current dynamic store entries that match the specified pattern.
- [func SCDynamicStoreCopyMultiple(SCDynamicStore?, CFArray?, CFArray?) -> CFDictionary?](scdynamicstorecopymultiple(_:_:_:).md)
  Returns the key-value pairs that match the specified keys and key patterns.
- [func SCDynamicStoreCopyNotifiedKeys(SCDynamicStore) -> CFArray?](scdynamicstorecopynotifiedkeys(_:).md)
  Returns the keys that have changed since the last call to this function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecopyvalue(_:_:))*