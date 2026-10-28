# mergePolicy

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The merge policy of the context.

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
var mergePolicy: Any { get set }
```

```objc
@property (strong) id mergePolicy;
```

## Discussion

The default is [`NSErrorMergePolicy`](../nserrormergepolicy.md). For possible values, see [`NSMergePolicy`](../nsmergepolicy.md).

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
- [var queryGenerationToken: NSQueryGenerationToken?](./querygenerationtoken.md)
  Returns the token associated with the query generation currently in use by this context.
- [var transactionAuthor: String?](./transactionauthor.md)
  The author for the context that is used as an identifier in persistent history transactions.
- [func mergeChanges(fromContextDidSave: Notification)](./mergechanges%28fromcontextdidsave%29.md)
  Merges the changes specified in a given notification.
- [func setQueryGenerationFrom(NSQueryGenerationToken?) throws](./setquerygenerationfrom%28_%29.md)
  Sets the query generation this context should use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/mergepolicy)*