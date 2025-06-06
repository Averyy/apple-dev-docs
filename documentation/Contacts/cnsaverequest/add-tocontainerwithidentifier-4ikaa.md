# add(_:toContainerWithIdentifier:)

**Framework**: Contacts  
**Kind**: method

Adds a group to the contact store.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func add(_ group: CNMutableGroup, toContainerWithIdentifier identifier: String?)
```

#### Discussion

This method overrides any previously made delete request for the group.

## Parameters

- `group`: The group to add.
- `identifier`: The identifier of the container to add the new group. To add the new group to the default container, set   to  .

## See Also

- [func update(CNMutableGroup)](cnsaverequest/update(_:)-8h6f6.md)
  Updates an existing group in the contact store.
- [func delete(CNMutableGroup)](cnsaverequest/delete(_:)-29lsm.md)
  Deletes a group from the contact store.
- [func addMember(CNContact, to: CNGroup)](cnsaverequest/addmember(_:to:).md)
  Adds a contact as a member of a group.
- [func removeMember(CNContact, from: CNGroup)](cnsaverequest/removemember(_:from:).md)
  Removes a contact as a member of a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsaverequest/add(_:tocontainerwithidentifier:)-4ikaa)*