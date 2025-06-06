# usesLazyFetching

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the receiver uses lazy fetching.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var usesLazyFetching: Bool { get set }
```

#### Discussion

When enabled the controller uses a number of techniques that typically make managing large data sets more efficient. As with all optimizations, you should use suitable performance analysis tools (such as Instruments) to determine the best solution.

## See Also

- [var entityName: String?](nsobjectcontroller/entityname.md)
  The entity name used by the receiver to create new objects.
- [func fetch(Any?)](nsobjectcontroller/fetch(_:).md)
  Causes the receiver to fetch the data objects specified by the entity name and fetch predicate.
- [func defaultFetchRequest() -> NSFetchRequest<any NSFetchRequestResult>](nsobjectcontroller/defaultfetchrequest.md)
  Returns the default fetch request used by the receiver.
- [var fetchPredicate: NSPredicate?](nsobjectcontroller/fetchpredicate.md)
  The receiver’s fetch predicate.
- [var managedObjectContext: NSManagedObjectContext?](nsobjectcontroller/managedobjectcontext.md)
  The receiver’s managed object context.
- [func fetch(with: NSFetchRequest<any NSFetchRequestResult>?, merge: Bool) throws](nsobjectcontroller/fetch(with:merge:).md)
  Subclasses should override this method to customize a fetch request, for example to specify fetch limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/useslazyfetching)*