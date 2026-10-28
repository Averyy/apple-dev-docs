# mutableArrayValue(forKey:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns a mutable array proxy that provides read-write access to an ordered to-many relationship specified by a given key.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func mutableArrayValue(forKey key: String) -> NSMutableArray
```

```objc
- (NSMutableArray *) mutableArrayValueForKey:(NSString *) key;
```

## Return Value

A mutable array proxy that provides read-write access to the ordered to-many relationship specified by `key`.

## Discussion

Objects added to the mutable array become related to the receiver, and objects removed from the mutable array become unrelated. The default implementation recognizes the same simple accessor methods and array accessor methods as [`value(forKey:)`](./value%28forkey%29.md), and follows the same direct instance variable access policies, but always returns a mutable collection proxy object instead of the immutable collection that [`value(forKey:)`](./value%28forkey%29.md) would return.

The search pattern that `mutableArrayValueForKey:` uses is described in [Accessor Search Patterns](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/SearchImplementation.html#//apple_ref/doc/uid/20000955) in [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i).

## Parameters

- `key`: The name of an ordered to-many relationship.

## See Also

### Getting Values
- [func value(forKey: String) -> Any?](./value%28forkey%29.md)
  Returns the value for the property identified by a given key.
- [func value(forKeyPath: String) -> Any?](./value%28forkeypath%29.md)
  Returns the value for the derived property identified by a given key path.
- [func dictionaryWithValues(forKeys: [String]) -> [String : Any]](./dictionarywithvalues%28forkeys%29.md)
  Returns a dictionary containing the property values identified by each of the keys in a given array.
- [func value(forUndefinedKey: String) -> Any?](./value%28forundefinedkey%29.md)
  Invoked by [`value(forKey:)`](./value%28forkey%29.md) when it finds no property corresponding to a given key.
- [func mutableArrayValue(forKeyPath: String) -> NSMutableArray](./mutablearrayvalue%28forkeypath%29.md)
  Returns a mutable array that provides read-write access to the ordered to-many relationship specified by a given key path.
- [func mutableSetValue(forKey: String) -> NSMutableSet](./mutablesetvalue%28forkey%29.md)
  Returns a mutable set proxy that provides read-write access to the unordered to-many relationship specified by a given key.
- [func mutableSetValue(forKeyPath: String) -> NSMutableSet](./mutablesetvalue%28forkeypath%29.md)
  Returns a mutable set that provides read-write access to the unordered to-many relationship specified by a given key path.
- [func mutableOrderedSetValue(forKey: String) -> NSMutableOrderedSet](./mutableorderedsetvalue%28forkey%29.md)
  Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key.
- [func mutableOrderedSetValue(forKeyPath: String) -> NSMutableOrderedSet](./mutableorderedsetvalue%28forkeypath%29.md)
  Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/mutablearrayvalue(forkey:))*