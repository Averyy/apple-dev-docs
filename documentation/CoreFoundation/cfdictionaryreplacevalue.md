# CFDictionaryReplaceValue(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Replaces a value corresponding to a given key.

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
func CFDictionaryReplaceValue(_ theDict: CFMutableDictionary!, _ key: UnsafeRawPointer!, _ value: UnsafeRawPointer!)
```

## Parameters

- `theDict`: The dictionary to modify.
- `key`: The key of the value to replace in  . If a key which matches   is present in the dictionary, the value is changed to the  , otherwise this function does nothing (“replace if present”).
- `value`: The new value for  . The   object is retained by   using the retain callback provided when   was created, and the old value is released.   must be of the type expected by the retain and release callbacks.

## See Also

- [func CFDictionaryAddValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](cfdictionaryaddvalue(_:_:_:).md)
  Adds a key-value pair to a dictionary if the specified key is not already present.
- [func CFDictionaryRemoveAllValues(CFMutableDictionary!)](cfdictionaryremoveallvalues(_:).md)
  Removes all the key-value pairs from a dictionary, making it empty.
- [func CFDictionaryRemoveValue(CFMutableDictionary!, UnsafeRawPointer!)](cfdictionaryremovevalue(_:_:).md)
  Removes a key-value pair.
- [func CFDictionarySetValue(CFMutableDictionary!, UnsafeRawPointer!, UnsafeRawPointer!)](cfdictionarysetvalue(_:_:_:).md)
  Sets the value corresponding to a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionaryreplacevalue(_:_:_:))*