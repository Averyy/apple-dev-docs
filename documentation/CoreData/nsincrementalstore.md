# NSIncrementalStore

**Framework**: Core Data  
**Kind**: class

An abstract superclass defining the API through which Core Data communicates with a store.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSIncrementalStore
```

#### Overview

You use this interface to create persistent stores that load and save data incrementally, allowing for the management of large and/or shared datasets.

##### Subclassing Notes

###### Methods to Override

In a subclass of `NSIncrementalStore`, you  override the following methods to provide behavior appropriate for your store:

- [`loadMetadata()`](nsincrementalstore/loadmetadata().md)
- [`execute(_:with:)`](nsincrementalstore/execute(_:with:).md)
- [`newValuesForObject(with:with:)`](nsincrementalstore/newvaluesforobject(with:with:).md)
- [`newValue(forRelationship:forObjectWith:with:)`](nsincrementalstore/newvalue(forrelationship:forobjectwith:with:).md)
- [`obtainPermanentIDs(for:)`](nsincrementalstore/obtainpermanentids(for:).md)

You can also optionally override the following methods:

- [`identifierForNewStore(at:)`](nsincrementalstore/identifierfornewstore(at:).md)
- [`managedObjectContextDidRegisterObjects(with:)`](nsincrementalstore/managedobjectcontextdidregisterobjects(with:).md)
- [`managedObjectContextDidUnregisterObjects(with:)`](nsincrementalstore/managedobjectcontextdidunregisterobjects(with:).md)

There is no need to override the methods that you must otherwise override for a subclass of [`NSPersistentStore`](nspersistentstore.md).

###### Methods That Should Not Be Overridden

In a subclass of `NSIncrementalStore`, you should not override the following methods:

- [`newObjectID(for:referenceObject:)`](nsincrementalstore/newobjectid(for:referenceobject:).md)
- [`referenceObject(for:)`](nsincrementalstore/referenceobject(for:).md)

## Topics

### Manipulating Managed Objects
- [func execute(NSPersistentStoreRequest, with: NSManagedObjectContext?) throws -> Any](nsincrementalstore/execute(_:with:).md)
  Returns a value as appropriate for the given request, or nil if the request cannot be completed.
- [func newValuesForObject(with: NSManagedObjectID, with: NSManagedObjectContext) throws -> NSIncrementalStoreNode](nsincrementalstore/newvaluesforobject(with:with:).md)
  Returns an incremental store node encapsulating the persistent external values of the object with a given object ID.
- [func newValue(forRelationship: NSRelationshipDescription, forObjectWith: NSManagedObjectID, with: NSManagedObjectContext?) throws -> Any](nsincrementalstore/newvalue(forrelationship:forobjectwith:with:).md)
  Returns the relationship for the given relationship of the object with a given object ID.
- [func obtainPermanentIDs(for: [NSManagedObject]) throws -> [NSManagedObjectID]](nsincrementalstore/obtainpermanentids(for:).md)
  Returns an array containing the object IDs for a given array of newly-inserted objects.
- [func newObjectID(for: NSEntityDescription, referenceObject: Any) -> NSManagedObjectID](nsincrementalstore/newobjectid(for:referenceobject:).md)
  Returns a new object ID that uses given data as the key.
- [func referenceObject(for: NSManagedObjectID) -> Any](nsincrementalstore/referenceobject(for:).md)
  Returns the reference data used to construct a given object ID.
### Responding to Context Changes
- [func managedObjectContextDidRegisterObjects(with: [NSManagedObjectID])](nsincrementalstore/managedobjectcontextdidregisterobjects(with:).md)
  Indicates that objects identified by a given array of object IDs are in use in a managed object context.
- [func managedObjectContextDidUnregisterObjects(with: [NSManagedObjectID])](nsincrementalstore/managedobjectcontextdidunregisterobjects(with:).md)
  Indicates that objects identified by a given array of object IDs are no longer being used by a managed object context.
### Accessing Metadata
- [class func identifierForNewStore(at: URL) -> Any](nsincrementalstore/identifierfornewstore(at:).md)
  Returns the identifier for the store at a given URL.
- [func loadMetadata() throws](nsincrementalstore/loadmetadata.md)
  Loads the metadata for the store.

## Relationships

### Inherits From
- [NSPersistentStore](nspersistentstore.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSPersistentStoreCoordinator](nspersistentstorecoordinator.md)
  An object that enables an app’s contexts and the underlying persistent stores to work together.
- [class NSPersistentStore](nspersistentstore.md)
  The abstract base class for all Core Data persistent stores.
- [class NSPersistentStoreDescription](nspersistentstoredescription.md)
  A description object used to create and load a persistent store.
- [class NSPersistentStoreRequest](nspersistentstorerequest.md)
  Criteria used to retrieve data from or save data to a persistent store.
- [class NSPersistentStoreResult](nspersistentstoreresult.md)
  The abstract base class for results returned from a persistent store coordinator.
- [class NSPersistentStoreAsynchronousResult](nspersistentstoreasynchronousresult.md)
  A concrete class used to represent the results of an asynchronous request.
- [class NSSaveChangesRequest](nssavechangesrequest.md)
  An encapsulation of a collection of changes to be made by an object store in response to a save operation on a managed object context.
- [class NSAtomicStore](nsatomicstore.md)
  An abstract superclass that you subclass to create a Core Data atomic store.
- [class NSAtomicStoreCacheNode](nsatomicstorecachenode.md)
  A concrete class that you use to represent basic nodes in a Core Data atomic store.
- [class NSIncrementalStoreNode](nsincrementalstorenode.md)
  A concrete class used to represent basic nodes in a Core Data incremental store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstore)*