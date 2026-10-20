# transactionAuthor

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, nullable) NSString * transactionAuthor;
```

## Mentions

- [Consuming relevant store changes](../consuming-relevant-store-changes.md)

#### Discussion

Set a managed object context’s [`transactionAuthor`](./transactionauthor.md) before saving it to differentiate among multiple call sites that modify the same context. Doing this records an [`author`](../nspersistenthistorytransaction/author.md) in subsequent transactions.

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

Reset the context’s [`transactionAuthor`](./transactionauthor.md) to nil after the save to prevent misattribution of future transactions.

## See Also

### Managing concurrency
- [let NSManagedObjectContextQueryGenerationKey: String](../nsmanagedobjectcontextquerygenerationkey.md)
  Constant used to reference the query generation token.
- [class func mergeChanges(fromRemoteContextSave: [AnyHashable : Any], into: [NSManagedObjectContext])](./mergechanges%28fromremotecontextsave,into%29.md)
  Handles changes from other processes or from a serialized state.
- [var automaticallyMergesChangesFromParent: Bool](./automaticallymergeschangesfromparent.md)
  A Boolean value that indicates whether the context automatically merges changes saved to its persistent store coordinator or parent context.
- [var concurrencyType: NSManagedObjectContextConcurrencyType](./concurrencytype-swift.property.md)
  The concurrency type for the context.
- [var mergePolicy: Any](./mergepolicy.md)
  The merge policy of the context.
- [var queryGenerationToken: NSQueryGenerationToken?](./querygenerationtoken.md)
  Returns the token associated with the query generation currently in use by this context.
- [func mergeChanges(fromContextDidSave: Notification)](./mergechanges%28fromcontextdidsave%29.md)
  Merges the changes specified in a given notification.
- [func setQueryGenerationFrom(NSQueryGenerationToken?) throws](./setquerygenerationfrom%28_%29.md)
  Sets the query generation this context should use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/transactionauthor)*