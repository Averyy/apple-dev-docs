# fetchedObjects

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The results of the fetch.

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
var fetchedObjects: [ResultType]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<id<NSFetchRequestResult>> * fetchedObjects;
```

#### Discussion

The value of the property is `nil` if [`performFetch()`](./performfetch%28%29.md) hasn’t been called.

The results array only includes instances of the entity specified by the fetch request ([`fetchRequest`](./fetchrequest.md)) and that match its predicate. (If the fetch request has no predicate, then the results array includes all instances of the entity specified by the fetch request.)

The results array reflects the in-memory state of managed objects in the controller’s managed object context, not their state in the persistent store. The returned array does not, however, update as managed objects are inserted, modified, or deleted.

## See Also

### Related Documentation
- [func fetch(NSFetchRequest<any NSFetchRequestResult>) throws -> [Any]](../nsmanagedobjectcontext/fetch%28_%29-38ys1.md)
  Returns an array of objects that meet the criteria of the specified fetch request.
- [- executeFetchRequest:error:](../nsmanagedobjectcontext/executefetchrequest_error_.md)
  Returns an array of objects that meet the criteria of the specified fetch request.
### Accessing Results
- [func object(at: IndexPath) -> ResultType](./object%28at%29.md)
  Returns the object at the given index path in the fetch results.
- [func indexPath(forObject: ResultType) -> IndexPath?](./indexpath%28forobject%29.md)
  Returns the index path of a given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchedresultscontroller/fetchedobjects)*