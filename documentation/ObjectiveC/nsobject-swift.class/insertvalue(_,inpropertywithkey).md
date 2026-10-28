# insertValue(_:inPropertyWithKey:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Inserts an object in the collection specified by the passed key.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func insertValue(_ value: Any, inPropertyWithKey key: String)
```

```objc
- (void) insertValue:(id) value inPropertyWithKey:(NSString *) key;
```

## Discussion

The method `insertIn<Key>:` is used if it exists. Otherwise, raises an `NSUndefinedKeyException`. This is part of Cocoa’s scripting support for inserting newly-created objects into containers without explicitly specifying a location.

## See Also

### Access by name, key, or ID
- [func value(withName: String, inPropertyWithKey: String) -> Any?](./value%28withname,inpropertywithkey%29.md)
  Retrieves a named object from the collection specified by the passed key.
- [func value(withUniqueID: Any, inPropertyWithKey: String) -> Any?](./value%28withuniqueid,inpropertywithkey%29.md)
  Retrieves an object by ID from the collection specified by the passed key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/insertvalue(_:inpropertywithkey:))*