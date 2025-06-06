# update(_:)

**Framework**: Contacts  
**Kind**: method

Updates an existing contact in the contact store.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func update(_ contact: CNMutableContact)
```

#### Discussion

The contact to be updated must already exist in the contact store. If it does not, the update request fails, the `CNErrorCodeRecordDoesNotExist` error occurs, and the `CNErrorUserInfoAffectedRecordsKey` array is updated to contain the object. Note that the contact may be modified when the save request is executing.

## Parameters

- `contact`: The contact to update.

## See Also

- [func add(CNMutableContact, toContainerWithIdentifier: String?)](cnsaverequest/add(_:tocontainerwithidentifier:)-7eut4.md)
  Adds the specified contact to the contact store.
- [func delete(CNMutableContact)](cnsaverequest/delete(_:)-8m1tc.md)
  Deletes a contact from the contact store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsaverequest/update(_:)-3gaig)*