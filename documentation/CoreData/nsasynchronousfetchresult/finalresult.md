# finalResult

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The results that were received from the fetch request.

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
var finalResult: [ResultType]? { get }
```

```objc
@property (strong, readonly, nullable) NSArray<id<NSFetchRequestResult>> * finalResult;
```

## See Also

### Getting Information About a Result
- [var fetchRequest: NSAsynchronousFetchRequest<ResultType>](./fetchrequest.md)
  The underlying fetch request that was executed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsasynchronousfetchresult/finalresult)*