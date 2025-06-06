# uriRepresentation()

**Framework**: Core Data  
**Kind**: method

Returns a URI that provides an archiveable reference to the object for the object ID.

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
func uriRepresentation() -> URL
```

#### Return Value

An `NSURL` object containing a URI that provides an archiveable reference to the object which the receiver represents.

#### Discussion

If the corresponding managed object has not yet been saved, the object ID (and hence URI) is a temporary value that will change when the corresponding managed object is saved.

## See Also

- [func managedObjectID(forURIRepresentation: URL) -> NSManagedObjectID?](nspersistentstorecoordinator/managedobjectid(forurirepresentation:).md)
  Returns the object identifier for the specified URI representation.
- [func object(with: NSManagedObjectID) -> NSManagedObject](nsmanagedobjectcontext/object(with:).md)
  Returns either an existing object from the context or a fault that represents that object.
- [var entity: NSEntityDescription](nsmanagedobjectid/entity.md)
  The entity description associated with the object ID.
- [var isTemporaryID: Bool](nsmanagedobjectid/istemporaryid.md)
  A Boolean value that indicates whether the object ID is temporary.
- [var persistentStore: NSPersistentStore?](nsmanagedobjectid/persistentstore.md)
  The persistent store that fetched the object for the object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectid/urirepresentation())*