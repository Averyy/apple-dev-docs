# ABGroupAddMember(_:_:_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Adds a person to a group.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS

> **Deprecated**: use [CNSaveRequest addMember:toGroup:]

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
func ABGroupAddMember(_ group: ABRecord!, _ person: ABRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

*macOS*

```swift
func ABGroupAddMember(_ group: ABGroupRef!, _ personToAdd: ABPersonRef!) -> Bool
```

*iOS, iPadOS, Mac Catalyst*

```c
extern bool ABGroupAddMember(ABRecordRef group, ABRecordRef person, CFErrorRef*error);
```

*macOS*

```c
extern bool ABGroupAddMember(ABGroupRef group, ABPersonRef personToAdd);
```

## Return Value

`true` ifsuccessful, false otherwise. For example, if `person` isalready in `group`, this function doesnothing but returns `false`.

## Parameters

- `group`: The group you wish to add `person` to.
- `person`: The person to add to `group`. If `person` is `NULL`, this function raises an exception.
- `personToAdd`: The person to add to `group`. If `person` is `NULL`, this function raises an exception.

## See Also

### Groups
- [func ABCopyArrayOfAllGroups(ABAddressBookRef!) -> Unmanaged<CFArray>!](./abcopyarrayofallgroups%28_%29.md)
  Returns an array of all the groups in the Address Book database.
- [func ABGroupAddGroup(ABGroupRef!, ABGroupRef!) -> Bool](./abgroupaddgroup%28_,_%29.md)
  Adds a subgroup to another group.
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
- [func ABGroupRemoveMember(ABRecord!, ABRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./abgroupremovemember%28_,_,_%29.md)
  Removes a person from a group.
- [func ABGroupSetDistributionIdentifier(ABGroupRef!, ABPersonRef!, CFString!, CFString!) -> Bool](./abgroupsetdistributionidentifier%28_,_,_,_%29.md)
  Assigning a specific distribution identifier for a person’smulti-value list property so that the group can be used as a distributionlist (mailing list, in the case of an email property).


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroupaddmember(_:_:_:))*