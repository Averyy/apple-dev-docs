# mutableArrayValue(forKey:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns a mutable array proxy that provides read-write access to an ordered to-many relationship specified by a given key.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func mutableArrayValue(forKey key: String) -> NSMutableArray
```

#### Return Value

A mutable array proxy that provides read-write access to the ordered to-many relationship specified by `key`.

#### Discussion

Objects added to the mutable array become related to the receiver, and objects removed from the mutable array become unrelated. The default implementation recognizes the same simple accessor methods and array accessor methods as [`value(forKey:)`](nsobject-swift.class/value(forkey:).md), and follows the same direct instance variable access policies, but always returns a mutable collection proxy object instead of the immutable collection that [`value(forKey:)`](nsobject-swift.class/value(forkey:).md) would return.

The search pattern that `mutableArrayValueForKey:` uses is described in [`Accessor Search Patterns`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/SearchImplementation.html#//apple_ref/doc/uid/20000955) in [`Key-Value Coding Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i).

## Parameters

- `key`: The name of an ordered to-many relationship.

## See Also

- [func value(forKey: String) -> Any?](nsobject-swift.class/value(forkey:).md)
  Returns the value for the property identified by a given key.
- [func value(forKeyPath: String) -> Any?](nsobject-swift.class/value(forkeypath:).md)
  Returns the value for the derived property identified by a given key path.
- [func dictionaryWithValues(forKeys: [String]) -> [String : Any]](nsobject-swift.class/dictionarywithvalues(forkeys:).md)
  Returns a dictionary containing the property values identified by each of the keys in a given array.
- [func value(forUndefinedKey: String) -> Any?](nsobject-swift.class/value(forundefinedkey:).md)
  Invoked by [`value(forKey:)`](nsobject-swift.class/value(forkey:).md) when it finds no property corresponding to a given key.
- [func mutableArrayValue(forKeyPath: String) -> NSMutableArray](nsobject-swift.class/mutablearrayvalue(forkeypath:).md)
  Returns a mutable array that provides read-write access to the ordered to-many relationship specified by a given key path.
- [func mutableSetValue(forKey: String) -> NSMutableSet](nsobject-swift.class/mutablesetvalue(forkey:).md)
  Returns a mutable set proxy that provides read-write access to the unordered to-many relationship specified by a given key.
- [func mutableSetValue(forKeyPath: String) -> NSMutableSet](nsobject-swift.class/mutablesetvalue(forkeypath:).md)
  Returns a mutable set that provides read-write access to the unordered to-many relationship specified by a given key path.
- [func mutableOrderedSetValue(forKey: String) -> NSMutableOrderedSet](nsobject-swift.class/mutableorderedsetvalue(forkey:).md)
  Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key.
- [func mutableOrderedSetValue(forKeyPath: String) -> NSMutableOrderedSet](nsobject-swift.class/mutableorderedsetvalue(forkeypath:).md)
  Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/mutablearrayvalue(forkey:))*