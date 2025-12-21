# refresh(_:mergeChanges:)

**Framework**: Core Data  
**Kind**: method

Updates the persistent properties of a managed object to use the latest values from the persistent store.

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
func refresh(_ object: NSManagedObject, mergeChanges flag: Bool)
```

#### Discussion

If you call this method before the [`stalenessInterval`](nsmanagedobjectcontext/stalenessinterval.md) expires, the context reloads the data from the cache instead of fetching from the store. If `flag` is [`true`](https://developer.apple.com/documentation/Swift/true), this method doesn’t affect any transient properties. If `flag` is [`false`](https://developer.apple.com/documentation/Swift/false), the object disposes the value of transient properties.

You typically use this method to ensure data freshness if multiple managed object contexts share a single persistent store. You can use this method to resolve an optimistic locking failure when attempting to save.

Turning `object` into a fault by setting `flag` to [`false`](https://developer.apple.com/documentation/Swift/false) breaks strong references to related managed objects. You can use this method to release a portion of your object graph if you want to constrain memory usage.

## Parameters

- `object`: A managed object.
- `flag`: If   is  , the context reloads the object’s property values from the store or the cache. Then the context applies local changes over the newly loaded values. Merging the local values into   always succeeds, and never results in a merge conflict.

## See Also

- [var stalenessInterval: TimeInterval](nsmanagedobjectcontext/stalenessinterval.md)
  The maximum length of time that may have elapsed since the store previously fetched data before fulfilling a fault issues a new fetch.
- [func reset()](nsmanagedobjectcontext/reset.md)
  Returns the context to its base state.
- [var shouldDeleteInaccessibleFaults: Bool](nsmanagedobjectcontext/shoulddeleteinaccessiblefaults.md)
  A Boolean value that determines whether the context turns inaccessible faults into deleted objects.
- [var insertedObjects: Set<NSManagedObject>](nsmanagedobjectcontext/insertedobjects.md)
  The set of objects that have been inserted into the context but not yet saved in a persistent store.
- [var updatedObjects: Set<NSManagedObject>](nsmanagedobjectcontext/updatedobjects.md)
  The set of objects registered with the context that have uncommitted changes.
- [var deletedObjects: Set<NSManagedObject>](nsmanagedobjectcontext/deletedobjects.md)
  The set of objects that will be removed from their persistent store during the next save operation.
- [func shouldHandleInaccessibleFault(NSManagedObject, for: NSManagedObjectID, triggeredByProperty: NSPropertyDescription?) -> Bool](nsmanagedobjectcontext/shouldhandleinaccessiblefault(_:for:triggeredbyproperty:).md)
  Creates a log of the inaccessible fault.
- [func insert(NSManagedObject)](nsmanagedobjectcontext/insert(_:).md)
  Registers an object to be inserted in the context’s persistent store the next time changes are saved.
- [func delete(NSManagedObject)](nsmanagedobjectcontext/delete(_:).md)
  Specifies an object that should be removed from its persistent store when changes are committed.
- [func assign(Any, to: NSPersistentStore)](nsmanagedobjectcontext/assign(_:to:).md)
  Specifies the store in which a newly inserted object will be saved.
- [func obtainPermanentIDs(for: [NSManagedObject]) throws](nsmanagedobjectcontext/obtainpermanentids(for:).md)
  Converts to permanent IDs the object IDs of the objects in a given array.
- [func detectConflicts(for: NSManagedObject)](nsmanagedobjectcontext/detectconflicts(for:).md)
  Marks an object for conflict detection.
- [func processPendingChanges()](nsmanagedobjectcontext/processpendingchanges.md)
  Forces the context to process changes to the object graph.
- [func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?, context: UnsafeMutableRawPointer?)](nsmanagedobjectcontext/observevalue(forkeypath:of:change:context:).md)
  Allows a context that has registered as an observer of a value to be notified of a change to that value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/refresh(_:mergechanges:))*