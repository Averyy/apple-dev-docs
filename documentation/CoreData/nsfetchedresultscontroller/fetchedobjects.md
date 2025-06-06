# fetchedObjects

**Framework**: Core Data  
**Kind**: property

The results of the fetch.

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
var fetchedObjects: [ResultType]? { get }
```

#### Discussion

The value of the property is `nil` if [`performFetch()`](nsfetchedresultscontroller/performfetch().md) hasn’t been called.

The results array only includes instances of the entity specified by the fetch request ([`fetchRequest`](nsfetchedresultscontroller/fetchrequest.md)) and that match its predicate. (If the fetch request has no predicate, then the results array includes all instances of the entity specified by the fetch request.)

The results array reflects the in-memory state of managed objects in the controller’s managed object context, not their state in the persistent store. The returned array does not, however, update as managed objects are inserted, modified, or deleted.

## See Also

- [func fetch(NSFetchRequest<any NSFetchRequestResult>) throws -> [Any]](nsmanagedobjectcontext/fetch(_:)-38ys1.md)
  Returns an array of objects that meet the criteria of the specified fetch request.
- [func object(at: IndexPath) -> ResultType](nsfetchedresultscontroller/object(at:).md)
  Returns the object at the given index path in the fetch results.
- [func indexPath(forObject: ResultType) -> IndexPath?](nsfetchedresultscontroller/indexpath(forobject:).md)
  Returns the index path of a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/fetchedobjects)*