# CFDictionaryRemoveValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Removes a key-value pair.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFDictionaryRemoveValue(_ theDict: CFMutableDictionary!, _ key: UnsafeRawPointer!)
```

## Parameters

- `theDict`: The dictionary to modify.
- `key`: The key of the value to remove from  . If a key which matches   is present in  , the key-value pair is removed from the dictionary, otherwise this function does nothing (“remove if present”).

## See Also

- [func CFDictionaryAddValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](cfdictionaryaddvalue(_:_:_:).md)
  Adds a key-value pair to a dictionary if the specified key is not already present.
- [func CFDictionaryRemoveAllValues(CFMutableDictionary!)](cfdictionaryremoveallvalues(_:).md)
  Removes all the key-value pairs from a dictionary, making it empty.
- [func CFDictionaryReplaceValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](cfdictionaryreplacevalue(_:_:_:).md)
  Replaces a value corresponding to a given key.
- [func CFDictionarySetValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](cfdictionarysetvalue(_:_:_:).md)
  Sets the value corresponding to a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionaryremovevalue(_:_:))*