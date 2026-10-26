# object(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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
func object(forKey aKey: Any) -> Any?
```

```objc
- (ObjectType) objectForKey:(KeyType) aKey;
```

#### Return Value

The value associated with `aKey`, or `nil` if no value is associated with `aKey`.

## Parameters

- `aKey`: The key for which to return the corresponding value.

## See Also

### Accessing Keys and Values
- [var allKeys: [Any]](./allkeys.md)
  A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [func allKeys(for: Any) -> [Any]](./allkeys%28for%29.md)
  Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.
- [var allValues: [Any]](./allvalues.md)
  A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.
- [func value(forKey: String) -> Any?](./value%28forkey%29.md)
  Returns the value associated with a given key.
- [func objects(forKeys: [Any], notFoundMarker: Any) -> [Any]](./objects%28forkeys,notfoundmarker%29.md)
  Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [subscript(any NSCopying) -> Any?](./subscript%28_%29-52n56.md)
  Returns the value associated with a given key.
- [subscript(Any) -> Any?](./subscript%28_%29-1bt1b.md)
  Accesses the value associated with a given key.
- [- getObjects:andKeys:count:](./getobjects_andkeys_count_.md)
  Returns by reference C arrays of the keys and values in the dictionary.
### Related Documentation
- [- getObjects:andKeys:](./getobjects_andkeys_.md)
  Returns by reference C arrays of the keys and values in the dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/object(forkey:))*