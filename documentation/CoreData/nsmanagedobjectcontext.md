# NSManagedObjectContext

**Framework**: Core Data  
**Kind**: class

An object space to manipulate and track changes to managed objects.

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
class NSManagedObjectContext
```

## Mentions

- [Setting up a Core Data stack manually](setting-up-a-core-data-stack-manually.md)
- [Using Core Data in the background](using-core-data-in-the-background.md)
- [Setting up a Core Data stack](setting-up-a-core-data-stack.md)

#### Overview

A context consists of a group of related model objects that represent an internally consistent view of one or more persistent stores. Changes to managed objects remain in memory in the associated context until Core Data saves that context to one or more persistent stores. A single managed object instance exists in one and only one context, but multiple copies of an object can exist in different contexts. Therefore, an object is unique to a particular context.

##### Life Cycle Management

The context is a powerful object with a central role in the life cycle of managed objects, with responsibilities from life cycle management (including faulting) to validation, inverse relationship handling, and undo/redo. Through a context you can retrieve or “fetch” objects from a persistent store, make changes to those objects, and then either discard the changes or—again through the context—commit them back to the persistent store. The context is responsible for watching for changes in its objects and maintains an undo manager so you can have finer-grained control over undo and redo. You can insert new objects and delete ones you have fetched, and commit these modifications to the persistent store.

All objects fetched from an external store are registered in a context together with a global identifier (an instance of `NSManagedObjectID`) that’s used to uniquely identify each object to the external store.

##### Parent Store

Managed object contexts have a parent store from which they retrieve data representing managed objects and through which they commit changes to managed objects.

Prior to OS X v10.7 and iOS v5.0, the parent store is always a persistent store coordinator. In macOS 10.7 and later and iOS v5.0 and later, the parent store may be another managed object context. Ultimately the root of a context’s ancestry must be a persistent store coordinator. The coordinator provides the managed object model and dispatches requests to the various persistent stores containing the data.

If a context’s parent store is another managed object context, fetch and save operations are mediated by the parent context instead of a coordinator. This pattern has a number of usage scenarios, including:

- Performing background operations on a second thread or queue.
- Managing discardable edits, such as in an inspector window or view.

As the first scenario implies, a parent context can service requests from children on different threads. You cannot, therefore, use parent contexts created with the thread confinement type (see [`Concurrency`](nsmanagedobjectcontext#Concurrency.md)).

When you save changes in a context, the changes are only committed “one store up.” If you save a child context, changes are pushed to its parent. Changes are not saved to the persistent store until the root context is saved. (A root managed object context is one whose parent context is `nil`.) In addition, a parent does not pull changes from children before it saves. You must save a child context if you want ultimately to commit the changes.

##### Notifications

A context posts notifications at various points—see [`NSManagedObjectContextObjectsDidChange`](https://developer.apple.com/documentation/foundation/nsnotification/name/1506884-nsmanagedobjectcontextobjectsdid) for example. Typically, you should register to receive these notifications only from known contexts:

Several system frameworks use Core Data internally. If you register to receive these notifications from all contexts (by passing `nil` as the object parameter to a method such as [`addObserver(_:selector:name:object:)`](https://developer.apple.com/documentation/foundation/notificationcenter/1415360-addobserver)), then you may receive unexpected notifications that are difficult to handle.

##### Concurrency

Core Data uses thread (or serialized queue) confinement to protect managed objects and managed object contexts (see [`Core Data Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)). A consequence of this is that a context assumes the default owner is the thread or queue that creates it. Don’t, therefore, initialize a context on one thread then pass it to another. Instead, pass a reference to a persistent store coordinator and have the receiving thread or queue create a new context using that. If you use [`Operation`](https://developer.apple.com/documentation/Foundation/Operation), you must create the context in [`main()`](https://developer.apple.com/documentation/foundation/operation/1407732-main) (for a serial queue) or [`start()`](https://developer.apple.com/documentation/foundation/operation/1416837-start) (for a concurrent queue).

When you create a context you specify the concurrency type with which you’ll use it. When you create a managed object context, you have two options for its thread (queue) association:

- Private: The context creates and manages a private queue.
- Main: The context associates with the main queue and is dependent on the application’s event loop; otherwise, it’s similar to a private context. Use this type for contexts that update view controllers and other user interface elements.

You use contexts using the queue-based concurrency types in conjunction with [`perform(_:)`](nsmanagedobjectcontext/perform(_:).md) and [`performAndWait(_:)`](nsmanagedobjectcontext/performandwait(_:)-ypye.md). You group “standard” messages to send to the context within a block to pass to one of these methods. There are two exceptions:

- Setter methods on queue-based managed object contexts are thread-safe. You can invoke these methods directly on any thread.
- If your code executes on the main thread, you can invoke methods on the main queue style contexts directly instead of using the block based API.

[`perform(_:)`](nsmanagedobjectcontext/perform(_:).md) and [`performAndWait(_:)`](nsmanagedobjectcontext/performandwait(_:)-ypye.md) ensure the block operations execute on the correct queue for the context. The [`perform(_:)`](nsmanagedobjectcontext/perform(_:).md) method returns immediately and the context executes the block methods on its own thread. With the [`performAndWait(_:)`](nsmanagedobjectcontext/performandwait(_:)-ypye.md) method, the context still executes the block methods on its own thread, but the method doesn’t return until the block completes.

It’s important to appreciate that blocks execute as a distinct body of work. As soon as your block ends, anyone else can enqueue another block, undo changes, reset the context, and so on. Thus blocks may be quite large, and typically end by invoking [`save()`](nsmanagedobjectcontext/save().md).

You can also perform other operations, such as:

##### Subclassing Notes

You are strongly discouraged from subclassing `NSManagedObjectContext`. The change tracking and undo management mechanisms are highly optimized and hence intricate and delicate. Interposing your own additional logic that might impact [`processPendingChanges()`](nsmanagedobjectcontext/processpendingchanges().md) can have unforeseen consequences. In situations such as store migration, Core Data will create instances of `NSManagedObjectContext` for its own use. Under these circumstances, you cannot rely on any features of your custom subclass. Any `NSManagedObject` subclass must always be fully compatible with `NSManagedObjectContext` (that is, it cannot rely on features of a subclass of `NSManagedObjectContext`).

## Topics

### Creating a context
- [convenience init(NSManagedObjectContext.ConcurrencyType)](nsmanagedobjectcontext/init(_:).md)
  Creates a context that uses the specified concurrency type.
- [NSManagedObjectContext.ConcurrencyType](nsmanagedobjectcontext/concurrencytype-swift.struct.md)
  The concurrency types to use with a managed object context.
- [init(concurrencyType: NSManagedObjectContextConcurrencyType)](nsmanagedobjectcontext/init(concurrencytype:).md)
  Creates a context that uses the specified concurrency type.
- [enum NSManagedObjectContextConcurrencyType](nsmanagedobjectcontextconcurrencytype.md)
  The concurrency types you can use with a managed object context.
### Configuring a context
- [var persistentStoreCoordinator: NSPersistentStoreCoordinator?](nsmanagedobjectcontext/persistentstorecoordinator.md)
  The persistent store coordinator of the context.
- [var parent: NSManagedObjectContext?](nsmanagedobjectcontext/parent.md)
  The parent of the context.
- [var name: String?](nsmanagedobjectcontext/name.md)
  The developer-provided name of the context.
- [var userInfo: NSMutableDictionary](nsmanagedobjectcontext/userinfo.md)
  The user information for the context.
### Registering and fetching objects
- [func fetch(NSFetchRequest<any NSFetchRequestResult>) throws -> [Any]](nsmanagedobjectcontext/fetch(_:)-38ys1.md)
  Returns an array of objects that meet the criteria of the specified fetch request.
- [func fetch<T>(NSFetchRequest<T>) throws -> [T]](nsmanagedobjectcontext/fetch(_:)-4xeoz.md)
  Returns an array of items of the specified type that meet the fetch request’s critieria.
- [func count(for: NSFetchRequest<any NSFetchRequestResult>) throws -> Int](nsmanagedobjectcontext/count(for:)-93zbm.md)
  Returns the number of objects the specified request fetches when it executes.
- [func registeredObject(for: NSManagedObjectID) -> NSManagedObject?](nsmanagedobjectcontext/registeredobject(for:).md)
  Returns an object that exists in the context.
- [func object(with: NSManagedObjectID) -> NSManagedObject](nsmanagedobjectcontext/object(with:).md)
  Returns either an existing object from the context or a fault that represents that object.
- [func existingObject(with: NSManagedObjectID) throws -> NSManagedObject](nsmanagedobjectcontext/existingobject(with:).md)
  Returns an existing object from either the context or the persistent store.
- [var registeredObjects: Set<NSManagedObject>](nsmanagedobjectcontext/registeredobjects.md)
  The set of registered managed objects in the context.
- [func count<T>(for: NSFetchRequest<T>) throws -> Int](nsmanagedobjectcontext/count(for:)-3r91z.md)
  Returns a count of the objects the specified request fetches when it executes.
- [func execute(NSPersistentStoreRequest) throws -> NSPersistentStoreResult](nsmanagedobjectcontext/execute(_:).md)
  Passes a request to the persistent store without affecting the contents of the managed object context, and returns a persistent store result.
- [func refreshAllObjects()](nsmanagedobjectcontext/refreshallobjects.md)
  Refreshes all of the registered managed objects in the context.
- [var retainsRegisteredObjects: Bool](nsmanagedobjectcontext/retainsregisteredobjects.md)
  A Boolean value that indicates whether the context keeps strong references to all registered managed objects.
### Handling managed objects
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
- [func refresh(NSManagedObject, mergeChanges: Bool)](nsmanagedobjectcontext/refresh(_:mergechanges:).md)
  Updates the persistent properties of a managed object to use the latest values from the persistent store.
- [func processPendingChanges()](nsmanagedobjectcontext/processpendingchanges.md)
  Forces the context to process changes to the object graph.
- [func observeValue(forKeyPath: String?, of: Any?, change: [String : Any]?, context: UnsafeMutableRawPointer?)](nsmanagedobjectcontext/observevalue(forkeypath:of:change:context:).md)
  Allows a context that has registered as an observer of a value to be notified of a change to that value.
### Managing concurrency
- [let NSManagedObjectContextQueryGenerationKey: String](nsmanagedobjectcontextquerygenerationkey.md)
  Constant used to reference the query generation token.
- [class func mergeChanges(fromRemoteContextSave: [AnyHashable : Any], into: [NSManagedObjectContext])](nsmanagedobjectcontext/mergechanges(fromremotecontextsave:into:).md)
  Handles changes from other processes or from a serialized state.
- [var automaticallyMergesChangesFromParent: Bool](nsmanagedobjectcontext/automaticallymergeschangesfromparent.md)
  A Boolean value that indicates whether the context automatically merges changes saved to its persistent store coordinator or parent context.
- [var concurrencyType: NSManagedObjectContextConcurrencyType](nsmanagedobjectcontext/concurrencytype-swift.property.md)
  The concurrency type for the context.
- [var mergePolicy: Any](nsmanagedobjectcontext/mergepolicy.md)
  The merge policy of the context.
- [var queryGenerationToken: NSQueryGenerationToken?](nsmanagedobjectcontext/querygenerationtoken.md)
  Returns the token associated with the query generation currently in use by this context.
- [var transactionAuthor: String?](nsmanagedobjectcontext/transactionauthor.md)
  The author for the context that is used as an identifier in persistent history transactions.
- [func mergeChanges(fromContextDidSave: Notification)](nsmanagedobjectcontext/mergechanges(fromcontextdidsave:).md)
  Merges the changes specified in a given notification.
- [func setQueryGenerationFrom(NSQueryGenerationToken?) throws](nsmanagedobjectcontext/setquerygenerationfrom(_:).md)
  Sets the query generation this context should use.
### Managing notifications
- [static let didChangeObjectsNotification: Notification.Name](nsmanagedobjectcontext/didchangeobjectsnotification.md)
  A notification that posts when a context makes changes to its registered objects.
- [static let NSManagedObjectContextObjectsDidChange: NSNotification.Name](../foundation/nsnotification/name/1506884-nsmanagedobjectcontextobjectsdid.md)
  A notification that posts when there are changes to context’s registered managed objects.
- [static let didSaveObjectsNotification: Notification.Name](nsmanagedobjectcontext/didsaveobjectsnotification.md)
  A notification that posts after a context completes a save.
- [static let NSManagedObjectContextDidSave: NSNotification.Name](../foundation/nsnotification/name/1506380-nsmanagedobjectcontextdidsave.md)
  A notification that posts after a context finishes writing unsaved changes.
- [static let willSaveObjectsNotification: Notification.Name](nsmanagedobjectcontext/willsaveobjectsnotification.md)
  A notification that posts before a context writes pending changes to disk.
- [static let NSManagedObjectContextWillSave: NSNotification.Name](../foundation/nsnotification/name/1506816-nsmanagedobjectcontextwillsave.md)
  A notification that posts before a context writes unsaved changes.
- [let NSInsertedObjectsKey: String](nsinsertedobjectskey.md)
  A key for the set of objects that were inserted into the context.
- [let NSUpdatedObjectsKey: String](nsupdatedobjectskey.md)
  A key for the set of objects that were updated.
- [let NSDeletedObjectsKey: String](nsdeletedobjectskey.md)
  A key for the set of objects that were marked for deletion during the previous event.
- [let NSRefreshedObjectsKey: String](nsrefreshedobjectskey.md)
  A key for the set of objects that were refreshed but were not dirtied in the scope of this context.
- [let NSInvalidatedObjectsKey: String](nsinvalidatedobjectskey.md)
  A key for the set of objects that were invalidated.
- [let NSInvalidatedAllObjectsKey: String](nsinvalidatedallobjectskey.md)
  A key that specifies that all objects in the context have been invalidated.
- [static let didMergeChangesObjectIDsNotification: Notification.Name](nsmanagedobjectcontext/didmergechangesobjectidsnotification.md)
  A notification that posts after a context finishes merging changes from another notification.
- [static let didSaveObjectIDsNotification: Notification.Name](nsmanagedobjectcontext/didsaveobjectidsnotification.md)
  A notification that posts after a context finishes saving changes to its managed objects.
- [NSManagedObjectContext.NotificationKey](nsmanagedobjectcontext/notificationkey.md)
  Keys to access details in user info dictionaries of managed object context notifications.
### Managing unsaved and uncommitted changes
- [func save() throws](nsmanagedobjectcontext/save.md)
  Attempts to commit unsaved changes to registered objects to the context’s parent store.
- [var hasChanges: Bool](nsmanagedobjectcontext/haschanges.md)
  A Boolean value that indicates whether the context has uncommitted changes.
### Undoing changes
- [var undoManager: UndoManager?](nsmanagedobjectcontext/undomanager.md)
  The object that provides undo support for the context.
- [func undo()](nsmanagedobjectcontext/undo.md)
  Sends an undo message to the context’s undo manager, asking it to reverse the latest uncommitted changes applied to objects in the object graph.
- [func redo()](nsmanagedobjectcontext/redo.md)
  Sends a redo message to the context’s undo manager, asking it to reverse the latest undo operation applied to objects in the object graph.
- [func reset()](nsmanagedobjectcontext/reset.md)
  Returns the context to its base state.
- [func rollback()](nsmanagedobjectcontext/rollback.md)
  Removes everything from the undo stack, discards all insertions and deletions, and restores updated objects to their last committed values.
### Handling delete propagation
- [var propagatesDeletesAtEndOfEvent: Bool](nsmanagedobjectcontext/propagatesdeletesatendofevent.md)
  A Boolean value that indicates whether the context propagates deletes at the end of the event in which a change was made.
### Managing the staleness interval
- [var stalenessInterval: TimeInterval](nsmanagedobjectcontext/stalenessinterval.md)
  The maximum length of time that may have elapsed since the store previously fetched data before fulfilling a fault issues a new fetch.
### Performing block operations
- [func perform(() -> Void)](nsmanagedobjectcontext/perform(_:).md)
  Asynchronously performs the specified closure on the context’s queue.
- [func perform<T>(schedule: NSManagedObjectContext.ScheduledTaskType, () throws -> T) async rethrows -> T](nsmanagedobjectcontext/perform(schedule:_:).md)
  Submits a closure to the context’s queue for asynchronous execution.
- [func performAndWait(() -> Void)](nsmanagedobjectcontext/performandwait(_:)-ypye.md)
  Synchronously performs the specified closure on the context’s queue.
- [func performAndWait<T>(() throws -> T) rethrows -> T](nsmanagedobjectcontext/performandwait(_:)-6aaf1.md)
  Submits a closure to the context’s queue for synchronous execution.
- [NSManagedObjectContext.ScheduledTaskType](nsmanagedobjectcontext/scheduledtasktype.md)
  The different types of scheduled tasks.
### Deprecated
- [Deprecated symbols](nsmanagedobjectcontext-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

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
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](../AppKit/NSEditor.md)
- [NSEditorRegistration](../AppKit/NSEditorRegistration.md)
- [NSLocking](../Foundation/NSLocking.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSManagedObject](nsmanagedobject.md)
  The base class that all Core Data model objects inherit from.
- [class NSManagedObjectID](nsmanagedobjectid.md)
  A compact, universal identifier for a managed object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext)*