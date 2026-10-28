# addMember(_:to:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

Adds a contact as a member of a group.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func addMember(_ contact: CNContact, to group: CNGroup)
```

```objc
- (void) addMember:(CNContact *) contact toGroup:(CNGroup *) group;
```

## Discussion

This method overrides any previously made remove membership request on the contact from the group.

## Parameters

- `contact`: The contact to add to the group membership.
- `group`: The group to add the contact to its membership.

## See Also

### Saving group changes
- [func add(CNMutableGroup, toContainerWithIdentifier: String?)](./add%28_,tocontainerwithidentifier%29-4ikaa.md)
  Adds a group to the contact store.
- [func update(CNMutableGroup)](./update%28_%29-8h6f6.md)
  Updates an existing group in the contact store.
- [func delete(CNMutableGroup)](./delete%28_%29-29lsm.md)
  Deletes a group from the contact store.
- [func removeMember(CNContact, from: CNGroup)](./removemember%28_,from%29.md)
  Removes a contact as a member of a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsaverequest/addmember(_:to:))*