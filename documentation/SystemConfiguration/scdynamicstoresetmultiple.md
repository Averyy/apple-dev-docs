# SCDynamicStoreSetMultiple(_:_:_:_:)

**Framework**: System Configuration  
**Kind**: func

Updates multiple values in the dynamic store.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreSetMultiple(_ store: SCDynamicStore?, _ keysToSet: CFDictionary?, _ keysToRemove: CFArray?, _ keysToNotify: CFArray?) -> Bool
```

#### Return Value

`TRUE` if the dynamic store updates were successful; otherwise, `FALSE`.

## Parameters

- `store`: The dynamic store session.
- `keysToSet`: A dictionary of key-value pairs to add to the dynamic store.
- `keysToRemove`: An array of keys to remove from the dynamic store.
- `keysToNotify`: An array of keys to flag as changed (without changing their values).

## See Also

- [func SCDynamicStoreAddTemporaryValue(SCDynamicStore, CFString, CFPropertyList) -> Bool](scdynamicstoreaddtemporaryvalue(_:_:_:).md)
  Temporarily adds the specified key-value pair to the dynamic store, if no such key already exists.
- [func SCDynamicStoreAddValue(SCDynamicStore?, CFString, CFPropertyList) -> Bool](scdynamicstoreaddvalue(_:_:_:).md)
  Adds the specified key-value pair to the dynamic store, if no such key already exists.
- [func SCDynamicStoreSetValue(SCDynamicStore?, CFString, CFPropertyList) -> Bool](scdynamicstoresetvalue(_:_:_:).md)
  Adds or replaces a value in the dynamic store for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstoresetmultiple(_:_:_:_:))*