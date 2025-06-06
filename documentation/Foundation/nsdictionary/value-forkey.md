# value(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns the value associated with a given key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func value(forKey key: String) -> Any?
```

#### Return Value

The value associated with `key`.

#### Discussion

If `key` does not start with “`@`”, invokes [`object(forKey:)`](nsdictionary/object(forkey:).md). If `key` does start with “`@`”, strips the “@” and invokes `[super valueForKey:]` with the rest of the key.

## Parameters

- `key`: The key for which to return the corresponding value. Note that when using key-value coding, the key must be a string (see  ).

## See Also

- [func setValue(Any?, forKey: String)](nsmutabledictionary/setvalue(_:forkey:).md)
  Adds a given key-value pair to the dictionary.
- [var allKeys: [Any]](nsdictionary/allkeys.md)
  A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [func allKeys(for: Any) -> [Any]](nsdictionary/allkeys(for:).md)
  Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.
- [var allValues: [Any]](nsdictionary/allvalues.md)
  A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.
- [func objects(forKeys: [Any], notFoundMarker: Any) -> [Any]](nsdictionary/objects(forkeys:notfoundmarker:).md)
  Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [func object(forKey: Any) -> Any?](nsdictionary/object(forkey:).md)
  Returns the value associated with a given key.
- [subscript(any NSCopying) -> Any?](nsdictionary/subscript(_:)-52n56.md)
  Returns the value associated with a given key.
- [subscript(Any) -> Any?](nsdictionary/subscript(_:)-1bt1b.md)
  Accesses the value associated with a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/value(forkey:))*