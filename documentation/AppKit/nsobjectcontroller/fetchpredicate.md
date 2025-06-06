# fetchPredicate

**Framework**: AppKit  
**Kind**: property

The receiver’s fetch predicate.

**Availability**:
- macOS ?+

## Declaration

```swift
var fetchPredicate: NSPredicate? { get set }
```

#### Discussion

The receiver uses `predicate` when fetching its content, for example in [`fetch(_:)`](nsobjectcontroller/fetch(_:).md). If you need to customize the fetching behavior further, you can override [`fetch(with:merge:)`](nsobjectcontroller/fetch(with:merge:).md).

## See Also

- [var entityName: String?](nsobjectcontroller/entityname.md)
  The entity name used by the receiver to create new objects.
- [func fetch(Any?)](nsobjectcontroller/fetch(_:).md)
  Causes the receiver to fetch the data objects specified by the entity name and fetch predicate.
- [var usesLazyFetching: Bool](nsobjectcontroller/useslazyfetching.md)
  A Boolean that indicates whether the receiver uses lazy fetching.
- [func defaultFetchRequest() -> NSFetchRequest<any NSFetchRequestResult>](nsobjectcontroller/defaultfetchrequest.md)
  Returns the default fetch request used by the receiver.
- [var managedObjectContext: NSManagedObjectContext?](nsobjectcontroller/managedobjectcontext.md)
  The receiver’s managed object context.
- [func fetch(with: NSFetchRequest<any NSFetchRequestResult>?, merge: Bool) throws](nsobjectcontroller/fetch(with:merge:).md)
  Subclasses should override this method to customize a fetch request, for example to specify fetch limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/fetchpredicate)*