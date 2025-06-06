# CNChangeHistoryFetchRequest

**Framework**: Contacts  
**Kind**: class

An object that specifies the criteria for fetching change history.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class CNChangeHistoryFetchRequest
```

#### Overview

The system always returns changes to contacts. The system coalesces changes to remove redundant adds, updates, and deletes.

Create and configure a fetch request, then call [`enumeratorForChangeHistoryFetchRequest:error:`](cncontactstore/enumeratorforchangehistoryfetchrequest:error:.md) to process changes.

## Topics

### Configuring the fetch request
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
- [var startingToken: Data?](cnchangehistoryfetchrequest/startingtoken.md)
  An opaque token that indicates a point in history in the user’s Contacts database.

## Relationships

### Inherits From
- [CNFetchRequest](cnfetchrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class CNChangeHistoryAddContactEvent](cnchangehistoryaddcontactevent.md)
  An object that represents a user adding a contact.
- [class CNChangeHistoryAddGroupEvent](cnchangehistoryaddgroupevent.md)
  An object that represents a user adding a group.
- [class CNChangeHistoryAddMemberToGroupEvent](cnchangehistoryaddmembertogroupevent.md)
  An object that represents a user adding a contact to a group.
- [class CNChangeHistoryAddSubgroupToGroupEvent](cnchangehistoryaddsubgrouptogroupevent.md)
  An object that represents a user adding a subgroup to a group.
- [class CNChangeHistoryDeleteContactEvent](cnchangehistorydeletecontactevent.md)
  An object that represents a user deleting a contact.
- [class CNChangeHistoryDeleteGroupEvent](cnchangehistorydeletegroupevent.md)
  An object that represents a user deleting a group.
- [class CNChangeHistoryDropEverythingEvent](cnchangehistorydropeverythingevent.md)
  An object that indicates the delegate should drop all contacts and groups before handling change events.
- [class CNChangeHistoryEvent](cnchangehistoryevent.md)
  An object that represents the user adding, updating, or deleting a contact or group.
- [class CNChangeHistoryRemoveMemberFromGroupEvent](cnchangehistoryremovememberfromgroupevent.md)
  An object that represents a user removing a contact from a group.
- [class CNChangeHistoryRemoveSubgroupFromGroupEvent](cnchangehistoryremovesubgroupfromgroupevent.md)
  An object that represents a user removing a subgroup from a group.
- [class CNChangeHistoryUpdateContactEvent](cnchangehistoryupdatecontactevent.md)
  An object that represents a user updating a contact.
- [class CNChangeHistoryUpdateGroupEvent](cnchangehistoryupdategroupevent.md)
  An object that represents an updated group event.
- [protocol CNChangeHistoryEventVisitor](cnchangehistoryeventvisitor.md)
  An interface for receiving notice of changes to contacts and groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistoryfetchrequest)*