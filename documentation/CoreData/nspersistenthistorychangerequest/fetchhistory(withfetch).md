# fetchHistory(withFetch:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Retrieves history based on a fetch request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func fetchHistory(withFetch fetchRequest: NSFetchRequest<any NSFetchRequestResult>) -> Self
```

```objc
+ (instancetype) fetchHistoryWithFetchRequest:(NSFetchRequest *) fetchRequest;
```

#### Return Value

A persistent history fetch request ([`NSPersistentHistoryChangeRequest`](../nspersistenthistorychangerequest.md)) built using an existing fetch request.

## Parameters

- `fetchRequest`: The fetch request that defines the history bounds.

## See Also

### Fetching History
- [class func fetchHistory(after: Date) -> Self](./fetchhistory%28after%29-qi5b.md)
  Retrieves history since a given date.
- [class func fetchHistory(after: NSPersistentHistoryToken?) -> Self](./fetchhistory%28after%29-3rmfm.md)
  Retrieves the request history after a given token.
- [class func fetchHistory(after: NSPersistentHistoryTransaction?) -> Self](./fetchhistory%28after%29-9cuj5.md)
  Retrieves history since a given transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest/fetchhistory(withfetch:))*