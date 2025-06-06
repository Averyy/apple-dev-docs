# fetchHistory(after:)

**Framework**: Core Data  
**Kind**: method

Retrieves history since a given date.

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
class func fetchHistory(after date: Date) -> Self
```

## Mentions

- [Consuming relevant store changes](consuming-relevant-store-changes.md)

#### Return Value

A persistent history fetch request ([`NSPersistentHistoryChangeRequest`](nspersistenthistorychangerequest.md)) with an initial date boundary.

## Parameters

- `date`: The date used to define the start of the fetch history.

## See Also

- [class func fetchHistory(after: NSPersistentHistoryToken?) -> Self](nspersistenthistorychangerequest/fetchhistory(after:)-3rmfm.md)
  Retrieves the request history after a given token.
- [class func fetchHistory(after: NSPersistentHistoryTransaction?) -> Self](nspersistenthistorychangerequest/fetchhistory(after:)-9cuj5.md)
  Retrieves history since a given transaction.
- [class func fetchHistory(withFetch: NSFetchRequest<any NSFetchRequestResult>) -> Self](nspersistenthistorychangerequest/fetchhistory(withfetch:).md)
  Retrieves history based on a fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest/fetchhistory(after:)-qi5b)*