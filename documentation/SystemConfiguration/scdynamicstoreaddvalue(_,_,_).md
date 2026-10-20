# SCDynamicStoreAddValue(_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Adds the specified key-value pair to the dynamic store, if no such key already exists.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreAddValue(_ store: SCDynamicStore?, _ key: CFString, _ value: CFPropertyList) -> Bool
```

```c
Boolean SCDynamicStoreAddValue(SCDynamicStoreRef store, CFStringRef key, CFPropertyListRef value);
```

#### Return Value

`TRUE` if the key was added; `FALSE` if the key was already present in the dynamic store or if an error occurred.

## Parameters

- `store`: The dynamic store session.
- `key`: The key of the value to add to the dynamic store.
- `value`: The value to add to the dynamic store.

## See Also

### Adding or Updating Keys and Values
- [func SCDynamicStoreAddTemporaryValue(SCDynamicStore, CFString, CFPropertyList) -> Bool](./scdynamicstoreaddtemporaryvalue%28_,_,_%29.md)
  Temporarily adds the specified key-value pair to the dynamic store, if no such key already exists.
- [func SCDynamicStoreSetMultiple(SCDynamicStore?, CFDictionary?, CFArray?, CFArray?) -> Bool](./scdynamicstoresetmultiple%28_,_,_,_%29.md)
  Updates multiple values in the dynamic store.
- [func SCDynamicStoreSetValue(SCDynamicStore?, CFString, CFPropertyList) -> Bool](./scdynamicstoresetvalue%28_,_,_%29.md)
  Adds or replaces a value in the dynamic store for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstoreaddvalue(_:_:_:))*