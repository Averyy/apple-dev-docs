# cacheName

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The name of the file used to cache section information.

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
var cacheName: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * cacheName;
```

## Discussion

The file itself is stored in a private directory; you can only access it by name using [`deleteCache(withName:)`](./deletecache%28withname%29.md)

## See Also

### Related Documentation
- [init(fetchRequest: NSFetchRequest<ResultType>, managedObjectContext: NSManagedObjectContext, sectionNameKeyPath: String?, cacheName: String?)](./init%28fetchrequest,managedobjectcontext,sectionnamekeypath,cachename%29.md)
  Returns a fetch request controller initialized using the given arguments.
### Getting Configuration Information
- [var fetchRequest: NSFetchRequest<ResultType>](./fetchrequest.md)
  The fetch request used to do the fetching.
- [var managedObjectContext: NSManagedObjectContext](./managedobjectcontext.md)
  The managed object context used to fetch objects.
- [var sectionNameKeyPath: String?](./sectionnamekeypath.md)
  The key path of the attribute that determines which section the fetched entity belongs to.
- [var delegate: (any NSFetchedResultsControllerDelegate)?](./delegate.md)
  The object that is notified when the fetched results changed.
- [class func deleteCache(withName: String?)](./deletecache%28withname%29.md)
  Deletes the cached section information with the given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/cachename)*