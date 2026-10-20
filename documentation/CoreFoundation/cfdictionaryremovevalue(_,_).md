# CFDictionaryRemoveValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Removes a key-value pair.

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
func CFDictionaryRemoveValue(_ theDict: CFMutableDictionary!, _ key: UnsafeRawPointer!)
```

```c
extern void CFDictionaryRemoveValue(CFMutableDictionaryRef theDict, const void *key);
```

## Parameters

- `theDict`: The dictionary to modify.
- `key`: The key of the value to remove from `theDict`. If a key which matches `key` is present in `theDict`, the key-value pair is removed from the dictionary, otherwise this function does nothing (“remove if present”).

## See Also

### Modifying a Dictionary
- [func CFDictionaryAddValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](./cfdictionaryaddvalue%28_,_,_%29.md)
  Adds a key-value pair to a dictionary if the specified key is not already present.
- [func CFDictionaryRemoveAllValues(CFMutableDictionary!)](./cfdictionaryremoveallvalues%28_%29.md)
  Removes all the key-value pairs from a dictionary, making it empty.
- [func CFDictionaryReplaceValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](./cfdictionaryreplacevalue%28_,_,_%29.md)
  Replaces a value corresponding to a given key.
- [func CFDictionarySetValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](./cfdictionarysetvalue%28_,_,_%29.md)
  Sets the value corresponding to a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionaryremovevalue(_:_:))*