# delegate

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The object that is notified when the fetched results changed.

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
unowned(unsafe) var delegate: (any NSFetchedResultsControllerDelegate)? { get set }
```

```objc
@property (nonatomic, assign, nullable) id<NSFetchedResultsControllerDelegate> delegate;
```

## Discussion

If you do not specify a delegate, the controller does not track changes to managed objects associated with its managed object context.

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
- [class func deleteCache(withName: String?)](./deletecache%28withname%29.md)
  Deletes the cached section information with the given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/delegate)*