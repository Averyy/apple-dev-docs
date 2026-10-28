# value(forUndefinedKey:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Invoked by [`value(forKey:)`](./value%28forkey%29.md) when it finds no property corresponding to a given key.

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
func value(forUndefinedKey key: String) -> Any?
```

```objc
- (id) valueForUndefinedKey:(NSString *) key;
```

## Discussion

Subclasses can override this method to return an alternate value for undefined keys. The default implementation raises an `NSUndefinedKeyException`.

## Parameters

- `key`: A string that is not equal to the name of any of the receiver’s properties.

## See Also

### Related Documentation
- [func setValue(Any?, forUndefinedKey: String)](./setvalue%28_,forundefinedkey%29.md)
  Invoked by [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) when it finds no property for a given key.
### Getting Values
- [func value(forKey: String) -> Any?](./value%28forkey%29.md)
  Returns the value for the property identified by a given key.
- [func value(forKeyPath: String) -> Any?](./value%28forkeypath%29.md)
  Returns the value for the derived property identified by a given key path.
- [func dictionaryWithValues(forKeys: [String]) -> [String : Any]](./dictionarywithvalues%28forkeys%29.md)
  Returns a dictionary containing the property values identified by each of the keys in a given array.
- [func mutableArrayValue(forKey: String) -> NSMutableArray](./mutablearrayvalue%28forkey%29.md)
  Returns a mutable array proxy that provides read-write access to an ordered to-many relationship specified by a given key.
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

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(forundefinedkey:))*