# managedObjectContext

**Framework**: Core Data  
**Kind**: property

The managed object context used to fetch objects.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var managedObjectContext: NSManagedObjectContext { get }
```

#### Discussion

The controller registers to listen to change notifications on this context and properly update its result set and section information.

## See Also

- [var fetchRequest: NSFetchRequest<ResultType>](nsfetchedresultscontroller/fetchrequest.md)
  The fetch request used to do the fetching.
- [var sectionNameKeyPath: String?](nsfetchedresultscontroller/sectionnamekeypath.md)
  The key path of the attribute that determines which section the fetched entity belongs to.
- [var cacheName: String?](nsfetchedresultscontroller/cachename.md)
  The name of the file used to cache section information.
- [var delegate: (any NSFetchedResultsControllerDelegate)?](nsfetchedresultscontroller/delegate.md)
  The object that is notified when the fetched results changed.
- [class func deleteCache(withName: String?)](nsfetchedresultscontroller/deletecache(withname:).md)
  Deletes the cached section information with the given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/managedobjectcontext)*