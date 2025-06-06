# setValue(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Adds a given key-value pair to the dictionary.

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
func setValue(_ value: Any?, forKey key: String)
```

#### Discussion

This method adds `value` and `key` to the dictionary using [`setObject(_:forKey:)`](nsmutabledictionary/setobject(_:forkey:).md), unless `value` is `nil` in which case the method instead attempts to remove `key` using [`removeObject(forKey:)`](nsmutabledictionary/removeobject(forkey:).md).

## Parameters

- `value`: The value for  .
- `key`: The key for  . Note that when using key-value coding, the key must be a string (see  ).

## See Also

- [func value(forKey: String) -> Any?](nsdictionary/value(forkey:).md)
  Returns the value associated with a given key.
- [func setObject(Any, forKey: any NSCopying)](nsmutabledictionary/setobject(_:forkey:).md)
  Adds a given key-value pair to the dictionary.
- [func addEntries(from: [AnyHashable : Any])](nsmutabledictionary/addentries(from:).md)
  Adds to the receiving dictionary the entries from another dictionary.
- [func setDictionary([AnyHashable : Any])](nsmutabledictionary/setdictionary(_:).md)
  Sets the contents of the receiving dictionary to entries in a given dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/setvalue(_:forkey:))*