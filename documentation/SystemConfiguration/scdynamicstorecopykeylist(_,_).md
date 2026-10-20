# SCDynamicStoreCopyKeyList(_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Returns the keys that represent the current dynamic store entries that match the specified pattern.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreCopyKeyList(_ store: SCDynamicStore?, _ pattern: CFString) -> CFArray?
```

```c
CFArrayRefSCDynamicStoreCopyKeyList(SCDynamicStoreRef store, CFStringRef pattern);
```

#### Return Value

An array of matching keys, or `NULL` if an error occurred. You must release the returned value.

## Parameters

- `store`: The dynamic store session.
- `pattern`: A regex(3) regular expression pattern used to match the dynamic store keys.

## See Also

### Getting Keys and Values
- [func SCDynamicStoreCopyMultiple(SCDynamicStore?, CFArray?, CFArray?) -> CFDictionary?](./scdynamicstorecopymultiple%28_,_,_%29.md)
  Returns the key-value pairs that match the specified keys and key patterns.
- [func SCDynamicStoreCopyNotifiedKeys(SCDynamicStore) -> CFArray?](./scdynamicstorecopynotifiedkeys%28_%29.md)
  Returns the keys that have changed since the last call to this function.
- [func SCDynamicStoreCopyValue(SCDynamicStore?, CFString) -> CFPropertyList?](./scdynamicstorecopyvalue%28_,_%29.md)
  Returns the value associated with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstorecopykeylist(_:_:))*