# CFDictionarySetValue(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets the value corresponding to a given key.

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
func CFDictionarySetValue(_ theDict: CFMutableDictionary!, _ key: UnsafeRawPointer!, _ value: UnsafeRawPointer!)
```

## Parameters

- `theDict`: The dictionary to modify. If this parameter is a fixed-capacity dictionary and it is full before this operation, and the key does not exist in the dictionary, the behavior is undefined.
- `key`: If a key-value pair is added, both   and   are retained by the dictionary, using the retain callback provided when   was created.   must be of the type expected by the key retain callback.
- `value`: The value to add to or replace in  .   is retained using the value retain callback provided when   was created, and the previous value if any is released.   must be of the type expected by the retain and release callbacks.

## See Also

- [func CFDictionaryAddValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](cfdictionaryaddvalue(_:_:_:).md)
  Adds a key-value pair to a dictionary if the specified key is not already present.
- [func CFDictionaryRemoveAllValues(CFMutableDictionary!)](cfdictionaryremoveallvalues(_:).md)
  Removes all the key-value pairs from a dictionary, making it empty.
- [func CFDictionaryRemoveValue(CFMutableDictionary!, UnsafeRawPointer!)](cfdictionaryremovevalue(_:_:).md)
  Removes a key-value pair.
- [func CFDictionaryReplaceValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](cfdictionaryreplacevalue(_:_:_:).md)
  Replaces a value corresponding to a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionarysetvalue(_:_:_:))*