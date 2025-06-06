# performFetch()

**Framework**: Core Data  
**Kind**: method

Executes the controller’s fetch request.

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
func performFetch() throws
```

#### Discussion

After you execute this method, access the controller’s fetched objects using the [`fetchedObjects`](nsfetchedresultscontroller/fetchedobjects.md) property.

> ❗ **Important**:  If you specify a value for the `sectionNameKeyPath` parameter when you initialize the fetched results controller, the fetch request must include a sort descriptor for the corresponding key path; otherwise, the fetch fails.

 If you specify a value for the `sectionNameKeyPath` parameter when you initialize the fetched results controller, the fetch request must include a sort descriptor for the corresponding key path; otherwise, the fetch fails.

## See Also

- [init(fetchRequest: NSFetchRequest<ResultType>, managedObjectContext: NSManagedObjectContext, sectionNameKeyPath: String?, cacheName: String?)](nsfetchedresultscontroller/init(fetchrequest:managedobjectcontext:sectionnamekeypath:cachename:).md)
  Returns a fetch request controller initialized using the given arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/performfetch())*