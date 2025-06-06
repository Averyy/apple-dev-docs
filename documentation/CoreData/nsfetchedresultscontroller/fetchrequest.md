# fetchRequest

**Framework**: Core Data  
**Kind**: property

The fetch request used to do the fetching.

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
var fetchRequest: NSFetchRequest<ResultType> { get }
```

#### Discussion

If you want to modify the fetch request, you must follow the steps described in [`Modifying the fetch request`](nsfetchedresultscontroller#Modifying-the-fetch-request.md).

## See Also

- [init(fetchRequest: NSFetchRequest<ResultType>, managedObjectContext: NSManagedObjectContext, sectionNameKeyPath: String?, cacheName: String?)](nsfetchedresultscontroller/init(fetchrequest:managedobjectcontext:sectionnamekeypath:cachename:).md)
  Returns a fetch request controller initialized using the given arguments.
- [var managedObjectContext: NSManagedObjectContext](nsfetchedresultscontroller/managedobjectcontext.md)
  The managed object context used to fetch objects.
- [var sectionNameKeyPath: String?](nsfetchedresultscontroller/sectionnamekeypath.md)
  The key path of the attribute that determines which section the fetched entity belongs to.
- [var cacheName: String?](nsfetchedresultscontroller/cachename.md)
  The name of the file used to cache section information.
- [var delegate: (any NSFetchedResultsControllerDelegate)?](nsfetchedresultscontroller/delegate.md)
  The object that is notified when the fetched results changed.
- [class func deleteCache(withName: String?)](nsfetchedresultscontroller/deletecache(withname:).md)
  Deletes the cached section information with the given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/fetchrequest)*