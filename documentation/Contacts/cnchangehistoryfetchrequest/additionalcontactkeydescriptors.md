# additionalContactKeyDescriptors

**Framework**: Contacts  
**Kind**: property

An array of contact property keys or key descriptors from contact objects to fetch in the returned contacts.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var additionalContactKeyDescriptors: [any CNKeyDescriptor]? { get set }
```

#### Discussion

By default, the system only fetches [`CNContactIdentifierKey`](cncontactidentifierkey.md) if you do not include a list of additional key descriptors. The system always fetches [`CNContactIdentifierKey`](cncontactidentifierkey.md), whether you request it or not.

For a list of possible keys, see [`Contact Keys`](contact-keys.md).

## See Also

- [var excludedTransactionAuthors: [String]?](cnchangehistoryfetchrequest/excludedtransactionauthors.md)
  An array of strings that identify transaction authors to exclude from the fetch results.
- [var includeGroupChanges: Bool](cnchangehistoryfetchrequest/includegroupchanges.md)
  A Boolean value that indicates whether the fetch should also return group changes.
- [var mutableObjects: Bool](cnchangehistoryfetchrequest/mutableobjects.md)
  A Boolean value that indicates whether the fetch should return mutable contacts and groups.
- [var shouldUnifyResults: Bool](cnchangehistoryfetchrequest/shouldunifyresults.md)
  A Boolean value that indicates whether the fetch should return contact changes as unified contacts.
- [var startingToken: Data?](cnchangehistoryfetchrequest/startingtoken.md)
  An opaque token that indicates a point in history in the user’s Contacts database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest/additionalcontactkeydescriptors)*