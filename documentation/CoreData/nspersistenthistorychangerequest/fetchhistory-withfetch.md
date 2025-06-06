# fetchHistory(withFetch:)

**Framework**: Core Data  
**Kind**: method

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

#### Return Value

A persistent history fetch request ([`NSPersistentHistoryChangeRequest`](nspersistenthistorychangerequest.md)) built using an existing fetch request.

## Parameters

- `fetchRequest`: The fetch request that defines the history bounds.

## See Also

- [class func fetchHistory(after: Date) -> Self](nspersistenthistorychangerequest/fetchhistory(after:)-qi5b.md)
  Retrieves history since a given date.
- [class func fetchHistory(after: NSPersistentHistoryToken?) -> Self](nspersistenthistorychangerequest/fetchhistory(after:)-3rmfm.md)
  Retrieves the request history after a given token.
- [class func fetchHistory(after: NSPersistentHistoryTransaction?) -> Self](nspersistenthistorychangerequest/fetchhistory(after:)-9cuj5.md)
  Retrieves history since a given transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest/fetchhistory(withfetch:))*