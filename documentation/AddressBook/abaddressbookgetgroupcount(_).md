# ABAddressBookGetGroupCount(_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Returns the number of groups in an address book.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: use count of fetch results for [CNContactStore groupsMatchingPredicate:nil error:]

## Declaration

```swift
func ABAddressBookGetGroupCount(_ addressBook: ABAddressBook!) -> CFIndex
```

```c
extern CFIndex ABAddressBookGetGroupCount(ABAddressBookRef addressBook);
```

#### Return Value

The number of groups in `addressBook`.

## Parameters

- `addressBook`: The address book whose record count is being returned.

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
- [func ABAddressBookGetGroupWithRecordID(ABAddressBook!, ABRecordID) -> Unmanaged<ABRecord>!](./abaddressbookgetgroupwithrecordid%28_,_%29.md)
  Returns the group with a given record ID.
- [func ABAddressBookGetPersonCount(ABAddressBook!) -> CFIndex](./abaddressbookgetpersoncount%28_%29.md)
  Returns the number of person records in an address book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbookgetgroupcount(_:))*