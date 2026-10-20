# ABGroupRemoveMember(_:_:_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Removes a person from a group.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS

> **Deprecated**: use [CNSaveRequest removeMember:fromGroup:]

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
func ABGroupRemoveMember(_ group: ABRecord!, _ member: ABRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

*macOS*

```swift
func ABGroupRemoveMember(_ group: ABGroupRef!, _ personToRemove: ABPersonRef!) -> Bool
```

*iOS, iPadOS, Mac Catalyst*

```c
extern bool ABGroupRemoveMember(ABRecordRef group, ABRecordRef member, CFErrorRef*error);
```

*macOS*

```c
extern bool ABGroupRemoveMember(ABGroupRef group, ABPersonRef personToRemove);
```

#### Return Value

`true` ifsuccessful. If the `person` parameteris not in `group`, this function does nothingand returns `false`.

## Parameters

- `group`: The group that you wish to remove `person` from.
- `member`: The person that you wish to remove from group.
- `personToRemove`: The member that you wish to remove from `group`.

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
- [func ABGroupCopyArrayOfAllSubgroups(ABGroupRef!) -> Unmanaged<CFArray>!](./abgroupcopyarrayofallsubgroups%28_%29.md)
  Returns an array containing a group’s subgroups.
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
- [func ABGroupSetDistributionIdentifier(ABGroupRef!, ABPersonRef!, CFString!, CFString!) -> Bool](./abgroupsetdistributionidentifier%28_,_,_,_%29.md)
  Assigning a specific distribution identifier for a person’smulti-value list property so that the group can be used as a distributionlist (mailing list, in the case of an email property).


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroupremovemember(_:_:_:))*