# ABGroupCreateSearchElement(_:_:_:_:_:)

**Framework**: Address Book  
**Kind**: func

Creates an ABSearchElement object that specifies a queryfor ABGroup records.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABGroupCreateSearchElement(_ property: CFString!, _ label: CFString!, _ key: CFString!, _ value: CFTypeRef!, _ comparison: ABSearchComparison) -> Unmanaged<ABSearchElementRef>!
```

#### Return Value

A search element objectthat specifies a query according to the above parameters. You areresponsible for releasing this object.

#### Discussion

Use the ABAddressBook [`ABCopyArrayOfMatchingRecords(_:_:)`](abcopyarrayofmatchingrecords(_:_:).md) functionto actually perform the query. Also, see `ABSearchElement C` formore functions that create compound queries.

## Parameters

- `property`: The name of the property to search on. It cannot be  . For a full list of the properties, see   and Common Properties.
- `label`: The label name for a multi-value list. If   does not have multiple values, pass  . If   does have multiple values, pass   to search all the values. By default, ABGroup records don’t contain any multi-value list properties.
- `key`: The key name for a dictionary. If   is not a dictionary, pass  . If   is a dictionary, pass   to search all keys. By default, ABGroup records don’t contain any properties that are dictionaries.
- `value`: The value you are searching for. It cannot be 
- `comparison`: Specifies the type of comparison to perform, such as   or  . For a full list, see  .

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
- [func ABGroupRemoveGroup(ABGroupRef!, ABGroupRef!) -> Bool](abgroupremovegroup(_:_:).md)
  Removes a subgroup from a group.
- [func ABGroupRemoveMember(ABRecord!, ABRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abgroupremovemember(_:_:).md)
  Removes a person from a group.
- [func ABGroupSetDistributionIdentifier(ABGroupRef!, ABPersonRef!, CFString!, CFString!) -> Bool](abgroupsetdistributionidentifier(_:_:_:_:).md)
  Assigning a specific distribution identifier for a person’smulti-value list property so that the group can be used as a distributionlist (mailing list, in the case of an email property).


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abgroupcreatesearchelement(_:_:_:_:_:))*