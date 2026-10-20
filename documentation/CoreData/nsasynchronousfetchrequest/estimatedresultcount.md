# estimatedResultCount

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A configuration parameter that assists Core Data with scheduling the asynchronous fetch request.

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
var estimatedResultCount: Int { get set }
```

```objc
@property (nonatomic) NSInteger estimatedResultCount;
```

## See Also

### Preparing a Request
- [var completionBlock: NSPersistentStoreAsynchronousFetchResultCompletionBlock?](./completionblock.md)
  The block that is executed when the fetch request has completed.
- [var fetchRequest: NSFetchRequest<ResultType>](./fetchrequest.md)
  The underlying fetch request that is executed asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/estimatedresultcount)*