# managedObjectContext

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The managed object context used to fetch objects.

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
var managedObjectContext: NSManagedObjectContext { get }
```

```objc
@property (nonatomic, readonly) NSManagedObjectContext * managedObjectContext;
```

#### Discussion

The controller registers to listen to change notifications on this context and properly update its result set and section information.

## See Also

### Getting Configuration Information
- [var fetchRequest: NSFetchRequest<ResultType>](./fetchrequest.md)
  The fetch request used to do the fetching.
- [var sectionNameKeyPath: String?](./sectionnamekeypath.md)
  The key path of the attribute that determines which section the fetched entity belongs to.
- [var cacheName: String?](./cachename.md)
  The name of the file used to cache section information.
- [var delegate: (any NSFetchedResultsControllerDelegate)?](./delegate.md)
  The object that is notified when the fetched results changed.
- [class func deleteCache(withName: String?)](./deletecache%28withname%29.md)
  Deletes the cached section information with the given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/managedobjectcontext)*