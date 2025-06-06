# CNSaveRequest

**Framework**: Contacts  
**Kind**: class

An object that collects the changes you want to save to the user’s contacts database.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class CNSaveRequest
```

#### Overview

Create a new `CNSaveRequest` object for each save operation you want to make. You can batch multiple changes into one save request (note that these changes only apply to objects). In the case of overlapping changes in multiple or concurrent save requests, the last change wins.

If you try to add an object (that is, a contact or a group) that already exists in the contact store, you receive the [`CNError.Code.insertedRecordAlreadyExists`](cnerror/code/insertedrecordalreadyexists.md) error and the [`CNErrorUserInfoAffectedRecordsKey`](cnerroruserinfoaffectedrecordskey.md) array is updated to contain the object you tried to add. If you try to update or delete an object that is not present in the contact store, the save request does not perform the update or deletion, the [`CNError.Code.recordDoesNotExist`](cnerror/code/recorddoesnotexist.md) error occurs, and the [`CNErrorUserInfoAffectedRecordsKey`](cnerroruserinfoaffectedrecordskey.md) array is updated to contain the object you tried to update or delete. Do not access objects in the save request while that request is executing.

## Topics

### Saving contact changes
- [func add(CNMutableContact, toContainerWithIdentifier: String?)](cnsaverequest/add(_:tocontainerwithidentifier:)-7eut4.md)
  Adds the specified contact to the contact store.
- [func update(CNMutableContact)](cnsaverequest/update(_:)-3gaig.md)
  Updates an existing contact in the contact store.
- [func delete(CNMutableContact)](cnsaverequest/delete(_:)-8m1tc.md)
  Deletes a contact from the contact store.
### Saving group changes
- [func add(CNMutableGroup, toContainerWithIdentifier: String?)](cnsaverequest/add(_:tocontainerwithidentifier:)-4ikaa.md)
  Adds a group to the contact store.
- [func update(CNMutableGroup)](cnsaverequest/update(_:)-8h6f6.md)
  Updates an existing group in the contact store.
- [func delete(CNMutableGroup)](cnsaverequest/delete(_:)-29lsm.md)
  Deletes a group from the contact store.
- [func addMember(CNContact, to: CNGroup)](cnsaverequest/addmember(_:to:).md)
  Adds a contact as a member of a group.
- [func removeMember(CNContact, from: CNGroup)](cnsaverequest/removemember(_:from:).md)
  Removes a contact as a member of a group.
### Adding and removing subgroups
- [func addSubgroup(CNGroup, to: CNGroup)](cnsaverequest/addsubgroup(_:to:).md)
  Add the specified group to a parent group.
- [func removeSubgroup(CNGroup, from: CNGroup)](cnsaverequest/removesubgroup(_:from:).md)
  Remove a subgroup from the specified parent group.
### Configuring the save request
- [var shouldRefetchContacts: Bool](cnsaverequest/shouldrefetchcontacts.md)
  A Boolean value that indicates whether to refetch the added and updated contacts after the save request executes.
- [var transactionAuthor: String?](cnsaverequest/transactionauthor.md)
  A string that identifies the author of the transaction.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CNContactFetchRequest](cncontactfetchrequest.md)
  An object that defines the options to use when fetching contacts.
- [class CNFetchRequest](cnfetchrequest.md)
  The base class for contact fetch requests.
- [class CNFetchResult](cnfetchresult.md)
  An object that represents the result of a change-history fetch request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsaverequest)*