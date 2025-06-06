# resultType

**Framework**: Core Data  
**Kind**: property

The type of result that this request returns.

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
var resultType: NSPersistentHistoryResultType { get set }
```

#### Discussion

This value defaults to [`NSPersistentHistoryResultType.transactionsAndChanges`](nspersistenthistoryresulttype/transactionsandchanges.md).

## See Also

- [var fetchRequest: NSFetchRequest<any NSFetchRequestResult>?](nspersistenthistorychangerequest/fetchrequest.md)
  The specified fetch request, when retrieving history.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest/resulttype)*