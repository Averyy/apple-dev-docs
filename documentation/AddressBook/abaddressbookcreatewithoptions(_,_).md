# ABAddressBookCreateWithOptions(_:_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Creates a new address book object with data from the Address Book database.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: use [[CNContactStore alloc] init]

## Declaration

```swift
func ABAddressBookCreateWithOptions(_ options: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ABAddressBook>!
```

```c
extern ABAddressBookRefABAddressBookCreateWithOptions(CFDictionaryRef options, CFErrorRef*error);
```

#### Return Value

An address book object, `NULL`, or an empty database.

#### Discussion

Changes made to the returned address book are reflected in the Address Book database only after saving the address book with [`ABAddressBookSave(_:_:)`](./abaddressbooksave%28_,_%29.md).

On iOS 6.0 and later, if the caller does not have access to the Address Book database:

- For apps linked against iOS 6.0 and later, this function returns `NULL`.
- For apps linked against previous version of iOS, this function returns an empty read-only database.

If your app syncs information with the database, it must not sync data when it does not have access to the database.

> ❗ **Important**:  You must ensure that an instance of `ABAddressBookRef` is used by only one thread.

## Parameters

- `options`: Reserved. Pass `NULL`.
- `error`: On error, contains error information. See [Address Book Errors](./address-book-errors.md).

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
- [func ABAddressBookGetAuthorizationStatus() -> ABAuthorizationStatus](./abaddressbookgetauthorizationstatus%28%29.md)
  Returns the authorization status of your app for accessing address book data.
- [func ABAddressBookGetGroupCount(ABAddressBook!) -> CFIndex](./abaddressbookgetgroupcount%28_%29.md)
  Returns the number of groups in an address book.
- [func ABAddressBookGetGroupWithRecordID(ABAddressBook!, ABRecordID) -> Unmanaged<ABRecord>!](./abaddressbookgetgroupwithrecordid%28_,_%29.md)
  Returns the group with a given record ID.
- [func ABAddressBookGetPersonCount(ABAddressBook!) -> CFIndex](./abaddressbookgetpersoncount%28_%29.md)
  Returns the number of person records in an address book.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbookcreatewithoptions(_:_:))*