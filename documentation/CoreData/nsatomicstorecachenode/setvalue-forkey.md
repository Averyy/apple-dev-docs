# setValue(_:forKey:)

**Framework**: Core Data  
**Kind**: method

Sets the value for the given key.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setValue(_ value: Any?, forKey key: String)
```

#### Discussion

The default implementation forwards the request to the [`propertyCache`](nsatomicstorecachenode/propertycache.md) dictionary if `key` matches a property name of the entity for this cache node. If `key` does not represent a property, the standard [`setValue(_:forKey:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/setValue(_:forKey:)) implementation is used.

## Parameters

- `value`: The value for the property identified by  .
- `key`: The name of a property.

## See Also

- [var objectID: NSManagedObjectID](nsatomicstorecachenode/objectid.md)
  The managed object ID of the node.
- [var propertyCache: NSMutableDictionary?](nsatomicstorecachenode/propertycache.md)
  The property cache dictionary of the node.
- [func value(forKey: String) -> Any?](nsatomicstorecachenode/value(forkey:).md)
  Returns the value for a given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/setvalue(_:forkey:))*