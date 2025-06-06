# CNChangeHistoryEventVisitor

**Framework**: Contacts  
**Kind**: protocol

An interface for receiving notice of changes to contacts and groups.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol CNChangeHistoryEventVisitor : NSObjectProtocol
```

#### Overview

Implement this protocol to receive events that describe when a user adds, updates, or deletes contacts or groups outside your app.

## Topics

### Updating contacts
- [func visit(CNChangeHistoryAddContactEvent)](cnchangehistoryeventvisitor/visit(_:)-9w73y.md)
  Tells the delegate that the user added a contact.
- [func visit(CNChangeHistoryUpdateContactEvent)](cnchangehistoryeventvisitor/visit(_:)-1pf2a.md)
  Tells the delegate that the user updated a contact.
- [func visit(CNChangeHistoryDeleteContactEvent)](cnchangehistoryeventvisitor/visit(_:)-ci4z.md)
  Tells the delegate that the user deleted a contact.
### Updating groups
- [func visit(CNChangeHistoryAddGroupEvent)](cnchangehistoryeventvisitor/visit(_:)-ve62.md)
  Tells the delegate that the user added a group.
- [func visit(CNChangeHistoryUpdateGroupEvent)](cnchangehistoryeventvisitor/visit(_:)-23p9h.md)
  Tells the delegate that the user updated a group.
- [func visit(CNChangeHistoryDeleteGroupEvent)](cnchangehistoryeventvisitor/visit(_:)-82duo.md)
  Tells the delegate that the user deleted a group.
### Updating subgroups
- [func visitAddSubgroup(CNChangeHistoryAddSubgroupToGroupEvent)](cnchangehistoryeventvisitor/visitaddsubgroup(_:).md)
  Tells the delegate that the user added a subgroup to a group.
- [func visitRemoveSubgroup(CNChangeHistoryRemoveSubgroupFromGroupEvent)](cnchangehistoryeventvisitor/visitremovesubgroup(_:).md)
  Tells the delegate that the user removed a subgroup from a group.
### Updating contacts in groups
- [func visitAddMember(CNChangeHistoryAddMemberToGroupEvent)](cnchangehistoryeventvisitor/visitaddmember(_:).md)
  Tells the delegate that the user added a contact to a group.
- [func visitRemoveMember(CNChangeHistoryRemoveMemberFromGroupEvent)](cnchangehistoryeventvisitor/visitremovemember(_:).md)
  Tells the delegate that the user removed a contact from a group.
### Resetting synced data
- [func visit(CNChangeHistoryDropEverythingEvent)](cnchangehistoryeventvisitor/visit(_:)-2yhz3.md)
  Tells the delegate to drop all contacts and groups before handling more events.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnchangehistoryeventvisitor)*