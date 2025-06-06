# SCDynamicStoreAddTemporaryValue(_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Temporarily adds the specified key-value pair to the dynamic store, if no such key already exists.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreAddTemporaryValue(_ store: SCDynamicStore, _ key: CFString, _ value: CFPropertyList) -> Bool
```

#### Return Value

`TRUE` if the key was added; `FALSE` if the key was already present in the dynamic store or if an error occurred.

#### Discussion

Unless the key is updated by another session, the key-value pair added by this function is removed automatically when the session is closed.

## Parameters

- `store`: The dynamic store session.
- `key`: The key of the value to add to the dynamic store.
- `value`: The value to add to the dynamic store.

## See Also

- [func SCDynamicStoreAddValue(SCDynamicStore?, CFString, CFPropertyList) -> Bool](scdynamicstoreaddvalue(_:_:_:).md)
  Adds the specified key-value pair to the dynamic store, if no such key already exists.
- [func SCDynamicStoreSetMultiple(SCDynamicStore?, CFDictionary?, CFArray?, CFArray?) -> Bool](scdynamicstoresetmultiple(_:_:_:_:).md)
  Updates multiple values in the dynamic store.
- [func SCDynamicStoreSetValue(SCDynamicStore?, CFString, CFPropertyList) -> Bool](scdynamicstoresetvalue(_:_:_:).md)
  Adds or replaces a value in the dynamic store for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstoreaddtemporaryvalue(_:_:_:))*