# ABGroupSetDistributionIdentifier(_:_:_:_:)

**Framework**: Address Book  
**Kind**: func

Assigning a specific distribution identifier for a person’smulti-value list property so that the group can be used as a distributionlist (mailing list, in the case of an email property).

**Availability**:
- macOS ?+

## Declaration

```swift
func ABGroupSetDistributionIdentifier(_ group: ABGroupRef!, _ person: ABPersonRef!, _ property: CFString!, _ identifier: CFString!) -> Bool
```

#### Return Value

`true` ifsuccessful, `false` otherwise.

#### Discussion

The default distribution identifier is a multi-value list’sprimary identifier. Use this function if you need to change thedistribution identifier for a particular person. For example, ifthe default identifier is a person’s home email but you want touse John’s work email, invoke this function passing kABEmailWorkLabel asthe `identifier` parameter, kABEmailProperty asthe `property` parameter, and John’sperson object as the `person` parameter.

## Parameters

- `group`: The group that   belongs to.
- `person`: The person whose distribution identifier for   you wish to change. If  , this function raises an exception.
- `property`: The multi-value list property whose distribution identifier you wish to change.
- `identifier`: The new distribution identifier, a label used by a multi-value list such as kABAddressHomeLabel for a kABAddressProperty. Pass   to reset the distribution identifier to its default, a multi-value list’s primary identifier.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroupsetdistributionidentifier(_:_:_:_:))*