# NSManagedObjectID

**Framework**: Core Data  
**Kind**: class

A compact, universal identifier for a managed object.

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
class NSManagedObjectID
```

## Mentions

- [Using Core Data in the background](using-core-data-in-the-background.md)

#### Overview

This identifier forms the basis for uniquing in the Core Data Framework. A managed object ID uniquely identifies the same managed object both between managed object contexts in a single application, and in multiple applications (as in distributed systems). Identifiers contain the information needed to exactly describe an object in a persistent store (like the primary key in the database), although the detailed information is not exposed. The framework completely encapsulates the “external” information and presents a clean object oriented interface.

Object IDs can be transformed into a URI representation which can be archived and recreated later to refer back to a given object (using [`managedObjectID(forURIRepresentation:)`](nspersistentstorecoordinator/managedobjectid(forurirepresentation:).md) (`NSPersistentStoreCoordinator`) and [`object(with:)`](nsmanagedobjectcontext/object(with:).md) (`NSManagedObjectContext`). For example, the last selected group in an application could be stored in the user defaults through the group object’s ID. You can also use object ID URI representations to store “weak” relationships across persistent stores (where no hard join is possible).

## Topics

### Getting Managed Object ID Information
- [var entity: NSEntityDescription](nsmanagedobjectid/entity.md)
  The entity description associated with the object ID.
- [var isTemporaryID: Bool](nsmanagedobjectid/istemporaryid.md)
  A Boolean value that indicates whether the object ID is temporary.
- [var persistentStore: NSPersistentStore?](nsmanagedobjectid/persistentstore.md)
  The persistent store that fetched the object for the object ID.
- [func uriRepresentation() -> URL](nsmanagedobjectid/urirepresentation.md)
  Returns a URI that provides an archiveable reference to the object for the object ID.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSFetchRequestResult](nsfetchrequestresult.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSManagedObjectContext](nsmanagedobjectcontext.md)
  An object space to manipulate and track changes to managed objects.
- [class NSManagedObject](nsmanagedobject.md)
  The base class that all Core Data model objects inherit from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectid)*