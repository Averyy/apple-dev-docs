# fetchRequest

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The underlying fetch request that is executed asynchronously.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var fetchRequest: NSFetchRequest<ResultType> { get }
```

```objc
@property (strong, readonly) NSFetchRequest<id<NSFetchRequestResult>> * fetchRequest;
```

## See Also

### Preparing a Request
- [var completionBlock: NSPersistentStoreAsynchronousFetchResultCompletionBlock?](./completionblock.md)
  The block that is executed when the fetch request has completed.
- [var estimatedResultCount: Int](./estimatedresultcount.md)
  A configuration parameter that assists Core Data with scheduling the asynchronous fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/fetchrequest)*