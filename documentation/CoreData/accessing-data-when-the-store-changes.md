# Accessing data when the store changes

**Framework**: Core Data

Guarantee that a context won’t see store changes until you tell it to look.

#### Overview

Query generations give your UI a stable view of data in the database, regardless of changes happening to the store underneath. Whenever you read from a context, you see the same generation, or snapshot, of data until you choose to advance it to a later generation.

Use query generations when you want to isolate your view context from any changes made in the store by background threads in your app, app extensions, CloudKit, or other sources.

##### Ensure the Correct Type and Mode for the Persistent Store

To use query generations, the persistent store must be an [`NSSQLiteStoreType`](nssqlitestoretype.md) in write-ahead logging (WAL) journal mode. Core Data creates SQLite stores with WAL mode enabled by default.

Query generations leverage WAL mode to let you query against the historical state of the database. Core Data appends transactions to a `.sqlite-wal` file, or journal, in the same directory as the main store file. When your context reads from the journal, it starts at the transaction associated with a specific generation, instead of at the most recent transaction.

To confirm whether a custom store has WAL mode enabled, turn on SQL logging. Choose Product > Scheme > Edit Scheme, then choose the Run action, and add the following line under Arguments Passed on Launch:

```swift
-com.apple.CoreData.SQLDebug 1
```

Run your app, and look for the following output in the console:

```swift
CoreData: sql: pragma journal_mode=wal
```

If you try to use query generations with a store that’s not an [`NSSQLiteStoreType`](nssqlitestoretype.md) in WAL journal mode, your contexts gracefully revert to unpinned behavior.

##### Pin the Context to a Store Generation

By default, contexts are unpinned, and read from the store at the generation of the most recent transaction. Pinned contexts read from the store at the generation of a specific transaction.

To pin a context, call [`setQueryGenerationFrom(_:)`](nsmanagedobjectcontext/setquerygenerationfrom(_:).md) and pass an opaque [`NSQueryGenerationToken`](nsquerygenerationtoken.md). The context updates to the specified generation lazily on the next read (fetching or faulting) operation.

Use the [`current`](nsquerygenerationtoken/current.md) generation token to pin the context to the generation corresponding to the most recent store transaction. For example, pass the [`current`](nsquerygenerationtoken/current.md) generation token when setting up your stack to pin the view context to the first generation that it fetches.

```swift
// Pin the context to the generation that corresponds with the most recent
// store transaction.
do {
    try persistentContainer.viewContext.setQueryGenerationFrom(.current)
} catch {
    // Handle the error appropriately.
    print("Failed to pin the context:", error.localizedDescription)
}
```

Alternatively, use the [`queryGenerationToken`](nsmanagedobjectcontext/querygenerationtoken.md) from another pinned context to align both contexts to the same generation.

To unpin a context, call [`setQueryGenerationFrom(_:)`](nsmanagedobjectcontext/setquerygenerationfrom(_:).md), passing `nil`.

```swift
// Unpin the context.
do {
    try persistentContainer.viewContext.setQueryGenerationFrom(nil)
} catch {
    // Handle the error appropriately.
    print("Failed to unpin the context:", error.localizedDescription)
}
```

Nested contexts inherit their parent’s generation. They’re implicitly unpinned, but they see data as viewed through the generation of their parent with the addition of their parent’s pending changes.

A generation doesn’t include stores added to the store coordinator after the generation’s creation. Additionally, if you remove a store from the coordinator, don’t try to load data from the deleted store into a context.

##### Update the View Context to the Current Store Generation

Advance a context to the generation of the most recent transaction, and pin it there, by calling [`setQueryGenerationFrom(_:)`](nsmanagedobjectcontext/setquerygenerationfrom(_:).md) and passing the [`current`](nsquerygenerationtoken/current.md) token. The context updates to the specified generation lazily on the next read (fetching or faulting) operation.

```swift
// Advance the context to the generation of the most recent store transaction.
do {
    try persistentContainer.viewContext.setQueryGenerationFrom(.current)
} catch {
    // Handle the error appropriately.
    print("Failed to set the query generation:", error.localizedDescription)
}
```

Alternatively, update a context’s generation by calling any of the following.

- [`setQueryGenerationFrom(_:)`](nsmanagedobjectcontext/setquerygenerationfrom(_:).md)
- [`save()`](nsmanagedobjectcontext/save().md)
- [`mergeChanges(fromContextDidSave:)`](nsmanagedobjectcontext/mergechanges(fromcontextdidsave:).md)
- [`mergeChanges(fromRemoteContextSave:into:)`](nsmanagedobjectcontext/mergechanges(fromremotecontextsave:into:).md)
- [`reset()`](nsmanagedobjectcontext/reset().md)

Update contexts to the [`current`](nsquerygenerationtoken/current.md) generation as soon as a specific generation is no longer needed. Query generations hold a file lock open to maintain the integrity of the journal for the duration of a query generation. Once no contexts refer to a query generation, it expires, and the system can reclaim the journal disk space.

##### Refresh Objects

Refresh any managed objects registered to the context after you change the context’s query generation or unpin the context. Managed objects don’t automatically refresh, as this behavior may not be desirable and is difficult to revert.

Call [`refreshAllObjects()`](nsmanagedobjectcontext/refreshallobjects().md) on the context to refresh its existing managed objects.

```swift
// Refresh existing managed objects.
persistentContainer.viewContext.refreshAllObjects()
```

You can also refresh your objects by fetching them again. Call [`fetch(_:)`](nsmanagedobjectcontext/fetch(_:)-4xeoz.md) on the context to retrieve a fresh set of managed objects matching your request criteria.

```swift
// Alternatively, refresh objects by fetching them again.
let request = NSFetchRequest<ShoppingItem>(entityName: "ShoppingItem")
request.fetchBatchSize = 10

// Execute the fetch.
let results = await persistentContainer.viewContext.perform {
    do {
        return try self.persistentContainer.viewContext.fetch(request)
    } catch {
        // Handle the error appropriately. It's useful to use
        // `fatalError(_:file:line:)` during development.
        fatalError("Failed to refresh the objects: \(error.localizedDescription)")
    }
}
```

The fetch reads the journal from the context’s query generation if pinned, or from the most recent transaction if unpinned.

## See Also

- [Consuming relevant store changes](consuming-relevant-store-changes.md)
  Filter store transactions for changes relevant to the current view.
- [Persistent history](persistent-history.md)
  Use persistent history tracking to determine what changes have occurred in the store since the enabling of persistent history tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/accessing-data-when-the-store-changes)*