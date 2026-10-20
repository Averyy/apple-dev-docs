# uriRepresentation()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns a URI that provides an archiveable reference to the object for the object ID.

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
func uriRepresentation() -> URL
```

```objc
- (NSURL *) URIRepresentation;
```

#### Return Value

An `NSURL` object containing a URI that provides an archiveable reference to the object which the receiver represents.

#### Discussion

If the corresponding managed object has not yet been saved, the object ID (and hence URI) is a temporary value that will change when the corresponding managed object is saved.

## See Also

### Related Documentation
- [func managedObjectID(forURIRepresentation: URL) -> NSManagedObjectID?](../nspersistentstorecoordinator/managedobjectid%28forurirepresentation%29.md)
  Returns the object identifier for the specified URI representation.
- [func object(with: NSManagedObjectID) -> NSManagedObject](../nsmanagedobjectcontext/object%28with%29.md)
  Returns either an existing object from the context or a fault that represents that object.
### Getting Managed Object ID Information
- [var entity: NSEntityDescription](./entity.md)
  The entity description associated with the object ID.
- [var isTemporaryID: Bool](./istemporaryid.md)
  A Boolean value that indicates whether the object ID is temporary.
- [var persistentStore: NSPersistentStore?](./persistentstore.md)
  The persistent store that fetched the object for the object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectid/urirepresentation())*