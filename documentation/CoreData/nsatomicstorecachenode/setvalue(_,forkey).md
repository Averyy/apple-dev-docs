# setValue(_:forKey:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Sets the value for the given key.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setValue(_ value: Any?, forKey key: String)
```

```objc
- (void) setValue:(id) value forKey:(NSString *) key;
```

## Discussion

The default implementation forwards the request to the [`propertyCache`](./propertycache.md) dictionary if `key` matches a property name of the entity for this cache node. If `key` does not represent a property, the standard [`setValue(_:forKey:)`](../../ObjectiveC/nsobject-swift.class/setvalue%28_,forkey%29.md) implementation is used.

## Parameters

- `value`: The value for the property identified by `key`.
- `key`: The name of a property.

## See Also

### Managing Node Data
- [var objectID: NSManagedObjectID](./objectid.md)
  The managed object ID of the node.
- [var propertyCache: NSMutableDictionary?](./propertycache.md)
  The property cache dictionary of the node.
- [func value(forKey: String) -> Any?](./value%28forkey%29.md)
  Returns the value for a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/setvalue(_:forkey:))*