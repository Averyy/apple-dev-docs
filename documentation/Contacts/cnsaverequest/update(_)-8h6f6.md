# update(_:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

Updates an existing group in the contact store.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func update(_ group: CNMutableGroup)
```

```objc
- (void) updateGroup:(CNMutableGroup *) group;
```

#### Discussion

The group to be updated must already exist in the contact store. If it does not, the update request fails, the `CNErrorCodeRecordDoesNotExist` error is thrown, and the `CNErrorUserInfoAffectedRecordsKey` array is updated to contain that object.

## Parameters

- `group`: The group to update.

## See Also

### Saving group changes
- [func add(CNMutableGroup, toContainerWithIdentifier: String?)](./add%28_,tocontainerwithidentifier%29-4ikaa.md)
  Adds a group to the contact store.
- [func delete(CNMutableGroup)](./delete%28_%29-29lsm.md)
  Deletes a group from the contact store.
- [func addMember(CNContact, to: CNGroup)](./addmember%28_,to%29.md)
  Adds a contact as a member of a group.
- [func removeMember(CNContact, from: CNGroup)](./removemember%28_,from%29.md)
  Removes a contact as a member of a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsaverequest/update(_:)-8h6f6)*