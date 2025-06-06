# CFDictionaryGetValueIfPresent(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a Boolean value that indicates whether a given value for a given key is in a dictionary, and returns that value indirectly if it exists.

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
func CFDictionaryGetValueIfPresent(_ theDict: CFDictionary!, _ key: UnsafeRawPointer!, _ value: UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool
```

#### Return Value

`true` if a matching key was found, otherwise `false`.

## Parameters

- `theDict`: The dictionary to examine.
- `key`: The key for which to find a match in  . The key hash and equal callbacks provided when the dictionary was created are used to compare. If the hash callback was  ,   is treated as a pointer and converted to an integer. If the equal callback was  , pointer equality (in C, ==) is used. If  , or any of the keys in  , is not understood by the equal callback, the behavior is undefined.
- `value`: A pointer to memory which, on return, is filled with the pointer-sized value if a matching key is found. If no key match is found, the contents of the storage pointed to by this parameter are undefined. This value may be  , in which case the value from the dictionary is not returned (but the return value of this function still indicates whether or not the key-value pair was present). If the value is a Core Foundation object, ownership follows the  .

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
- [func CFDictionaryGetKeysAndValues(CFDictionary!, UnsafeMutablePointer<UnsafeRawPointer?>!, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfdictionarygetkeysandvalues(_:_:_:).md)
  Fills two buffers with the keys and values from a dictionary.
- [func CFDictionaryGetValue(CFDictionary!, UnsafeRawPointer!) -> UnsafeRawPointer!](cfdictionarygetvalue(_:_:).md)
  Returns the value associated with a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionarygetvalueifpresent(_:_:_:))*