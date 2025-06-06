# mergeChanges(fromRemoteContextSave:into:)

**Framework**: Core Data  
**Kind**: method

Handles changes from other processes or from a serialized state.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func mergeChanges(fromRemoteContextSave changeNotificationData: [AnyHashable : Any], into contexts: [NSManagedObjectContext])
```

## Mentions

- [Accessing data when the store changes](accessing-data-when-the-store-changes.md)

#### Discussion

This method more efficiently merges changes into multiple contexts as well as nested contexts. The dictionary keys should be one or more from an [`NSManagedObjectContextObjectsDidChange`](https://developer.apple.com/documentation/foundation/nsnotification/name/1506884-nsmanagedobjectcontextobjectsdid):  [`NSInsertedObjectsKey`](nsinsertedobjectskey.md), [`NSUpdatedObjectsKey`](nsupdatedobjectskey.md), [`NSDeletedObjectsKey`](nsdeletedobjectskey.md). The values should be an [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) of either [`NSManagedObjectID`](nsmanagedobjectid.md) or [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects conforming to valid results from [`uriRepresentation()`](nsmanagedobjectid/urirepresentation().md).

## See Also

- [let NSManagedObjectContextQueryGenerationKey: String](nsmanagedobjectcontextquerygenerationkey.md)
  Constant used to reference the query generation token.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/mergechanges(fromremotecontextsave:into:))*