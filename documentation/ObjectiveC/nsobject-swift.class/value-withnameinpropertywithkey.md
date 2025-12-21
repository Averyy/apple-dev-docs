# value(withName:inPropertyWithKey:)

**Framework**: Objective-C Runtime  
**Kind**: method

Retrieves a named object from the collection specified by the passed key.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func value(withName name: String, inPropertyWithKey key: String) -> Any?
```

#### Discussion

The method `valueIn<Key>WithName:` is used if it exists. Otherwise, raises an `NSUndefinedKeyException`.

## See Also

- [func insertValue(Any, inPropertyWithKey: String)](nsobject-swift.class/insertvalue(_:inpropertywithkey:).md)
  Inserts an object in the collection specified by the passed key.
- [func value(withUniqueID: Any, inPropertyWithKey: String) -> Any?](nsobject-swift.class/value(withuniqueid:inpropertywithkey:).md)
  Retrieves an object by ID from the collection specified by the passed key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(withname:inpropertywithkey:))*