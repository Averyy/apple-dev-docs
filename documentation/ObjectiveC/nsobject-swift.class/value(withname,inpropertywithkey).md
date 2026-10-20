# value(withName:inPropertyWithKey:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Retrieves a named object from the collection specified by the passed key.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func value(withName name: String, inPropertyWithKey key: String) -> Any?
```

```objc
- (id) valueWithName:(NSString *) name inPropertyWithKey:(NSString *) key;
```

#### Discussion

The method `valueIn<Key>WithName:` is used if it exists. Otherwise, raises an `NSUndefinedKeyException`.

## See Also

### Access by name, key, or ID
- [func insertValue(Any, inPropertyWithKey: String)](./insertvalue%28_,inpropertywithkey%29.md)
  Inserts an object in the collection specified by the passed key.
- [func value(withUniqueID: Any, inPropertyWithKey: String) -> Any?](./value%28withuniqueid,inpropertywithkey%29.md)
  Retrieves an object by ID from the collection specified by the passed key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/value(withname:inpropertywithkey:))*