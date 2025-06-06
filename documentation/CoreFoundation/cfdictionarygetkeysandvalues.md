# CFDictionaryGetKeysAndValues(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Fills two buffers with the keys and values from a dictionary.

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
func CFDictionaryGetKeysAndValues(_ theDict: CFDictionary!, _ keys: UnsafeMutablePointer<UnsafeRawPointer?>!, _ values: UnsafeMutablePointer<UnsafeRawPointer?>!)
```

## Parameters

- `theDict`: The dictionary to examine.
- `keys`: A C array of pointer-sized values that, on return, is filled with keys from the  . The keys and values C arrays are parallel to each other (that is, the items at the same indices form a key-value pair from the dictionary). This value must be a valid pointer to a C array of the appropriate type and size (that is, a size equal to the count of  ), or   if the keys are not required. If the keys are Core Foundation objects, ownership follows the  .
- `values`: A C array of pointer-sized values that, on return, is filled with values from the  . The keys and values C arrays are parallel to each other (that is, the items at the same indices form a key-value pair from the dictionary). This value must be a valid pointer to a C array of the appropriate type and size (that is, a size equal to the count of  ), or   if the values are not required. If the values are Core Foundation objects, ownership follows the  .

## See Also

- [func CFDictionaryContainsKey(CFDictionary!, UnsafeRawPointer!) -> Bool](cfdictionarycontainskey(_:_:).md)
  Returns a Boolean value that indicates whether a given key is in a dictionary.
- [func CFDictionaryContainsValue(CFDictionary!, UnsafeRawPointer!) -> Bool](cfdictionarycontainsvalue(_:_:).md)
  Returns a Boolean value that indicates whether a given value is in a dictionary.
- [func CFDictionaryGetCount(CFDictionary!) -> CFIndex](cfdictionarygetcount(_:).md)
  Returns the number of key-value pairs in a dictionary.
- [func CFDictionaryGetCountOfKey(CFDictionary!, UnsafeRawPointer!) -> CFIndex](cfdictionarygetcountofkey(_:_:).md)
  Returns the number of times a key occurs in a dictionary.
- [func CFDictionaryGetCountOfValue(CFDictionary!, UnsafeRawPointer!) -> CFIndex](cfdictionarygetcountofvalue(_:_:).md)
  Counts the number of times a given value occurs in the dictionary.
- [func CFDictionaryGetValue(CFDictionary!, UnsafeRawPointer!) -> UnsafeRawPointer!](cfdictionarygetvalue(_:_:).md)
  Returns the value associated with a given key.
- [func CFDictionaryGetValueIfPresent(CFDictionary!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](cfdictionarygetvalueifpresent(_:_:_:).md)
  Returns a Boolean value that indicates whether a given value for a given key is in a dictionary, and returns that value indirectly if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionarygetkeysandvalues(_:_:_:))*