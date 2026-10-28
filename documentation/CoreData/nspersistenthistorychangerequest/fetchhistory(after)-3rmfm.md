# fetchHistory(after:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Retrieves the request history after a given token.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func fetchHistory(after token: NSPersistentHistoryToken?) -> Self
```

```objc
+ (instancetype) fetchHistoryAfterToken:(NSPersistentHistoryToken *) token;
```

## Mentions

- [Consuming relevant store changes](../consuming-relevant-store-changes.md)

## Return Value

A persistent history fetch request ([`NSPersistentHistoryChangeRequest`](../nspersistenthistorychangerequest.md)) with an initial token bookmark boundary.

## Parameters

- `token`: The bookmark that defines the start of the request history.

## See Also

### Fetching History
- [class func fetchHistory(after: Date) -> Self](./fetchhistory%28after%29-qi5b.md)
  Retrieves history since a given date.
- [class func fetchHistory(after: NSPersistentHistoryTransaction?) -> Self](./fetchhistory%28after%29-9cuj5.md)
  Retrieves history since a given transaction.
- [class func fetchHistory(withFetch: NSFetchRequest<any NSFetchRequestResult>) -> Self](./fetchhistory%28withfetch%29.md)
  Retrieves history based on a fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest/fetchhistory(after:)-3rmfm)*