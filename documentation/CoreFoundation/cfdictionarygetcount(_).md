# CFDictionaryGetCount(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the number of key-value pairs in a dictionary.

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
func CFDictionaryGetCount(_ theDict: CFDictionary!) -> CFIndex
```

```c
extern CFIndex CFDictionaryGetCount(CFDictionaryRef theDict);
```

## Return Value

The number of number of key-value pairs in `theDict`.

## Parameters

- `theDict`: The dictionary to examine.

## See Also

### Examining a dictionary
- [func CFDictionaryContainsKey(CFDictionary!, UnsafeRawPointer!) -> Bool](./cfdictionarycontainskey%28_,_%29.md)
  Returns a Boolean value that indicates whether a given key is in a dictionary.
- [func CFDictionaryContainsValue(CFDictionary!, UnsafeRawPointer!) -> Bool](./cfdictionarycontainsvalue%28_,_%29.md)
  Returns a Boolean value that indicates whether a given value is in a dictionary.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdictionarygetcount(_:))*