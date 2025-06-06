# NSAsynchronousFetchRequest

**Framework**: Core Data  
**Kind**: class

A fetch request that retrieves results asynchronously and supports progress notification.

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
class NSAsynchronousFetchRequest<ResultType> where ResultType : NSFetchRequestResult
```

## Topics

### Initializing a Request
- [init(fetchRequest: NSFetchRequest<ResultType>, completionBlock: ((NSAsynchronousFetchResult<ResultType>) -> Void)?)](nsasynchronousfetchrequest/init(fetchrequest:completionblock:).md)
  Initializes a new asynchronous fetch request configured with the provided fetch request and completion block.
### Preparing a Request
- [var completionBlock: NSPersistentStoreAsynchronousFetchResultCompletionBlock?](nsasynchronousfetchrequest/completionblock.md)
  The block that is executed when the fetch request has completed.
- [var estimatedResultCount: Int](nsasynchronousfetchrequest/estimatedresultcount.md)
  A configuration parameter that assists Core Data with scheduling the asynchronous fetch request.
- [var fetchRequest: NSFetchRequest<ResultType>](nsasynchronousfetchrequest/fetchrequest.md)
  The underlying fetch request that is executed asynchronously.

## Relationships

### Inherits From
- [NSPersistentStoreRequest](nspersistentstorerequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSFetchRequest](nsfetchrequest.md)
  A description of search criteria used to retrieve data from a persistent store.
- [class NSAsynchronousFetchResult](nsasynchronousfetchresult.md)
  A fetch result object that encompasses the response from an executed asynchronous fetch request.
- [class NSFetchedResultsController](nsfetchedresultscontroller.md)
  A controller that you use to manage the results of a Core Data fetch request and to display data to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest)*