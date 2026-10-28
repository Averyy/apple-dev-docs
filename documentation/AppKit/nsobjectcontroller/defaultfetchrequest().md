# defaultFetchRequest()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the default fetch request used by the receiver.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func defaultFetchRequest() -> NSFetchRequest<any NSFetchRequestResult>
```

```objc
- (NSFetchRequest *) defaultFetchRequest;
```

## Return Value

The default NSFetchResult used by the receiver.

## See Also

### Core Data support
- [var entityName: String?](./entityname.md)
  The entity name used by the receiver to create new objects.
- [func fetch(Any?)](./fetch%28_%29.md)
  Causes the receiver to fetch the data objects specified by the entity name and fetch predicate.
- [var usesLazyFetching: Bool](./useslazyfetching.md)
  A Boolean that indicates whether the receiver uses lazy fetching.
- [var fetchPredicate: NSPredicate?](./fetchpredicate.md)
  The receiver’s fetch predicate.
- [var managedObjectContext: NSManagedObjectContext?](./managedobjectcontext.md)
  The receiver’s managed object context.
- [func fetch(with: NSFetchRequest<any NSFetchRequestResult>?, merge: Bool) throws](./fetch%28with,merge%29.md)
  Subclasses should override this method to customize a fetch request, for example to specify fetch limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/defaultfetchrequest())*