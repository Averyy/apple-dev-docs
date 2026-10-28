# mergeChanges(fromRemoteContextSave:into:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (void) mergeChangesFromRemoteContextSave:(NSDictionary *) changeNotificationData intoContexts:(NSArray<NSManagedObjectContext *> *) contexts;
```

## Mentions

- [Accessing data when the store changes](../accessing-data-when-the-store-changes.md)

## Discussion

This method more efficiently merges changes into multiple contexts as well as nested contexts. The dictionary keys should be one or more from an [`NSManagedObjectContextObjectsDidChange`](../../Foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextobjectsdidchange.md):  [`NSInsertedObjectsKey`](../nsinsertedobjectskey.md), [`NSUpdatedObjectsKey`](../nsupdatedobjectskey.md), [`NSDeletedObjectsKey`](../nsdeletedobjectskey.md). The values should be an [`NSArray`](../../Foundation/nsarray.md) of either [`NSManagedObjectID`](../nsmanagedobjectid.md) or [`NSURL`](../../Foundation/nsurl.md) objects conforming to valid results from [`uriRepresentation()`](../nsmanagedobjectid/urirepresentation%28%29.md).

## See Also

### Managing concurrency
- [let NSManagedObjectContextQueryGenerationKey: String](../nsmanagedobjectcontextquerygenerationkey.md)
  Constant used to reference the query generation token.
- [var automaticallyMergesChangesFromParent: Bool](./automaticallymergeschangesfromparent.md)
  A Boolean value that indicates whether the context automatically merges changes saved to its persistent store coordinator or parent context.
- [var concurrencyType: NSManagedObjectContextConcurrencyType](./concurrencytype-swift.property.md)
  The concurrency type for the context.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/mergechanges(fromremotecontextsave:into:))*