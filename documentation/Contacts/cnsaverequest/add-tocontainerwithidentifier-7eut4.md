# add(_:toContainerWithIdentifier:)

**Framework**: Contacts  
**Kind**: method

Adds the specified contact to the contact store.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func add(_ contact: CNMutableContact, toContainerWithIdentifier identifier: String?)
```

#### Discussion

This method overrides any previously made deletion requests for the contact. The new contact may be modified by executing the save request.

## Parameters

- `contact`: The new contact to add.
- `identifier`: The identifier of the container to add the new contact. To add the new contact to the default container set   to  .

## See Also

- [func update(CNMutableContact)](cnsaverequest/update(_:)-3gaig.md)
  Updates an existing contact in the contact store.
- [func delete(CNMutableContact)](cnsaverequest/delete(_:)-8m1tc.md)
  Deletes a contact from the contact store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsaverequest/add(_:tocontainerwithidentifier:)-7eut4)*