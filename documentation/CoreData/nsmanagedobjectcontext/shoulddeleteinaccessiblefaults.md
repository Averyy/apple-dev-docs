# shouldDeleteInaccessibleFaults

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the context turns inaccessible faults into deleted objects.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var shouldDeleteInaccessibleFaults: Bool { get set }
```

```objc
@property BOOL shouldDeleteInaccessibleFaults;
```

## Discussion

Use this property to control how the context behaves when it encounters an *inaccessible fault* — an object with no underlying data in the persistent store. For example, you might fetch an object that has a to-many relationship, but then a background context deletes the related objects from the store before you traverse that relationship.

When this property is set to [`true`](../../Swift/true.md), the context returns a managed object with the following characteristics:

- The object’s attributes, including scalars, nullable, and mandatory attributes are all set to `nil` or `0`.
- The object’s [`isDeleted`](../nsmanagedobject/isdeleted.md) property is set to [`true`](../../Swift/true.md), which adds the object to the context’s [`deletedObjects`](./deletedobjects.md) set.
- The object is exempt from validation rules, including optionality, because the object is nonexistent and the context discards it when you next call [`save()`](./save%28%29.md) or [`reset()`](./reset%28%29.md).

When the context returns an object with these characteristics, your app can continue running and process this object in the same way as any other deleted object.

When this property is set to [`false`](../../Swift/false.md), the context throws an exception.

The default value is [`true`](../../Swift/true.md).

> **Note**:  You can use query generations to pin a context to a stable view of the store’s data and isolate that context from changes that other contexts or processes make. For more information, see [Accessing data when the store changes](../accessing-data-when-the-store-changes.md).

## See Also

### Handling managed objects
- [var insertedObjects: Set<NSManagedObject>](./insertedobjects.md)
  The set of objects that have been inserted into the context but not yet saved in a persistent store.
- [var updatedObjects: Set<NSManagedObject>](./updatedobjects.md)
  The set of objects registered with the context that have uncommitted changes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/shoulddeleteinaccessiblefaults)*