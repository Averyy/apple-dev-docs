# SCDynamicStoreCopyMultiple(_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Returns the key-value pairs that match the specified keys and key patterns.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreCopyMultiple(_ store: SCDynamicStore?, _ keys: CFArray?, _ patterns: CFArray?) -> CFDictionary?
```

#### Return Value

A dictionary of key-value pairs that match the specified keys and key patterns, or `NULL` if an error occurred. You must release the returned value.

## Parameters

- `store`: The dynamic store session.
- `keys`: The keys associated with the desired values or   if no specific keys are requested.
- `patterns`: An array of regex(3) pattern strings used to match the keys, or   if no key patterns are requested.

## See Also

- [func SCDynamicStoreCopyKeyList(SCDynamicStore?, CFString) -> CFArray?](scdynamicstorecopykeylist(_:_:).md)
  Returns the keys that represent the current dynamic store entries that match the specified pattern.
- [func SCDynamicStoreCopyNotifiedKeys(SCDynamicStore) -> CFArray?](scdynamicstorecopynotifiedkeys(_:).md)
  Returns the keys that have changed since the last call to this function.
- [func SCDynamicStoreCopyValue(SCDynamicStore?, CFString) -> CFPropertyList?](scdynamicstorecopyvalue(_:_:).md)
  Returns the value associated with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecopymultiple(_:_:_:))*