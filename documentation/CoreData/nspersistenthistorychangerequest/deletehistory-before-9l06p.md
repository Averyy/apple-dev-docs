# deleteHistory(before:)

**Framework**: Core Data  
**Kind**: method

Purges history older than a given transaction.

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
class func deleteHistory(before transaction: NSPersistentHistoryTransaction?) -> Self
```

#### Return Value

A delete history change request ([`NSPersistentHistoryChangeRequest`](nspersistenthistorychangerequest.md)) using an end transaction boundary.

## Parameters

- `transaction`: The transaction that marks the end of the delete history request.

## See Also

- [class func deleteHistory(before: Date) -> Self](nspersistenthistorychangerequest/deletehistory(before:)-7t2th.md)
  Purges history older than a given date.
- [class func deleteHistory(before: NSPersistentHistoryToken?) -> Self](nspersistenthistorychangerequest/deletehistory(before:)-5kghb.md)
  Purges history older than that defined by a given token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest/deletehistory(before:)-9l06p)*