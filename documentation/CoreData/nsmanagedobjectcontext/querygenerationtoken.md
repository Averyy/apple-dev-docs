# queryGenerationToken

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

Returns the token associated with the query generation currently in use by this context.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var queryGenerationToken: NSQueryGenerationToken? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSQueryGenerationToken * queryGenerationToken;
```

## Mentions

- [Accessing data when the store changes](../accessing-data-when-the-store-changes.md)

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
- [var transactionAuthor: String?](./transactionauthor.md)
  The author for the context that is used as an identifier in persistent history transactions.
- [func mergeChanges(fromContextDidSave: Notification)](./mergechanges%28fromcontextdidsave%29.md)
  Merges the changes specified in a given notification.
- [func setQueryGenerationFrom(NSQueryGenerationToken?) throws](./setquerygenerationfrom%28_%29.md)
  Sets the query generation this context should use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/querygenerationtoken)*