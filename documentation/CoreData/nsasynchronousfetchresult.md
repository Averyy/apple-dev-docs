# NSAsynchronousFetchResult

**Framework**: Core Data  
**Kind**: class

A fetch result object that encompasses the response from an executed asynchronous fetch request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSAsynchronousFetchResult<ResultType> where ResultType : NSFetchRequestResult
```

## Topics

### Getting Information About a Result
- [var fetchRequest: NSAsynchronousFetchRequest<ResultType>](nsasynchronousfetchresult/fetchrequest.md)
  The underlying fetch request that was executed.
- [var finalResult: [ResultType]?](nsasynchronousfetchresult/finalresult.md)
  The results that were received from the fetch request.

## Relationships

### Inherits From
- [NSPersistentStoreAsynchronousResult](nspersistentstoreasynchronousresult.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSFetchRequest](nsfetchrequest.md)
  A description of search criteria used to retrieve data from a persistent store.
- [class NSAsynchronousFetchRequest](nsasynchronousfetchrequest.md)
  A fetch request that retrieves results asynchronously and supports progress notification.
- [class NSFetchedResultsController](nsfetchedresultscontroller.md)
  A controller that you use to manage the results of a Core Data fetch request and to display data to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsasynchronousfetchresult)*