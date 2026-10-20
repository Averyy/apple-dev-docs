# deleteCache(withName:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Deletes the cached section information with the given name.

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
class func deleteCache(withName name: String?)
```

```objc
+ (void) deleteCacheWithName:(NSString *) name;
```

## Parameters

- `name`: The name of the cache file to delete.

  If `name` is `nil`, deletes all cache files.

## See Also

### Getting Configuration Information
- [var fetchRequest: NSFetchRequest<ResultType>](./fetchrequest.md)
  The fetch request used to do the fetching.
- [var managedObjectContext: NSManagedObjectContext](./managedobjectcontext.md)
  The managed object context used to fetch objects.
- [var sectionNameKeyPath: String?](./sectionnamekeypath.md)
  The key path of the attribute that determines which section the fetched entity belongs to.
- [var cacheName: String?](./cachename.md)
  The name of the file used to cache section information.
- [var delegate: (any NSFetchedResultsControllerDelegate)?](./delegate.md)
  The object that is notified when the fetched results changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/deletecache(withname:))*