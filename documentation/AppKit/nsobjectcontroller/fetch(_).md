# fetch(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Causes the receiver to fetch the data objects specified by the entity name and fetch predicate.

**Availability**:
- macOS

## Declaration

```swift
@IBAction
func fetch(_ sender: Any?)
```

```objc
- (void) fetch:(id) sender;
```

#### Discussion

Beginning with OS X v10.4 the result of this method is deferred until the next iteration of the runloop so that the error presentation mechanism can provide feedback as a sheet.

## Parameters

- `sender`: Typically the object that invoked this method.

## See Also

### Core Data support
- [var entityName: String?](./entityname.md)
  The entity name used by the receiver to create new objects.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/fetch(_:))*