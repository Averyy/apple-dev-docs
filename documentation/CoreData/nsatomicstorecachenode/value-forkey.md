# value(forKey:)

**Framework**: Core Data  
**Kind**: method

Returns the value for a given key.

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
func value(forKey key: String) -> Any?
```

#### Return Value

The value for the property named `key`. For an attribute, the return value is an instance of an attribute type supported by Core Data (see [`NSAttributeDescription`](nsattributedescription.md)); for a to-one relationship, the return value must be another cache node instance; for a to-many relationship, the return value must be an collection of the related cache nodes.

#### Discussion

The default implementation forwards the request to the [`propertyCache`](nsatomicstorecachenode/propertycache.md) dictionary if `key` matches a property name of the entity for the cache node. If `key` does not represent a property, the standard [`value(forKey:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/value(forKey:)) implementation is used.

## Parameters

- `key`: The name of a property.

## See Also

- [var objectID: NSManagedObjectID](nsatomicstorecachenode/objectid.md)
  The managed object ID of the node.
- [var propertyCache: NSMutableDictionary?](nsatomicstorecachenode/propertycache.md)
  The property cache dictionary of the node.
- [func setValue(Any?, forKey: String)](nsatomicstorecachenode/setvalue(_:forkey:).md)
  Sets the value for the given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/value(forkey:))*