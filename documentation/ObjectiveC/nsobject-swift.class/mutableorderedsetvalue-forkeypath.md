# mutableOrderedSetValue(forKeyPath:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key path.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet
```

#### Return Value

A mutable ordered set that provides read-write access to the uniquing to-many relationship specified by `keyPath`.

#### Discussion

See [`mutableOrderedSetValue(forKey:)`](nsobject-swift.class/mutableorderedsetvalue(forkey:).md) for additional details.

## Parameters

- `keyPath`: A key path, relative to the receiver, to a uniquing ordered to-many relationship represented by a set.

## See Also

- [func value(forKey: String) -> Any?](nsobject-swift.class/value(forkey:).md)
  Returns the value for the property identified by a given key.
- [func value(forKeyPath: String) -> Any?](nsobject-swift.class/value(forkeypath:).md)
  Returns the value for the derived property identified by a given key path.
- [func dictionaryWithValues(forKeys: [String]) -> [String : Any]](nsobject-swift.class/dictionarywithvalues(forkeys:).md)
  Returns a dictionary containing the property values identified by each of the keys in a given array.
- [func value(forUndefinedKey: String) -> Any?](nsobject-swift.class/value(forundefinedkey:).md)
  Invoked by [`value(forKey:)`](nsobject-swift.class/value(forkey:).md) when it finds no property corresponding to a given key.
- [func mutableArrayValue(forKey: String) -> NSMutableArray](nsobject-swift.class/mutablearrayvalue(forkey:).md)
  Returns a mutable array proxy that provides read-write access to an ordered to-many relationship specified by a given key.
- [func mutableArrayValue(forKeyPath: String) -> NSMutableArray](nsobject-swift.class/mutablearrayvalue(forkeypath:).md)
  Returns a mutable array that provides read-write access to the ordered to-many relationship specified by a given key path.
- [func mutableSetValue(forKey: String) -> NSMutableSet](nsobject-swift.class/mutablesetvalue(forkey:).md)
  Returns a mutable set proxy that provides read-write access to the unordered to-many relationship specified by a given key.
- [func mutableSetValue(forKeyPath: String) -> NSMutableSet](nsobject-swift.class/mutablesetvalue(forkeypath:).md)
  Returns a mutable set that provides read-write access to the unordered to-many relationship specified by a given key path.
- [func mutableOrderedSetValue(forKey: String) -> NSMutableOrderedSet](nsobject-swift.class/mutableorderedsetvalue(forkey:).md)
  Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/mutableorderedsetvalue(forkeypath:))*