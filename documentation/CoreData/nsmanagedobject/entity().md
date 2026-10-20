# entity()

**Framework**: Core Data  
**Kind**: method

Returns the entity description that is associated with this subclass.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func entity() -> NSEntityDescription
```

#### Discussion

This method is only legal to call on subclasses of `NSManagedObject` that represent a single entity in the model.

## See Also

- [var entity: NSEntityDescription](nsmanagedobject/entity-swift.property.md)
  The entity description of the managed object.
- [var objectID: NSManagedObjectID](nsmanagedobject/objectid.md)
  The object ID of the managed object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/entity())*