# CFDictionaryReplaceValue(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Replaces a value corresponding to a given key.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFDictionaryReplaceValue(_ theDict: CFMutableDictionary!, _ key: UnsafeRawPointer!, _ value: UnsafeRawPointer!)
```

```c
extern void CFDictionaryReplaceValue(CFMutableDictionaryRef theDict, const void *key, const void *value);
```

## Parameters

- `theDict`: The dictionary to modify.
- `key`: The key of the value to replace in `theDict`. If a key which matches `key` is present in the dictionary, the value is changed to the `value`, otherwise this function does nothing (“replace if present”).
- `value`: The new value for `key`. The `value` object is retained by `theDict` using the retain callback provided when `theDict` was created, and the old value is released. `value` must be of the type expected by the retain and release callbacks.

## See Also

### Modifying a Dictionary
- [func CFDictionaryAddValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](./cfdictionaryaddvalue%28_,_,_%29.md)
  Adds a key-value pair to a dictionary if the specified key is not already present.
- [func CFDictionaryRemoveAllValues(CFMutableDictionary!)](./cfdictionaryremoveallvalues%28_%29.md)
  Removes all the key-value pairs from a dictionary, making it empty.
- [func CFDictionaryRemoveValue(CFMutableDictionary!, UnsafeRawPointer!)](./cfdictionaryremovevalue%28_,_%29.md)
  Removes a key-value pair.
- [func CFDictionarySetValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](./cfdictionarysetvalue%28_,_,_%29.md)
  Sets the value corresponding to a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionaryreplacevalue(_:_:_:))*