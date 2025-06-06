# transactionAuthor

**Framework**: Core Data  
**Kind**: property

The author for the context that is used as an identifier in persistent history transactions.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var transactionAuthor: String? { get set }
```

## Mentions

- [Consuming relevant store changes](consuming-relevant-store-changes.md)

#### Discussion

Set a managed object context’s [`transactionAuthor`](nsmanagedobjectcontext/transactionauthor.md) before saving it to differentiate among multiple call sites that modify the same context. Doing this records an [`author`](nspersistenthistorytransaction/author.md) in subsequent transactions.

```swift
func addColor(_ name: String, in context: NSManagedObjectContext) {
    let color = Color(context: context)
    color.name = name
    color.creationDate = Date()

    // set the transaction author
    context.transactionAuthor = "addColor"
    persistentContainer.saveContext(context)
    context.transactionAuthor = nil
}
```

Reset the context’s [`transactionAuthor`](nsmanagedobjectcontext/transactionauthor.md) to nil after the save to prevent misattribution of future transactions.

## See Also

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
- [func mergeChanges(fromContextDidSave: Notification)](nsmanagedobjectcontext/mergechanges(fromcontextdidsave:).md)
  Merges the changes specified in a given notification.
- [func setQueryGenerationFrom(NSQueryGenerationToken?) throws](nsmanagedobjectcontext/setquerygenerationfrom(_:).md)
  Sets the query generation this context should use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/transactionauthor)*