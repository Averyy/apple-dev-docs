# objects(forKeys:notFoundMarker:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.

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
func objects(forKeys keys: [Any], notFoundMarker marker: Any) -> [Any]
```

```objc
- (NSArray<id> *) objectsForKeys:(NSArray<id> *) keys notFoundMarker:(ObjectType) marker;
```

#### Discussion

The objects in the returned array and the `keys` array have a one-for-one correspondence, so that the nthe object in the returned array corresponds to the nthe key in `keys`.

## Parameters

- `keys`: An `NSArray` containing the keys for which to return corresponding values.
- `marker`: The marker object to place in the corresponding element of the returned array if an object isn’t found in the dictionary to correspond to a given key.

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
- [func object(forKey: Any) -> Any?](./object%28forkey%29.md)
  Returns the value associated with a given key.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/objects(forkeys:notfoundmarker:))*