# ABPersonComparePeopleByName(_:_:_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Indicates how two person records get sorted.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: use [CNContact comparatorForNameSortOrder:]

## Declaration

```swift
func ABPersonComparePeopleByName(_ person1: ABRecord!, _ person2: ABRecord!, _ ordering: ABPersonSortOrdering) -> CFComparisonResult
```

```c
extern CFComparisonResult ABPersonComparePeopleByName(ABRecordRef person1, ABRecordRef person2, ABPersonSortOrdering ordering);
```

## Return Value

- `kCFCompareLessThan` when `person1` goes before `person2`.

## Discussion

- `kCFCompareEqualTo` when `person1` and `person2` have the same name.
- `kCFCompareGreaterThan` when `person1` goes after `person2`.

## Parameters

- `person1`: The first person.
- `person2`: The second person.
- `ordering`: Indicates whether to sort by first name or by last name. See [Sort Order](./api-1619730-sort-order.md).

## See Also

### Deprecated
- [func ABAddressBookAddRecord(ABAddressBook!, ABRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./abaddressbookaddrecord%28_,_,_%29.md)
  Adds a record to an address book.
- [func ABAddressBookCopyArrayOfAllGroups(ABAddressBook!) -> Unmanaged<CFArray>!](./abaddressbookcopyarrayofallgroups%28_%29.md)
  Returns an array with all the groups in an address book.
- [func ABAddressBookCopyArrayOfAllGroupsInSource(ABAddressBook!, ABRecord!) -> Unmanaged<CFArray>!](./abaddressbookcopyarrayofallgroupsinsource%28_,_%29.md)
  Returns an array of all groups from a particular source.
- [func ABAddressBookCopyArrayOfAllPeople(ABAddressBook!) -> Unmanaged<CFArray>!](./abaddressbookcopyarrayofallpeople%28_%29.md)
  Returns all the person records in an address book.
- [func ABAddressBookCopyArrayOfAllPeopleInSource(ABAddressBook!, ABRecord!) -> Unmanaged<CFArray>!](./abaddressbookcopyarrayofallpeopleinsource%28_,_%29.md)
  Returns an array of all person records from a particular source.
- [func ABAddressBookCopyArrayOfAllPeopleInSourceWithSortOrdering(ABAddressBook!, ABRecord!, ABPersonSortOrdering) -> Unmanaged<CFArray>!](./abaddressbookcopyarrayofallpeopleinsourcewithsortordering%28_,_,_%29.md)
  Returns an array of all person records in the address book, sorted with the specified order.
- [func ABAddressBookCopyArrayOfAllSources(ABAddressBook!) -> Unmanaged<CFArray>!](./abaddressbookcopyarrayofallsources%28_%29.md)
  Returns an array of all sources in the address book.
- [func ABAddressBookCopyDefaultSource(ABAddressBook!) -> Unmanaged<ABRecord>!](./abaddressbookcopydefaultsource%28_%29.md)
  Returns the default source.
- [func ABAddressBookCopyLocalizedLabel(CFString!) -> Unmanaged<CFString>!](./abaddressbookcopylocalizedlabel%28_%29.md)
  Returns a localized version of a record-property label.
- [func ABAddressBookCopyPeopleWithName(ABAddressBook!, CFString!) -> Unmanaged<CFArray>!](./abaddressbookcopypeoplewithname%28_,_%29.md)
  Performs a prefix search on the composite names of people in an address book and returns an array of persons that match the search criteria.
- [func ABAddressBookCreate() -> Unmanaged<ABAddressBook>!](./abaddressbookcreate%28%29.md)
  Creates a new address book object with data from the Address Book database.
- [func ABAddressBookCreateWithOptions(CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ABAddressBook>!](./abaddressbookcreatewithoptions%28_,_%29.md)
  Creates a new address book object with data from the Address Book database.
- [func ABAddressBookGetAuthorizationStatus() -> ABAuthorizationStatus](./abaddressbookgetauthorizationstatus%28%29.md)
  Returns the authorization status of your app for accessing address book data.
- [func ABAddressBookGetGroupCount(ABAddressBook!) -> CFIndex](./abaddressbookgetgroupcount%28_%29.md)
  Returns the number of groups in an address book.
- [func ABAddressBookGetGroupWithRecordID(ABAddressBook!, ABRecordID) -> Unmanaged<ABRecord>!](./abaddressbookgetgroupwithrecordid%28_,_%29.md)
  Returns the group with a given record ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpersoncomparepeoplebyname(_:_:_:))*