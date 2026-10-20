# entityName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The entity name used by the receiver to create new objects.

**Availability**:
- macOS

## Declaration

```swift
var entityName: String? { get set }
```

```objc
@property (copy, nullable) NSString * entityName;
```

## See Also

### Core Data support
- [func fetch(Any?)](./fetch%28_%29.md)
  Causes the receiver to fetch the data objects specified by the entity name and fetch predicate.
- [var usesLazyFetching: Bool](./useslazyfetching.md)
  A Boolean that indicates whether the receiver uses lazy fetching.
- [func defaultFetchRequest() -> NSFetchRequest<any NSFetchRequestResult>](./defaultfetchrequest%28%29.md)
  Returns the default fetch request used by the receiver.
- [var fetchPredicate: NSPredicate?](./fetchpredicate.md)
  The receiver’s fetch predicate.
- [var managedObjectContext: NSManagedObjectContext?](./managedobjectcontext.md)
  The receiver’s managed object context.
- [func fetch(with: NSFetchRequest<any NSFetchRequestResult>?, merge: Bool) throws](./fetch%28with,merge%29.md)
  Subclasses should override this method to customize a fetch request, for example to specify fetch limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/entityname)*