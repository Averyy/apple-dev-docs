# add(_:toContainerWithIdentifier:)

**Framework**: Contacts  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addGroup:(CNMutableGroup *) group toContainerWithIdentifier:(NSString *) identifier;
```

#### Discussion

This method overrides any previously made delete request for the group.

## Parameters

- `group`: The group to add.
- `identifier`: The identifier of the container to add the new group. To add the new group to the default container, set `identifier` to `nil`.

## See Also

### Saving group changes
- [func update(CNMutableGroup)](./update%28_%29-8h6f6.md)
  Updates an existing group in the contact store.
- [func delete(CNMutableGroup)](./delete%28_%29-29lsm.md)
  Deletes a group from the contact store.
- [func addMember(CNContact, to: CNGroup)](./addmember%28_,to%29.md)
  Adds a contact as a member of a group.
- [func removeMember(CNContact, from: CNGroup)](./removemember%28_,from%29.md)
  Removes a contact as a member of a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsaverequest/add(_:tocontainerwithidentifier:)-4ikaa)*