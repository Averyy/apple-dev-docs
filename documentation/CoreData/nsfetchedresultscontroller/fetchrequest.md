# fetchRequest

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The fetch request used to do the fetching.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var fetchRequest: NSFetchRequest<ResultType> { get }
```

```objc
@property (nonatomic, readonly) NSFetchRequest<id<NSFetchRequestResult>> * fetchRequest;
```

## Discussion

If you want to modify the fetch request, you must follow the steps described in [Modifying the fetch request](../nsfetchedresultscontroller.md#Modifying-the-fetch-request).

## See Also

### Related Documentation
- [init(fetchRequest: NSFetchRequest<ResultType>, managedObjectContext: NSManagedObjectContext, sectionNameKeyPath: String?, cacheName: String?)](./init%28fetchrequest,managedobjectcontext,sectionnamekeypath,cachename%29.md)
  Returns a fetch request controller initialized using the given arguments.
### Getting Configuration Information
- [var managedObjectContext: NSManagedObjectContext](./managedobjectcontext.md)
  The managed object context used to fetch objects.
- [var sectionNameKeyPath: String?](./sectionnamekeypath.md)
  The key path of the attribute that determines which section the fetched entity belongs to.
- [var cacheName: String?](./cachename.md)
  The name of the file used to cache section information.
- [var delegate: (any NSFetchedResultsControllerDelegate)?](./delegate.md)
  The object that is notified when the fetched results changed.
- [class func deleteCache(withName: String?)](./deletecache%28withname%29.md)
  Deletes the cached section information with the given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/fetchrequest)*