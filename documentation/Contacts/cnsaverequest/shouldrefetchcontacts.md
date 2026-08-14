# shouldRefetchContacts

**Framework**: Contacts  
**Kind**: property

A Boolean value that indicates whether to refetch the added and updated contacts after the save request executes.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- visionOS 1.0+

## Declaration

```swift
var shouldRefetchContacts: Bool { get set }
```

#### Discussion

The default value is [`true`](https://developer.apple.com/documentation/swift/true), so the save request refetches added and updated contacts. Set to [`false`](https://developer.apple.com/documentation/swift/false) to suppress the refetch behavior and reduce the save request’s execution time.

## See Also

- [var transactionAuthor: String?](cnsaverequest/transactionauthor.md)
  A string that identifies the author of the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsaverequest/shouldrefetchcontacts)*