# completionBlock

**Framework**: Core Data  
**Kind**: property

The block that is executed when the fetch request has completed.

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
var completionBlock: NSPersistentStoreAsynchronousFetchResultCompletionBlock? { get }
```

## See Also

- [var estimatedResultCount: Int](nsasynchronousfetchrequest/estimatedresultcount.md)
  A configuration parameter that assists Core Data with scheduling the asynchronous fetch request.
- [var fetchRequest: NSFetchRequest<ResultType>](nsasynchronousfetchrequest/fetchrequest.md)
  The underlying fetch request that is executed asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/completionblock)*