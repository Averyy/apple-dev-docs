# automaticallyMergesChangesFromParent

**Framework**: Core Data  
**Kind**: property

A Boolean value that indicates whether the context automatically merges changes saved to its persistent store coordinator or parent context.

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
var automaticallyMergesChangesFromParent: Bool { get set }
```

## See Also

- [let NSManagedObjectContextQueryGenerationKey: String](nsmanagedobjectcontextquerygenerationkey.md)
  Constant used to reference the query generation token.
- [class func mergeChanges(fromRemoteContextSave: [AnyHashable : Any], into: [NSManagedObjectContext])](nsmanagedobjectcontext/mergechanges(fromremotecontextsave:into:).md)
  Handles changes from other processes or from a serialized state.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/automaticallymergeschangesfromparent)*