# NSPersistentHistoryChangeRequest

**Framework**: Core Data  
**Kind**: class  
**Role**: Class

A request to fetch or purge persistent history.

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
class NSPersistentHistoryChangeRequest
```

```objc
@interface NSPersistentHistoryChangeRequest : NSPersistentStoreRequest
```

## Mentions

- [Consuming relevant store changes](./consuming-relevant-store-changes.md)

## Topics

### Configuring the Request
- [var fetchRequest: NSFetchRequest<any NSFetchRequestResult>?](./nspersistenthistorychangerequest/fetchrequest.md)
  The specified fetch request, when retrieving history.
- [var resultType: NSPersistentHistoryResultType](./nspersistenthistorychangerequest/resulttype.md)
  The type of result that this request returns.
### Getting the Token
- [var token: NSPersistentHistoryToken?](./nspersistenthistorychangerequest/token.md)
  The specified token, when retrieving history defined by a token.
### Fetching History
- [class func fetchHistory(after: Date) -> Self](./nspersistenthistorychangerequest/fetchhistory%28after%29-qi5b.md)
  Retrieves history since a given date.
- [class func fetchHistory(after: NSPersistentHistoryToken?) -> Self](./nspersistenthistorychangerequest/fetchhistory%28after%29-3rmfm.md)
  Retrieves the request history after a given token.
- [class func fetchHistory(after: NSPersistentHistoryTransaction?) -> Self](./nspersistenthistorychangerequest/fetchhistory%28after%29-9cuj5.md)
  Retrieves history since a given transaction.
- [class func fetchHistory(withFetch: NSFetchRequest<any NSFetchRequestResult>) -> Self](./nspersistenthistorychangerequest/fetchhistory%28withfetch%29.md)
  Retrieves history based on a fetch request.
### Purging History
- [class func deleteHistory(before: Date) -> Self](./nspersistenthistorychangerequest/deletehistory%28before%29-7t2th.md)
  Purges history older than a given date.
- [class func deleteHistory(before: NSPersistentHistoryToken?) -> Self](./nspersistenthistorychangerequest/deletehistory%28before%29-5kghb.md)
  Purges history older than that defined by a given token.
- [class func deleteHistory(before: NSPersistentHistoryTransaction?) -> Self](./nspersistenthistorychangerequest/deletehistory%28before%29-9l06p.md)
  Purges history older than a given transaction.

## Relationships

### Inherits From
- [NSPersistentStoreRequest](./nspersistentstorerequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Requesting History
- [class NSPersistentHistoryResult](./nspersistenthistoryresult.md)
  The result of a request to fetch persistent history.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest)*