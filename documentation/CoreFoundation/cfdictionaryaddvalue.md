# CFDictionaryAddValue(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Adds a key-value pair to a dictionary if the specified key is not already present.

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
func CFDictionaryAddValue(_ theDict: CFMutableDictionary!, _ key: UnsafeRawPointer!, _ value: UnsafeRawPointer!)
```

## Parameters

- `theDict`: The dictionary to modify. If the dictionary is a fixed-capacity dictionary and it is full before this operation, the behavior is undefined.
- `key`: The key for the value to add to the dictionary—a CFType object or a pointer value. The   is retained by the dictionary using the retain callback provided when the dictionary was created, so must be of the type expected by the callback. If a key which matches   is already present in the dictionary, this function does nothing (“add if absent”).
- `value`: A CFType object or a pointer value to add to the dictionary. The   is retained by the dictionary using the retain callback provided when the dictionary was created, so must be of the type expected by the callback.

## See Also

- [func CFDictionaryRemoveAllValues(CFMutableDictionary!)](cfdictionaryremoveallvalues(_:).md)
  Removes all the key-value pairs from a dictionary, making it empty.
- [func CFDictionaryRemoveValue(CFMutableDictionary!, UnsafeRawPointer!)](cfdictionaryremovevalue(_:_:).md)
  Removes a key-value pair.
- [func CFDictionaryReplaceValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](cfdictionaryreplacevalue(_:_:_:).md)
  Replaces a value corresponding to a given key.
- [func CFDictionarySetValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](cfdictionarysetvalue(_:_:_:).md)
  Sets the value corresponding to a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionaryaddvalue(_:_:_:))*