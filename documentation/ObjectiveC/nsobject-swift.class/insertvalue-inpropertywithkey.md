# insertValue(_:inPropertyWithKey:)

**Framework**: Objective-C Runtime  
**Kind**: method

Inserts an object in the collection specified by the passed key.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func insertValue(_ value: Any, inPropertyWithKey key: String)
```

#### Discussion

The method `insertIn<Key>:` is used if it exists. Otherwise, raises an `NSUndefinedKeyException`. This is part of Cocoa’s scripting support for inserting newly-created objects into containers without explicitly specifying a location.

## See Also

- [func value(withName: String, inPropertyWithKey: String) -> Any?](nsobject-swift.class/value(withname:inpropertywithkey:).md)
  Retrieves a named object from the collection specified by the passed key.
- [func value(withUniqueID: Any, inPropertyWithKey: String) -> Any?](nsobject-swift.class/value(withuniqueid:inpropertywithkey:).md)
  Retrieves an object by ID from the collection specified by the passed key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/insertvalue(_:inpropertywithkey:))*