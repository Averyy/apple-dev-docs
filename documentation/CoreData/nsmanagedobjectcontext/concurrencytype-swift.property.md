# concurrencyType

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The concurrency type for the context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var concurrencyType: NSManagedObjectContextConcurrencyType { get }
```

```objc
@property (readonly) NSManagedObjectContextConcurrencyType concurrencyType;
```

## Discussion

For more details on concurrency type, see [Concurrency](../nsmanagedobjectcontext.md#Concurrency).

## See Also

### Related Documentation
- [init(concurrencyType: NSManagedObjectContextConcurrencyType)](./init%28concurrencytype%29.md)
  Creates a context that uses the specified concurrency type.
### Managing concurrency
- [let NSManagedObjectContextQueryGenerationKey: String](../nsmanagedobjectcontextquerygenerationkey.md)
  Constant used to reference the query generation token.
- [class func mergeChanges(fromRemoteContextSave: [AnyHashable : Any], into: [NSManagedObjectContext])](./mergechanges%28fromremotecontextsave,into%29.md)
  Handles changes from other processes or from a serialized state.
- [var automaticallyMergesChangesFromParent: Bool](./automaticallymergeschangesfromparent.md)
  A Boolean value that indicates whether the context automatically merges changes saved to its persistent store coordinator or parent context.
- [var mergePolicy: Any](./mergepolicy.md)
  The merge policy of the context.
- [var queryGenerationToken: NSQueryGenerationToken?](./querygenerationtoken.md)
  Returns the token associated with the query generation currently in use by this context.
- [var transactionAuthor: String?](./transactionauthor.md)
  The author for the context that is used as an identifier in persistent history transactions.
- [func mergeChanges(fromContextDidSave: Notification)](./mergechanges%28fromcontextdidsave%29.md)
  Merges the changes specified in a given notification.
- [func setQueryGenerationFrom(NSQueryGenerationToken?) throws](./setquerygenerationfrom%28_%29.md)
  Sets the query generation this context should use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/concurrencytype-swift.property)*