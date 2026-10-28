# value(forKey:)

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
func value(forKey key: String) -> Any?
```

```objc
- (ObjectType) valueForKey:(NSString *) key;
```

## Return Value

The value associated with `key`.

## Discussion

If `key` does not start with “`@`”, invokes [`object(forKey:)`](./object%28forkey%29.md). If `key` does start with “`@`”, strips the “@” and invokes `[super valueForKey:]` with the rest of the key.

## Parameters

- `key`: The key for which to return the corresponding value. Note that when using key-value coding, the key must be a string (see [Accessing Object Properties](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/BasicPrinciples.html#//apple_ref/doc/uid/20002170)).

## See Also

### Related Documentation
- [func setValue(Any?, forKey: String)](../nsmutabledictionary/setvalue%28_,forkey%29.md)
  Adds a given key-value pair to the dictionary.
- [- getObjects:andKeys:](./getobjects_andkeys_.md)
  Returns by reference C arrays of the keys and values in the dictionary.
### Accessing Keys and Values
- [var allKeys: [Any]](./allkeys.md)
  A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [func allKeys(for: Any) -> [Any]](./allkeys%28for%29.md)
  Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.
- [var allValues: [Any]](./allvalues.md)
  A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.
- [func objects(forKeys: [Any], notFoundMarker: Any) -> [Any]](./objects%28forkeys,notfoundmarker%29.md)
  Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [func object(forKey: Any) -> Any?](./object%28forkey%29.md)
  Returns the value associated with a given key.
- [subscript(any NSCopying) -> Any?](./subscript%28_%29-52n56.md)
  Returns the value associated with a given key.
- [subscript(Any) -> Any?](./subscript%28_%29-1bt1b.md)
  Accesses the value associated with a given key.
- [- getObjects:andKeys:count:](./getobjects_andkeys_count_.md)
  Returns by reference C arrays of the keys and values in the dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/value(forkey:))*