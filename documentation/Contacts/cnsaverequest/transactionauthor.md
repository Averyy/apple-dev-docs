# transactionAuthor

**Framework**: Contacts  
**Kind**: property

A string that identifies the author of the transaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var transactionAuthor: String? { get set }
```

#### Discussion

Specify a string to identify a transaction author when you save changes. Then, when you configure a [`CNChangeHistoryFetchRequest`](cnchangehistoryfetchrequest.md), provide the same string in [`excludedTransactionAuthors`](cnchangehistoryfetchrequest/excludedtransactionauthors.md) to prevent fetching changes that the author already knows about.

## See Also

- [var shouldRefetchContacts: Bool](cnsaverequest/shouldrefetchcontacts.md)
  A Boolean value that indicates whether to refetch the added and updated contacts after the save request executes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsaverequest/transactionauthor)*