# objectID

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The object ID of the managed object.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var objectID: NSManagedObjectID { get }
```

```objc
@property (nonatomic, strong, readonly) NSManagedObjectID * objectID;
```

## Mentions

- [Consuming relevant store changes](../consuming-relevant-store-changes.md)
- [Creating a Core Data Model for CloudKit](../creating-a-core-data-model-for-cloudkit.md)

## Discussion

If the receiver is a fault, accessing this property does not cause it to fire.

> ❗ **Important**:  If the receiver has not yet been saved, the object ID is a temporary value that will change when the object is saved.

## See Also

### Related Documentation
- [func uriRepresentation() -> URL](../nsmanagedobjectid/urirepresentation%28%29.md)
  Returns a URI that provides an archiveable reference to the object for the object ID.
### Getting a Managed Object’s Identity
- [var entity: NSEntityDescription](./entity-swift.property.md)
  The entity description of the managed object.
- [class func entity() -> NSEntityDescription](./entity%28%29.md)
  Returns the entity description that is associated with this subclass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/objectid)*