# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript

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
subscript(key: any NSCopying) -> Any? { get set }
```

#### Return Value

The value associated with `key`, or `nil` if no value is associated with `aKey`.

#### Discussion

This method has the same behavior as the [`object(forKey:)`](nsdictionary/object(forkey:).md) method.

You shouldn’t need to call this method directly. Instead, this method is called when accessing an object by key using subscripting.

```objc
id value = dictionary[@"key"]; // equivalent to [dictionary objectForKeyedSubscript:@"key"]
```

## Parameters

- `key`: The key for which to return the corresponding value.

## See Also

- [var allKeys: [Any]](nsdictionary/allkeys.md)
  A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [func allKeys(for: Any) -> [Any]](nsdictionary/allkeys(for:).md)
  Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.
- [var allValues: [Any]](nsdictionary/allvalues.md)
  A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.
- [func value(forKey: String) -> Any?](nsdictionary/value(forkey:).md)
  Returns the value associated with a given key.
- [func objects(forKeys: [Any], notFoundMarker: Any) -> [Any]](nsdictionary/objects(forkeys:notfoundmarker:).md)
  Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [func object(forKey: Any) -> Any?](nsdictionary/object(forkey:).md)
  Returns the value associated with a given key.
- [subscript(Any) -> Any?](nsdictionary/subscript(_:)-1bt1b.md)
  Accesses the value associated with a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/subscript(_:)-52n56)*