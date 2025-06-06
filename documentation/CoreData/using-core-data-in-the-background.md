# Using Core Data in the background

**Framework**: Core Data

Use Core Data in both a single-threaded and multithreaded app.

#### Overview

Core Data works in a multithreaded environment. However, not every object under the Core Data framework is thread safe. To use Core Data in a multithreaded environment, ensure that:

- Bind managed object contexts to the thread (queue) that they’re initialization on.
- Bind managed objects that you retrieve from a context to the same queue as the context.

##### Comparing Main Queue and Private Queue Contexts

There are two types of managed object contexts: main queue and private queue. You define the type of context when you initialize it.

A main queue context (as defined by a [`NSManagedObjectContextConcurrencyType.mainQueueConcurrencyType`](nsmanagedobjectcontextconcurrencytype/mainqueueconcurrencytype.md)) is specifically for use with your application interface. Only use it on the main queue of your app.

A private queue context (as defined by a [`NSManagedObjectContextConcurrencyType.privateQueueConcurrencyType`](nsmanagedobjectcontextconcurrencytype/privatequeueconcurrencytype.md)) creates its own queue upon initialization. Only use it on that queue. Because the queue is private and internal to the [`NSManagedObjectContext`](nsmanagedobjectcontext.md) instance, you can only access it through the [`perform(_:)`](nsmanagedobjectcontext/perform(_:).md) and the [`performAndWait(_:)`](nsmanagedobjectcontext/performandwait(_:)-ypye.md) methods.

##### Initializing and Configuring a Context

Use [`init(concurrencyType:)`](nsmanagedobjectcontext/init(concurrencytype:).md) to create a new context. For example, to create a private queue context:

```swift
// Create a private queue context.
let context = NSManagedObjectContext(.privateQueue)
```

The parameter you pass during initialization determines what type of [`NSManagedObjectContext`](nsmanagedobjectcontext.md) you receive.

When you use the [`NSPersistentContainer`](nspersistentcontainer.md), you configure the [`viewContext`](nspersistentcontainer/viewcontext.md) property as a main queue ([`NSManagedObjectContextConcurrencyType.mainQueueConcurrencyType`](nsmanagedobjectcontextconcurrencytype/mainqueueconcurrencytype.md)) context, and configure the contexts associated with [`performBackgroundTask(_:)`](nspersistentcontainer/performbackgroundtask(_:)-39sch.md) and [`newBackgroundContext()`](nspersistentcontainer/newbackgroundcontext().md) as a private queue ([`NSManagedObjectContextConcurrencyType.privateQueueConcurrencyType`](nsmanagedobjectcontextconcurrencytype/privatequeueconcurrencytype.md)).

##### Avoiding Problems

 Data processing can be CPU-intensive, and if it’s performed on the main queue, it can result in unresponsiveness in the user interface. If your application processes data, such as importing data into Core Data from JSON, create a private queue context and perform the import on the private context.

 Doing so can result in corruption of the data and termination of the app. When it’s necessary to hand off a managed object reference from one queue to another, use [`NSManagedObjectID`](nsmanagedobjectid.md) instances.

You retrieve the managed object ID of a managed object by calling the `objectID` accessor on the [`NSManagedObject`](nsmanagedobject.md) instance.

## See Also

- [Loading and Displaying a Large Data Feed](../swiftui/loading_and_displaying_a_large_data_feed.md)
  Consume data in the background, and lower memory use by batching imports and preventing duplicate records.
- [Conflict resolution](conflict-resolution.md)
  Detect and resolve conflicts that occur when data is changed on multiple threads.
- [Batch processing](batch-processing.md)
  Use batch processes to manage large data changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/using-core-data-in-the-background)*