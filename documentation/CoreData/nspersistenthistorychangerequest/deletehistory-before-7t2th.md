# deleteHistory(before:)

**Framework**: Core Data  
**Kind**: method

Purges history older than a given date.

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
class func deleteHistory(before date: Date) -> Self
```

#### Return Value

A delete history change request ([`NSPersistentHistoryChangeRequest`](nspersistenthistorychangerequest.md)) using an end date boundary.

## Parameters

- `date`: The date used to define the end of the delete history request.

## See Also

- [class func deleteHistory(before: NSPersistentHistoryToken?) -> Self](nspersistenthistorychangerequest/deletehistory(before:)-5kghb.md)
  Purges history older than that defined by a given token.
- [class func deleteHistory(before: NSPersistentHistoryTransaction?) -> Self](nspersistenthistorychangerequest/deletehistory(before:)-9l06p.md)
  Purges history older than a given transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest/deletehistory(before:)-7t2th)*