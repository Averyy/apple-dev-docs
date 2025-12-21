# value(forUndefinedKey:)

**Framework**: Objective-C Runtime  
**Kind**: method

Invoked by [`value(forKey:)`](nsobject-swift.class/value(forkey:).md) when it finds no property corresponding to a given key.

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
func value(forUndefinedKey key: String) -> Any?
```

#### Discussion

Subclasses can override this method to return an alternate value for undefined keys. The default implementation raises an `NSUndefinedKeyException`.

## Parameters

- `key`: A string that is not equal to the name of any of the receiver’s properties.

## See Also

- [func setValue(Any?, forUndefinedKey: String)](nsobject-swift.class/setvalue(_:forundefinedkey:).md)
  Invoked by [`setValue(_:forKey:)`](nsobject-swift.class/setvalue(_:forkey:).md) when it finds no property for a given key.
- [func value(forKey: String) -> Any?](nsobject-swift.class/value(forkey:).md)
  Returns the value for the property identified by a given key.
- [func value(forKeyPath: String) -> Any?](nsobject-swift.class/value(forkeypath:).md)
  Returns the value for the derived property identified by a given key path.
- [func dictionaryWithValues(forKeys: [String]) -> [String : Any]](nsobject-swift.class/dictionarywithvalues(forkeys:).md)
  Returns a dictionary containing the property values identified by each of the keys in a given array.
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

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(forundefinedkey:))*