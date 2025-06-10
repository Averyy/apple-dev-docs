# ABGroupCopyParentGroups(_:)

**Framework**: Address Book  
**Kind**: func

Returns an array containing a group’s parents—thegroups that a group belongs to.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABGroupCopyParentGroups(_ group: ABGroupRef!) -> Unmanaged<CFArray>!
```

#### Return Value

An array containingABGroup objects representing the parents of `group`.If `group` doesn’t belong to anygroups, this function returns an empty array. You are responsiblefor releasing this object.

## Parameters

- `group`: The group whose parent groups you wish to obtain.

## See Also

- [func ABCopyArrayOfAllGroups(ABAddressBookRef!) -> Unmanaged<CFArray>!](abcopyarrayofallgroups(_:).md)
  Returns an array of all the groups in the Address Book database.
- [func ABGroupAddGroup(ABGroupRef!, ABGroupRef!) -> Bool](abgroupaddgroup(_:_:).md)
  Adds a subgroup to another group.
- [func ABGroupAddMember(ABRecord!, ABRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abgroupaddmember(_:_:).md)
  Adds a person to a group.
- [func ABGroupCopyArrayOfAllMembers(ABRecord!) -> Unmanaged<CFArray>!](abgroupcopyarrayofallmembers(_:).md)
  Returns an array of persons in a group.
- [func ABGroupCopyArrayOfAllSubgroups(ABGroupRef!) -> Unmanaged<CFArray>!](abgroupcopyarrayofallsubgroups(_:).md)
  Returns an array containing a group’s subgroups.
- [func ABGroupCopyDistributionIdentifier(ABGroupRef!, ABPersonRef!, CFString!) -> Unmanaged<CFString>!](abgroupcopydistributionidentifier(_:_:_:).md)
  Returns the distribution identifier for the given propertyand person.
- [func ABGroupCreate() -> Unmanaged<ABRecord>!](abgroupcreate().md)
  Returns a new ABGroup object.
- [func ABGroupCreateSearchElement(CFString!, CFString!, CFString!, CFTypeRef!, ABSearchComparison) -> Unmanaged<ABSearchElementRef>!](abgroupcreatesearchelement(_:_:_:_:_:).md)
  Creates an ABSearchElement object that specifies a queryfor ABGroup records.
- [func ABGroupRemoveGroup(ABGroupRef!, ABGroupRef!) -> Bool](abgroupremovegroup(_:_:).md)
  Removes a subgroup from a group.
- [func ABGroupRemoveMember(ABRecord!, ABRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abgroupremovemember(_:_:).md)
  Removes a person from a group.
- [func ABGroupSetDistributionIdentifier(ABGroupRef!, ABPersonRef!, CFString!, CFString!) -> Bool](abgroupsetdistributionidentifier(_:_:_:_:).md)
  Assigning a specific distribution identifier for a person’smulti-value list property so that the group can be used as a distributionlist (mailing list, in the case of an email property).


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroupcopyparentgroups(_:))*