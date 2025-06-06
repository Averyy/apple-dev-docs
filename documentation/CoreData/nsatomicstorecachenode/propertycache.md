# propertyCache

**Framework**: Core Data  
**Kind**: property

The property cache dictionary of the node.

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
var propertyCache: NSMutableDictionary? { get set }
```

#### Discussion

This dictionary is used by [`value(forKey:)`](nsatomicstorecachenode/value(forkey:).md) and [`setValue(_:forKey:)`](nsatomicstorecachenode/setvalue(_:forkey:).md) for property values. This property is `nil` unless it has been explicitly set or non-`nil` values have been set for keys using [`setValue(_:forKey:)`](nsatomicstorecachenode/setvalue(_:forkey:).md).

## See Also

- [var objectID: NSManagedObjectID](nsatomicstorecachenode/objectid.md)
  The managed object ID of the node.
- [func value(forKey: String) -> Any?](nsatomicstorecachenode/value(forkey:).md)
  Returns the value for a given key.
- [func setValue(Any?, forKey: String)](nsatomicstorecachenode/setvalue(_:forkey:).md)
  Sets the value for the given key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsatomicstorecachenode/propertycache)*