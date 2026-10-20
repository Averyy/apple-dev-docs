# allKeys(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a new array containing the keys corresponding to all occurrences of a given object in the dictionary.

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
func allKeys(for anObject: Any) -> [Any]
```

```objc
- (NSArray<id> *) allKeysForObject:(ObjectType) anObject;
```

#### Return Value

A new array containing the keys corresponding to all occurrences of `anObject` in the dictionary. If no object matching `anObject` is found, returns an empty array.

#### Discussion

Each object in the dictionary is sent an [`isEqual(_:)`](../../ObjectiveC/nsobjectprotocol/isequal%28_%29.md) message to determine if it’s equal to `anObject`.

## Parameters

- `anObject`: The value to look for in the dictionary.

## See Also

### Accessing Keys and Values
- [var allKeys: [Any]](./allkeys.md)
  A new array containing the dictionary’s keys, or an empty array if the dictionary has no entries.
- [var allValues: [Any]](./allvalues.md)
  A new array containing the dictionary’s values, or an empty array if the dictionary has no entries.
- [func value(forKey: String) -> Any?](./value%28forkey%29.md)
  Returns the value associated with a given key.
- [func objects(forKeys: [Any], notFoundMarker: Any) -> [Any]](./objects%28forkeys,notfoundmarker%29.md)
  Returns as a static array the set of objects from the dictionary that corresponds to the specified keys.
- [func object(forKey: Any) -> Any?](./object%28forkey%29.md)
  Returns the value associated with a given key.
- [subscript(any NSCopying) -> Any?](./subscript%28_%29-52n56.md)
  Returns the value associated with a given key.
- [subscript(Any) -> Any?](./subscript%28_%29-1bt1b.md)
  Accesses the value associated with a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/allkeys(for:))*