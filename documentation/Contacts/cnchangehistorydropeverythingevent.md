# CNChangeHistoryDropEverythingEvent

**Framework**: Contacts  
**Kind**: class

An object that indicates the delegate should drop all contacts and groups before handling change events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class CNChangeHistoryDropEverythingEvent
```

#### Overview

The system sends this event to your delegate when the system determines that enough has changed since the last time your app fetched the history changes that an incremental update is no longer possible. Following the drop-everything event, your app receives an add event for each contact and group currently in the database. This allows you to implement full syncs and incremental syncs using the same code.

## Relationships

### Inherits From
- [CNChangeHistoryEvent](cnchangehistoryevent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
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
- [class CNChangeHistoryEvent](cnchangehistoryevent.md)
  An object that represents the user adding, updating, or deleting a contact or group.
- [class CNChangeHistoryFetchRequest](cnchangehistoryfetchrequest.md)
  An object that specifies the criteria for fetching change history.
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

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistorydropeverythingevent)*