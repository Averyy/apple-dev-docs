# SCDynamicStoreSetValue(_:_:_:)

**Framework**: System Configuration  
**Kind**: func  
**Role**: Function

Adds or replaces a value in the dynamic store for the specified key.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func SCDynamicStoreSetValue(_ store: SCDynamicStore?, _ key: CFString, _ value: CFPropertyList) -> Bool
```

```c
Boolean SCDynamicStoreSetValue(SCDynamicStoreRef store, CFStringRef key, CFPropertyListRef value);
```

## Return Value

`TRUE` if the key was updated; otherwise, `FALSE`.

## Parameters

- `store`: The dynamic store session.
- `key`: The key associated with the value.
- `value`: The value to add to or replace in the dynamic store.

## See Also

### Adding or Updating Keys and Values
- [func SCDynamicStoreAddTemporaryValue(SCDynamicStore, CFString, CFPropertyList) -> Bool](./scdynamicstoreaddtemporaryvalue%28_,_,_%29.md)
  Temporarily adds the specified key-value pair to the dynamic store, if no such key already exists.
- [func SCDynamicStoreAddValue(SCDynamicStore?, CFString, CFPropertyList) -> Bool](./scdynamicstoreaddvalue%28_,_,_%29.md)
  Adds the specified key-value pair to the dynamic store, if no such key already exists.
- [func SCDynamicStoreSetMultiple(SCDynamicStore?, CFDictionary?, CFArray?, CFArray?) -> Bool](./scdynamicstoresetmultiple%28_,_,_,_%29.md)
  Updates multiple values in the dynamic store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/scdynamicstoresetvalue(_:_:_:))*