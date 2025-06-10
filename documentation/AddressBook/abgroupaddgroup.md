# ABGroupAddGroup(_:_:)

**Framework**: Address Book  
**Kind**: func

Adds a subgroup to another group.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABGroupAddGroup(_ group: ABGroupRef!, _ groupToAdd: ABGroupRef!) -> Bool
```

#### Return Value

Returns `true` ifsuccessful. If the `group` argumentis already part of the receiver, this function does nothing andreturns `false`. If adding the group wouldcreate a recursion, this function also does nothing and returns `false`. Forexample, if the group “Animal Lovers” is in “Dog Lovers,“and you add “Dog Lovers” to “Animal Lovers,” that wouldcreate a recursion, which this function won’t allow.

## Parameters

- `group`: The group you wish to add a subgroup to. If  , this function raises an exception.
- `groupToAdd`: The subgroup you wish to add to  .

## See Also

- [func ABCopyArrayOfAllGroups(ABAddressBookRef!) -> Unmanaged<CFArray>!](abcopyarrayofallgroups(_:).md)
  Returns an array of all the groups in the Address Book database.
- [func ABGroupAddMember(ABRecord!, ABRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abgroupaddmember(_:_:).md)
  Adds a person to a group.
- [func ABGroupCopyArrayOfAllMembers(ABRecord!) -> Unmanaged<CFArray>!](abgroupcopyarrayofallmembers(_:).md)
  Returns an array of persons in a group.
- [func ABGroupCopyArrayOfAllSubgroups(ABGroupRef!) -> Unmanaged<CFArray>!](abgroupcopyarrayofallsubgroups(_:).md)
  Returns an array containing a group’s subgroups.
- [func ABGroupCopyDistributionIdentifier(ABGroupRef!, ABPersonRef!, CFString!) -> Unmanaged<CFString>!](abgroupcopydistributionidentifier(_:_:_:).md)
  Returns the distribution identifier for the given propertyand person.
- [func ABGroupCopyParentGroups(ABGroupRef!) -> Unmanaged<CFArray>!](abgroupcopyparentgroups(_:).md)
  Returns an array containing a group’s parents—thegroups that a group belongs to.
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

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroupaddgroup(_:_:))*