# CFDictionaryContainsValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a given value is in a dictionary.

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
func CFDictionaryContainsValue(_ theDict: CFDictionary!, _ value: UnsafeRawPointer!) -> Bool
```

```c
extern Boolean CFDictionaryContainsValue(CFDictionaryRef theDict, const void *value);
```

#### Return Value

`true` if `value` is in the dictionary, otherwise `false`.

## Parameters

- `theDict`: The dictionary to examine.
- `value`: The value for which to find matches in `theDict`. The value equal callback provided when the dictionary was created is used to compare. If the equal callback was `NULL`, pointer equality (in C, ==) is used. If `value`, or any other value in the dictionary, is not understood by the equal callback, the behavior is undefined.

## See Also

### Examining a dictionary
- [func CFDictionaryContainsKey(CFDictionary!, UnsafeRawPointer!) -> Bool](./cfdictionarycontainskey%28_,_%29.md)
  Returns a Boolean value that indicates whether a given key is in a dictionary.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionarycontainsvalue(_:_:))*