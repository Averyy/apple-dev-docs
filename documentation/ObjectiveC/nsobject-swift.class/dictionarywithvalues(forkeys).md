# dictionaryWithValues(forKeys:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary containing the property values identified by each of the keys in a given array.

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
func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]
```

```objc
- (NSDictionary<NSString *,id> *) dictionaryWithValuesForKeys:(NSArray<NSString *> *) keys;
```

#### Return Value

A dictionary containing as keys the property names in `keys`, with corresponding values being the corresponding property values.

#### Discussion

The default implementation invokes [`value(forKey:)`](./value%28forkey%29.md) for each key in `keys` and substitutes `NSNull` values in the dictionary for returned `nil` values.

## Parameters

- `keys`: An array containing `NSString` objects that identify properties of the receiver.

## See Also

### Related Documentation
- [func setValuesForKeys([String : Any])](./setvaluesforkeys%28_%29.md)
  Sets properties of the receiver with values from a given dictionary, using its keys to identify the properties.
### Getting Values
- [func value(forKey: String) -> Any?](./value%28forkey%29.md)
  Returns the value for the property identified by a given key.
- [func value(forKeyPath: String) -> Any?](./value%28forkeypath%29.md)
  Returns the value for the derived property identified by a given key path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/dictionarywithvalues(forkeys:))*