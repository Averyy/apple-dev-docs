# entity

**Framework**: Core Data  
**Kind**: property

The entity description of the managed object.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var entity: NSEntityDescription { get }
```

#### Discussion

If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

- [var objectID: NSManagedObjectID](nsmanagedobject/objectid.md)
  The object ID of the managed object.
- [class func entity() -> NSEntityDescription](nsmanagedobject/entity.md)
  Returns the entity description that is associated with this subclass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/entity-swift.property)*