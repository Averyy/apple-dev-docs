# getObjects:andKeys:count:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns by reference C arrays of the keys and values in the dictionary.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
- (void) getObjects:(ObjectType[]) objects andKeys:(KeyType[]) keys count:(NSUInteger) count;
```

#### Discussion

The elements in the returned array and the keys array have a one-for-one correspondence, so that the nth object in the returned array corresponds to the the key in keys.

## Parameters

- `objects`: Upon return, contains a C array of the values in the dictionary.
- `keys`: Upon return, contains a C array of the keys in the dictionary.
- `count`: The maximum number of objects to return.

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
- [- getObjects:andKeys:](./getobjects_andkeys_.md)
  Returns by reference C arrays of the keys and values in the dictionary.
- [func objects(forKeys: [Any], notFoundMarker: Any) -> [Any]](./objects%28forkeys,notfoundmarker%29.md)
  Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [func object(forKey: Any) -> Any?](./object%28forkey%29.md)
  Returns the value associated with a given key.
- [subscript(any NSCopying) -> Any?](./subscript%28_%29-52n56.md)
  Returns the value associated with a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/getobjects:andkeys:count:)*