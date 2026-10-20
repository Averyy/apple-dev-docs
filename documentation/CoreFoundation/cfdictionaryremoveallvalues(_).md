# CFDictionaryRemoveAllValues(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Removes all the key-value pairs from a dictionary, making it empty.

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
func CFDictionaryRemoveAllValues(_ theDict: CFMutableDictionary!)
```

```c
extern void CFDictionaryRemoveAllValues(CFMutableDictionaryRef theDict);
```

## Parameters

- `theDict`: The dictionary to modify.

## See Also

### Modifying a Dictionary
- [func CFDictionaryAddValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](./cfdictionaryaddvalue%28_,_,_%29.md)
  Adds a key-value pair to a dictionary if the specified key is not already present.
- [func CFDictionaryRemoveValue(CFMutableDictionary!, UnsafeRawPointer!)](./cfdictionaryremovevalue%28_,_%29.md)
  Removes a key-value pair.
- [func CFDictionaryReplaceValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](./cfdictionaryreplacevalue%28_,_,_%29.md)
  Replaces a value corresponding to a given key.
- [func CFDictionarySetValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](./cfdictionarysetvalue%28_,_,_%29.md)
  Sets the value corresponding to a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionaryremoveallvalues(_:))*