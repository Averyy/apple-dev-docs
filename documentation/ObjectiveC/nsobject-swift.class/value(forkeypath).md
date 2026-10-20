# value(forKeyPath:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns the value for the derived property identified by a given key path.

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
func value(forKeyPath keyPath: String) -> Any?
```

```objc
- (id) valueForKeyPath:(NSString *) keyPath;
```

#### Return Value

The value for the derived property identified by `keyPath`.

#### Discussion

The default implementation gets the destination object for each relationship using [`value(forKey:)`](./value%28forkey%29.md) and returns the result of a [`value(forKey:)`](./value%28forkey%29.md) message to the final object.

## Parameters

- `keyPath`: A key path of the form relationship.property (with one or more relationships); for example “department.name” or “department.manager.lastName”.

## See Also

### Related Documentation
- [func setValue(Any?, forKeyPath: String)](./setvalue%28_,forkeypath%29.md)
  Sets the value for the property identified by a given key path to a given value.
### Getting Values
- [func value(forKey: String) -> Any?](./value%28forkey%29.md)
  Returns the value for the property identified by a given key.
- [func dictionaryWithValues(forKeys: [String]) -> [String : Any]](./dictionarywithvalues%28forkeys%29.md)
  Returns a dictionary containing the property values identified by each of the keys in a given array.
- [func value(forUndefinedKey: String) -> Any?](./value%28forundefinedkey%29.md)
  Invoked by [`value(forKey:)`](./value%28forkey%29.md) when it finds no property corresponding to a given key.
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

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(forkeypath:))*