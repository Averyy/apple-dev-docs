# CFDictionaryGetCountOfValue(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Counts the number of times a given value occurs in the dictionary.

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
func CFDictionaryGetCountOfValue(_ theDict: CFDictionary!, _ value: UnsafeRawPointer!) -> CFIndex
```

#### Return Value

The number of times the `value` occurs in `theDict`.

## Parameters

- `theDict`: The dictionary to examine.
- `value`: The value for which to find matches in  . The value equal callback provided when the dictionary was created is used to compare. If the equal callback was  , pointer equality (in C, ==) is used. If  , or any other value in the dictionary, is not understood by the equal callback, the behavior is undefined.

## See Also

- [func CFDictionaryContainsKey(CFDictionary!, UnsafeRawPointer!) -> Bool](cfdictionarycontainskey(_:_:).md)
  Returns a Boolean value that indicates whether a given key is in a dictionary.
- [func CFDictionaryContainsValue(CFDictionary!, UnsafeRawPointer!) -> Bool](cfdictionarycontainsvalue(_:_:).md)
  Returns a Boolean value that indicates whether a given value is in a dictionary.
- [func CFDictionaryGetCount(CFDictionary!) -> CFIndex](cfdictionarygetcount(_:).md)
  Returns the number of key-value pairs in a dictionary.
- [func CFDictionaryGetCountOfKey(CFDictionary!, UnsafeRawPointer!) -> CFIndex](cfdictionarygetcountofkey(_:_:).md)
  Returns the number of times a key occurs in a dictionary.
- [func CFDictionaryGetKeysAndValues(CFDictionary!, UnsafeMutablePointer<UnsafeRawPointer?>!, UnsafeMutablePointer<UnsafeRawPointer?>!)](cfdictionarygetkeysandvalues(_:_:_:).md)
  Fills two buffers with the keys and values from a dictionary.
- [func CFDictionaryGetValue(CFDictionary!, UnsafeRawPointer!) -> UnsafeRawPointer!](cfdictionarygetvalue(_:_:).md)
  Returns the value associated with a given key.
- [func CFDictionaryGetValueIfPresent(CFDictionary!, UnsafeRawPointer!, UnsafeMutablePointer<UnsafeRawPointer?>!) -> Bool](cfdictionarygetvalueifpresent(_:_:_:).md)
  Returns a Boolean value that indicates whether a given value for a given key is in a dictionary, and returns that value indirectly if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionarygetcountofvalue(_:_:))*