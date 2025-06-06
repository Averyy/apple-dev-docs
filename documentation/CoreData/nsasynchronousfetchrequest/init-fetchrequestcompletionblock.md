# init(fetchRequest:completionBlock:)

**Framework**: Core Data  
**Kind**: init

Initializes a new asynchronous fetch request configured with the provided fetch request and completion block.

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
init(fetchRequest request: NSFetchRequest<ResultType>, completionBlock blk: ((NSAsynchronousFetchResult<ResultType>) -> Void)? = nil)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest/init(fetchrequest:completionblock:))*