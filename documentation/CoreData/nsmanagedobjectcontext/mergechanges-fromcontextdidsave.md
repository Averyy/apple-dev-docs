# mergeChanges(fromContextDidSave:)

**Framework**: Coredata  
**Kind**: method

Merges the changes specified in a given notification.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func mergeChanges(fromContextDidSave notification: Notification)
```

## Mentions

- [Accessing data when the store changes](accessing-data-when-the-store-changes.md)
- [Consuming relevant store changes](consuming-relevant-store-changes.md)

#### Discussion

This method refreshes any objects which have been updated in the other context, faults in any newly-inserted objects, and invokes [`delete(_:)`](nsmanagedobjectcontext/delete(_:).md): on those which have been deleted.

You can pass a [`NSManagedObjectContextDidSave`](https://developer.apple.com/documentation/foundation/nsnotification/name/1506380-nsmanagedobjectcontextdidsave) notification posted by a managed object context on another thread, however you must not use the managed objects in the user info dictionary directly. For more details, see Concurrency with Core Data.

> **Note**: Objective-C uses instances of [`NSManagedObjectContextDidSaveNotification`](nsmanagedobjectcontextdidsavenotification.md) instead of [`NSManagedObjectContextDidSave`](https://developer.apple.com/documentation/foundation/nsnotification/name/1506380-nsmanagedobjectcontextdidsave).

## Parameters

- `notification`: An instance of an   notification posted by another context.

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
- [var transactionAuthor: String?](nsmanagedobjectcontext/transactionauthor.md)
  The author for the context that is used as an identifier in persistent history transactions.
- [func setQueryGenerationFrom(NSQueryGenerationToken?) throws](nsmanagedobjectcontext/setquerygenerationfrom(_:).md)
  Sets the query generation this context should use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/mergechanges(fromcontextdidsave:))*