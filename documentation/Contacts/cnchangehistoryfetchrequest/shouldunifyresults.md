# shouldUnifyResults

**Framework**: Contacts  
**Kind**: property

A Boolean value that indicates whether the fetch should return contact changes as unified contacts.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var shouldUnifyResults: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the fetch returns unified contact history. Otherwise the system returns individual contact history. A unified contact is the aggregation of properties from a set of linked individual contacts. If an individual contact is not linked then the unified contact is simply that individual contact.

## See Also

- [var additionalContactKeyDescriptors: [any CNKeyDescriptor]?](cnchangehistoryfetchrequest/additionalcontactkeydescriptors.md)
  An array of contact property keys or key descriptors from contact objects to fetch in the returned contacts.
- [var excludedTransactionAuthors: [String]?](cnchangehistoryfetchrequest/excludedtransactionauthors.md)
  An array of strings that identify transaction authors to exclude from the fetch results.
- [var includeGroupChanges: Bool](cnchangehistoryfetchrequest/includegroupchanges.md)
  A Boolean value that indicates whether the fetch should also return group changes.
- [var mutableObjects: Bool](cnchangehistoryfetchrequest/mutableobjects.md)
  A Boolean value that indicates whether the fetch should return mutable contacts and groups.
- [var startingToken: Data?](cnchangehistoryfetchrequest/startingtoken.md)
  An opaque token that indicates a point in history in the user’s Contacts database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest/shouldunifyresults)*