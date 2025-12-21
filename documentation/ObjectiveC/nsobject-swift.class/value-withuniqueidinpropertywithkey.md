# value(withUniqueID:inPropertyWithKey:)

**Framework**: Objective-C Runtime  
**Kind**: method

Retrieves an object by ID from the collection specified by the passed key.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?
```

#### Discussion

The method `valueIn<Key>WithUniqueID:` is invoked if it exists. Otherwise, raises an `NSUndefinedKeyException`. The declared type of `uniqueID` in the constructed method must be `id`, `NSNumber *`, `NSString *`, or one of the scalar types that can be encapsulated by `NSNumber`.

## See Also

- [func insertValue(Any, inPropertyWithKey: String)](nsobject-swift.class/insertvalue(_:inpropertywithkey:).md)
  Inserts an object in the collection specified by the passed key.
- [func value(withName: String, inPropertyWithKey: String) -> Any?](nsobject-swift.class/value(withname:inpropertywithkey:).md)
  Retrieves a named object from the collection specified by the passed key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(withuniqueid:inpropertywithkey:))*