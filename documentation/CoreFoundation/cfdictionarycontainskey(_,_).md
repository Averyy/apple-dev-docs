# CFDictionaryContainsKey(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a given key is in a dictionary.

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
func CFDictionaryContainsKey(_ theDict: CFDictionary!, _ key: UnsafeRawPointer!) -> Bool
```

```c
extern Boolean CFDictionaryContainsKey(CFDictionaryRef theDict, const void *key);
```

## Return Value

`true` if `key` is in the dictionary, otherwise `false`.

## Parameters

- `theDict`: The dictionary to examine.
- `key`: The key for which to find matches in `theDict`. The key hash and equal callbacks provided when the dictionary was created, are used to compare. If the hash callback is `NULL`, `key` is treated as a pointer and converted to an integer. If the equal callback is `NULL`, pointer equality (in C, ==) is used. If `key`, or any of the keys in the dictionary, is not understood by the equal callback, the behavior is undefined.

## See Also

### Examining a dictionary
- [func CFDictionaryContainsValue(CFDictionary!, UnsafeRawPointer!) -> Bool](./cfdictionarycontainsvalue%28_,_%29.md)
  Returns a Boolean value that indicates whether a given value is in a dictionary.
- [func CFDictionaryGetCount(CFDictionary!) -> CFIndex](./cfdictionarygetcount%28_%29.md)
  Returns the number of key-value pairs in a dictionary.
- [func CFDictionaryGetCountOfKey(CFDictionary!, UnsafeRawPointer!) -> CFIndex](./cfdictionarygetcountofkey%28_,_%29.md)
  Returns the number of times a key occurs in a dictionary.
- [func CFDictionaryGetCountOfValue(CFDictionary!, UnsafeRawPointer!) -> CFIndex](./cfdictionarygetcountofvalue%28_,_%29.md)
  Counts the number of times a given value occurs in the dictionary.
- [func CFDictionaryGetKeysAndValues(CFDictionary!, UnsafeMutablePointer<UnsafeRawPointer?>!, UnsafeMutablePointer<UnsafeRawPointer?>!)](./cfdictionarygetkeysandvalues%28_,_,_%29.md)
  Fills two buffers with the keys and values from a dictionary.
- [func CFDictionaryGetValue(CFDictionary!, UnsafeRawPointer!) -> UnsafeRawPointer!](./cfdictionarygetvalue%28_,_%29.md)
  Returns the value associated with a given key.
- [func CFDictionaryGetValueIfPresent(CFDictionary!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](./cfdictionarygetvalueifpresent%28_,_,_%29.md)
  Returns a Boolean value that indicates whether a given value for a given key is in a dictionary, and returns that value indirectly if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionarycontainskey(_:_:))*