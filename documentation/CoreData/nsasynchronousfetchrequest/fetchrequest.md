# fetchRequest

**Framework**: Core Data  
**Kind**: property

The underlying fetch request that is executed asynchronously.

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
var fetchRequest: NSFetchRequest<ResultType> { get }
```

## See Also

- [var completionBlock: NSPersistentStoreAsynchronousFetchResultCompletionBlock?](nsasynchronousfetchrequest/completionblock.md)
  The block that is executed when the fetch request has completed.
- [var estimatedResultCount: Int](nsasynchronousfetchrequest/estimatedresultcount.md)
  A configuration parameter that assists Core Data with scheduling the asynchronous fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/fetchrequest)*