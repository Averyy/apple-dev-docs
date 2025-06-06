# CFDictionaryGetCountOfKey(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the number of times a key occurs in a dictionary.

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
func CFDictionaryGetCountOfKey(_ theDict: CFDictionary!, _ key: UnsafeRawPointer!) -> CFIndex
```

#### Return Value

Returns `1` if a matching key is used by the dictionary, otherwise `0`.

## Parameters

- `theDict`: The dictionary to examine.
- `key`: The key for which to find matches in  . The key hash and equal callbacks provided when the dictionary was created are used to compare. If the hash callback was  , the key is treated as a pointer and converted to an integer. If the equal callback was  , pointer equality (in C, ==) is used. If  , or any of the keys in the dictionary, is not understood by the equal callback, the behavior is undefined.

## See Also

- [func CFDictionaryContainsKey(CFDictionary!, UnsafeRawPointer!) -> Bool](cfdictionarycontainskey(_:_:).md)
  Returns a Boolean value that indicates whether a given key is in a dictionary.
- [func CFDictionaryContainsValue(CFDictionary!, UnsafeRawPointer!) -> Bool](cfdictionarycontainsvalue(_:_:).md)
  Returns a Boolean value that indicates whether a given value is in a dictionary.
- [func CFDictionaryGetCount(CFDictionary!) -> CFIndex](cfdictionarygetcount(_:).md)
  Returns the number of key-value pairs in a dictionary.
- [func CFDictionaryGetCountOfValue(CFDictionary!, UnsafeRawPointer!) -> CFIndex](cfdictionarygetcountofvalue(_:_:).md)
  Counts the number of times a given value occurs in the dictionary.
- [func CFDictionaryGetKeysAndValues(CFDictionary!, UnsafeMutablePointer<UnsafeRawPointer?>!, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfdictionarygetkeysandvalues(_:_:_:).md)
  Fills two buffers with the keys and values from a dictionary.
- [func CFDictionaryGetValue(CFDictionary!, UnsafeRawPointer!) -> UnsafeRawPointer!](cfdictionarygetvalue(_:_:).md)
  Returns the value associated with a given key.
- [func CFDictionaryGetValueIfPresent(CFDictionary!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](cfdictionarygetvalueifpresent(_:_:_:).md)
  Returns a Boolean value that indicates whether a given value for a given key is in a dictionary, and returns that value indirectly if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionarygetcountofkey(_:_:))*