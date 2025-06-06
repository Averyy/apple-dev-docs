# SCDynamicStoreSetValue(_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Adds or replaces a value in the dynamic store for the specified key.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreSetValue(_ store: SCDynamicStore?, _ key: CFString, _ value: CFPropertyList) -> Bool
```

#### Return Value

`TRUE` if the key was updated; otherwise, `FALSE`.

## Parameters

- `store`: The dynamic store session.
- `key`: The key associated with the value.
- `value`: The value to add to or replace in the dynamic store.

## See Also

- [func SCDynamicStoreAddTemporaryValue(SCDynamicStore, CFString, CFPropertyList) -> Bool](scdynamicstoreaddtemporaryvalue(_:_:_:).md)
  Temporarily adds the specified key-value pair to the dynamic store, if no such key already exists.
- [func SCDynamicStoreAddValue(SCDynamicStore?, CFString, CFPropertyList) -> Bool](scdynamicstoreaddvalue(_:_:_:).md)
  Adds the specified key-value pair to the dynamic store, if no such key already exists.
- [func SCDynamicStoreSetMultiple(SCDynamicStore?, CFDictionary?, CFArray?, CFArray?) -> Bool](scdynamicstoresetmultiple(_:_:_:_:).md)
  Updates multiple values in the dynamic store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstoresetvalue(_:_:_:))*