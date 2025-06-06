# removeMember(_:from:)

**Framework**: Contacts  
**Kind**: method

Removes a contact as a member of a group.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func removeMember(_ contact: CNContact, from group: CNGroup)
```

#### Discussion

This method removes the contact from the group, but does not delete it from the contact store. This method overrides any previously made add membership request on the contact to the group.

## Parameters

- `contact`: The contact to remove from the group membership.
- `group`: The group to remove the contact from its membership.

## See Also

- [func add(CNMutableGroup, toContainerWithIdentifier: String?)](cnsaverequest/add(_:tocontainerwithidentifier:)-4ikaa.md)
  Adds a group to the contact store.
- [func update(CNMutableGroup)](cnsaverequest/update(_:)-8h6f6.md)
  Updates an existing group in the contact store.
- [func delete(CNMutableGroup)](cnsaverequest/delete(_:)-29lsm.md)
  Deletes a group from the contact store.
- [func addMember(CNContact, to: CNGroup)](cnsaverequest/addmember(_:to:).md)
  Adds a contact as a member of a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsaverequest/removemember(_:from:))*