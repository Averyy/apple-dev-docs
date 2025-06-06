# startingToken

**Framework**: Contacts  
**Kind**: property

An opaque token that indicates a point in history in the user’s Contacts database.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var startingToken: Data? { get set }
```

#### Discussion

Specify [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) to receive a [`CNChangeHistoryDropEverythingEvent`](cnchangehistorydropeverythingevent.md), followed by an add event for every contact and group in the Contacts database.

Save the [`currentHistoryToken`](cnfetchresult/currenthistorytoken.md) from a successful fetch result in your app, then specify it here to receive changes after that point in history.

## See Also

- [var additionalContactKeyDescriptors: [any CNKeyDescriptor]?](cnchangehistoryfetchrequest/additionalcontactkeydescriptors.md)
  An array of contact property keys or key descriptors from contact objects to fetch in the returned contacts.
- [var excludedTransactionAuthors: [String]?](cnchangehistoryfetchrequest/excludedtransactionauthors.md)
  An array of strings that identify transaction authors to exclude from the fetch results.
- [var includeGroupChanges: Bool](cnchangehistoryfetchrequest/includegroupchanges.md)
  A Boolean value that indicates whether the fetch should also return group changes.
- [var mutableObjects: Bool](cnchangehistoryfetchrequest/mutableobjects.md)
  A Boolean value that indicates whether the fetch should return mutable contacts and groups.
- [var shouldUnifyResults: Bool](cnchangehistoryfetchrequest/shouldunifyresults.md)
  A Boolean value that indicates whether the fetch should return contact changes as unified contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest/startingtoken)*