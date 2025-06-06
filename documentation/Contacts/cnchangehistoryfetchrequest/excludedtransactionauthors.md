# excludedTransactionAuthors

**Framework**: Contacts  
**Kind**: property

An array of strings that identify transaction authors to exclude from the fetch results.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var excludedTransactionAuthors: [String]? { get set }
```

#### Discussion

Specify authors using the same string(s) that you use in [`CNSaveRequest`](cnsaverequest.md)’s [`transactionAuthor`](cnsaverequest/transactionauthor.md) to suppress processing changes that you already know about.

## See Also

- [var additionalContactKeyDescriptors: [any CNKeyDescriptor]?](cnchangehistoryfetchrequest/additionalcontactkeydescriptors.md)
  An array of contact property keys or key descriptors from contact objects to fetch in the returned contacts.
- [var includeGroupChanges: Bool](cnchangehistoryfetchrequest/includegroupchanges.md)
  A Boolean value that indicates whether the fetch should also return group changes.
- [var mutableObjects: Bool](cnchangehistoryfetchrequest/mutableobjects.md)
  A Boolean value that indicates whether the fetch should return mutable contacts and groups.
- [var shouldUnifyResults: Bool](cnchangehistoryfetchrequest/shouldunifyresults.md)
  A Boolean value that indicates whether the fetch should return contact changes as unified contacts.
- [var startingToken: Data?](cnchangehistoryfetchrequest/startingtoken.md)
  An opaque token that indicates a point in history in the user’s Contacts database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest/excludedtransactionauthors)*