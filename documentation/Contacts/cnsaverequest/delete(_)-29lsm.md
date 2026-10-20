# delete(_:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

Deletes a group from the contact store.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func delete(_ group: CNMutableGroup)
```

```objc
- (void) deleteGroup:(CNMutableGroup *) group;
```

#### Discussion

This method overrides any previously made add request on the group. The group to be deleted must already exist in the contact store. If it does not, the delete request fails, the `CNErrorCodeRecordDoesNotExist` error is thrown, and the `CNErrorUserInfoAffectedRecordsKey` array is updated to contain that object.

## Parameters

- `group`: The group to delete.

## See Also

### Saving group changes
- [func add(CNMutableGroup, toContainerWithIdentifier: String?)](./add%28_,tocontainerwithidentifier%29-4ikaa.md)
  Adds a group to the contact store.
- [func update(CNMutableGroup)](./update%28_%29-8h6f6.md)
  Updates an existing group in the contact store.
- [func addMember(CNContact, to: CNGroup)](./addmember%28_,to%29.md)
  Adds a contact as a member of a group.
- [func removeMember(CNContact, from: CNGroup)](./removemember%28_,from%29.md)
  Removes a contact as a member of a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsaverequest/delete(_:)-29lsm)*