# value(forKeyPath:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns the value for the derived property identified by a given key path.

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
func value(forKeyPath keyPath: String) -> Any?
```

#### Return Value

The value for the derived property identified by `keyPath`.

#### Discussion

The default implementation gets the destination object for each relationship using [`value(forKey:)`](nsobject-swift.class/value(forkey:).md) and returns the result of a [`value(forKey:)`](nsobject-swift.class/value(forkey:).md) message to the final object.

## Parameters

- `keyPath`: A key path of the form relationship.property (with one or more relationships); for example “department.name” or “department.manager.lastName”.

## See Also

- [func setValue(Any?, forKeyPath: String)](nsobject-swift.class/setvalue(_:forkeypath:).md)
  Sets the value for the property identified by a given key path to a given value.
- [func value(forKey: String) -> Any?](nsobject-swift.class/value(forkey:).md)
  Returns the value for the property identified by a given key.
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
- [func mutableOrderedSetValue(forKeyPath: String) -> NSMutableOrderedSet](nsobject-swift.class/mutableorderedsetvalue(forkeypath:).md)
  Returns a mutable ordered set that provides read-write access to the uniquing ordered to-many relationship specified by a given key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(forkeypath:))*