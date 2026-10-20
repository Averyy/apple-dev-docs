# ABGroupCopyArrayOfAllSubgroups(_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Returns an array containing a group’s subgroups.

**Availability**:
- macOS

## Declaration

```swift
func ABGroupCopyArrayOfAllSubgroups(_ group: ABGroupRef!) -> Unmanaged<CFArray>!
```

```c
extern CFArrayRefABGroupCopyArrayOfAllSubgroups(ABGroupRef group);
```

#### Return Value

An array of ABGroupobjects representing the subgroups of `group`.If `group` doesn’t contain any groups,this function returns an empty array. You are responsible for releasingthis object.

## Parameters

- `group`: The ABGroup object whose subgroups you wish to obtain.

## See Also

### Groups
- [func ABCopyArrayOfAllGroups(ABAddressBookRef!) -> Unmanaged<CFArray>!](./abcopyarrayofallgroups%28_%29.md)
  Returns an array of all the groups in the Address Book database.
- [func ABGroupAddGroup(ABGroupRef!, ABGroupRef!) -> Bool](./abgroupaddgroup%28_,_%29.md)
  Adds a subgroup to another group.
- [func ABGroupAddMember(ABRecord!, ABRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./abgroupaddmember%28_,_,_%29.md)
  Adds a person to a group.
- [func ABGroupCopyArrayOfAllMembers(ABRecord!) -> Unmanaged<CFArray>!](./abgroupcopyarrayofallmembers%28_%29.md)
  Returns an array of persons in a group.
- [func ABGroupCopyDistributionIdentifier(ABGroupRef!, ABPersonRef!, CFString!) -> Unmanaged<CFString>!](./abgroupcopydistributionidentifier%28_,_,_%29.md)
  Returns the distribution identifier for the given propertyand person.
- [func ABGroupCopyParentGroups(ABGroupRef!) -> Unmanaged<CFArray>!](./abgroupcopyparentgroups%28_%29.md)
  Returns an array containing a group’s parents—thegroups that a group belongs to.
- [func ABGroupCreate() -> Unmanaged<ABRecord>!](./abgroupcreate%28%29.md)
  Returns a new ABGroup object.
- [func ABGroupCreateSearchElement(CFString!, CFString!, CFString!, CFTypeRef!, ABSearchComparison) -> Unmanaged<ABSearchElementRef>!](./abgroupcreatesearchelement%28_,_,_,_,_%29.md)
  Creates an ABSearchElement object that specifies a queryfor ABGroup records.
- [func ABGroupRemoveGroup(ABGroupRef!, ABGroupRef!) -> Bool](./abgroupremovegroup%28_,_%29.md)
  Removes a subgroup from a group.
- [func ABGroupRemoveMember(ABRecord!, ABRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./abgroupremovemember%28_,_,_%29.md)
  Removes a person from a group.
- [func ABGroupSetDistributionIdentifier(ABGroupRef!, ABPersonRef!, CFString!, CFString!) -> Bool](./abgroupsetdistributionidentifier%28_,_,_,_%29.md)
  Assigning a specific distribution identifier for a person’smulti-value list property so that the group can be used as a distributionlist (mailing list, in the case of an email property).


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroupcopyarrayofallsubgroups(_:))*