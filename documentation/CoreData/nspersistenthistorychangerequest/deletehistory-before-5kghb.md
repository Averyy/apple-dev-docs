# deleteHistory(before:)

**Framework**: Core Data  
**Kind**: method

Purges history older than that defined by a given token.

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
class func deleteHistory(before token: NSPersistentHistoryToken?) -> Self
```

## Mentions

- [Consuming relevant store changes](consuming-relevant-store-changes.md)

#### Return Value

A delete history change request ([`NSPersistentHistoryChangeRequest`](nspersistenthistorychangerequest.md)) using an end token bookmark boundary.

## Parameters

- `token`: The bookmark that marks the end of the delete history request.

## See Also

- [class func deleteHistory(before: Date) -> Self](nspersistenthistorychangerequest/deletehistory(before:)-7t2th.md)
  Purges history older than a given date.
- [class func deleteHistory(before: NSPersistentHistoryTransaction?) -> Self](nspersistenthistorychangerequest/deletehistory(before:)-9l06p.md)
  Purges history older than a given transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest/deletehistory(before:)-5kghb)*