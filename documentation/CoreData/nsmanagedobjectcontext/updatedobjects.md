# updatedObjects

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The set of objects registered with the context that have uncommitted changes.

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
var updatedObjects: Set<NSManagedObject> { get }
```

```objc
@property (nonatomic, strong, readonly) NSSet<__kindof NSManagedObject *> * updatedObjects;
```

#### Discussion

A managed object context does not post key-value observing notifications when the return value of `updatedObjects` changes. A context does, however, post a [`NSManagedObjectContextObjectsDidChange`](../../Foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextobjectsdidchange.md) notification when a change is made, and a [`NSManagedObjectContextWillSave`](../../Foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextwillsave.md) notification and a [`NSManagedObjectContextDidSave`](../../Foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextdidsave.md) notification before and after changes are committed respectively.

## See Also

### Related Documentation
- [var registeredObjects: Set<NSManagedObject>](./registeredobjects.md)
  The set of registered managed objects in the context.
### Handling managed objects
- [var shouldDeleteInaccessibleFaults: Bool](./shoulddeleteinaccessiblefaults.md)
  A Boolean value that determines whether the context turns inaccessible faults into deleted objects.
- [var insertedObjects: Set<NSManagedObject>](./insertedobjects.md)
  The set of objects that have been inserted into the context but not yet saved in a persistent store.
- [var deletedObjects: Set<NSManagedObject>](./deletedobjects.md)
  The set of objects that will be removed from their persistent store during the next save operation.
- [func shouldHandleInaccessibleFault(NSManagedObject, for: NSManagedObjectID, triggeredByProperty: NSPropertyDescription?) -> Bool](./shouldhandleinaccessiblefault%28_,for,triggeredbyproperty%29.md)
  Creates a log of the inaccessible fault.
- [func insert(NSManagedObject)](./insert%28_%29.md)
  Registers an object to be inserted in the context’s persistent store the next time changes are saved.
- [func delete(NSManagedObject)](./delete%28_%29.md)
  Specifies an object that should be removed from its persistent store when changes are committed.
- [func assign(Any, to: NSPersistentStore)](./assign%28_,to%29.md)
  Specifies the store in which a newly inserted object will be saved.
- [func obtainPermanentIDs(for: [NSManagedObject]) throws](./obtainpermanentids%28for%29.md)
  Converts to permanent IDs the object IDs of the objects in a given array.
- [func detectConflicts(for: NSManagedObject)](./detectconflicts%28for%29.md)
  Marks an object for conflict detection.
- [func refresh(NSManagedObject, mergeChanges: Bool)](./refresh%28_,mergechanges%29.md)
  Updates the persistent properties of a managed object to use the latest values from the persistent store.
- [func processPendingChanges()](./processpendingchanges%28%29.md)
  Forces the context to process changes to the object graph.
- [func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?, context: UnsafeMutableRawPointer?)](./observevalue%28forkeypath,of,change,context%29.md)
  Allows a context that has registered as an observer of a value to be notified of a change to that value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/updatedobjects)*