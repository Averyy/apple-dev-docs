# ABMultiValueGetCount(_:)

**Framework**: Address Book  
**Kind**: func

Returns the number of values in a multivalue property.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func ABMultiValueGetCount(_ multiValue: ABMultiValue!) -> CFIndex
```

#### Return Value

The number of values in `multiValue`.

## Parameters

- `multiValue`: The multivalue property whose value are being counted.

## See Also

- [func ABAddressBookAddRecord(ABAddressBook!, ABRecord!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abaddressbookaddrecord(_:_:_:).md)
  Adds a record to an address book.
- [func ABAddressBookCopyArrayOfAllGroups(ABAddressBook!) -> Unmanaged<CFArray>!](abaddressbookcopyarrayofallgroups(_:).md)
  Returns an array with all the groups in an address book.
- [func ABAddressBookCopyArrayOfAllGroupsInSource(ABAddressBook!, ABRecord!) -> Unmanaged<CFArray>!](abaddressbookcopyarrayofallgroupsinsource(_:_:).md)
  Returns an array of all groups from a particular source.
- [func ABAddressBookCopyArrayOfAllPeople(ABAddressBook!) -> Unmanaged<CFArray>!](abaddressbookcopyarrayofallpeople(_:).md)
  Returns all the person records in an address book.
- [func ABAddressBookCopyArrayOfAllPeopleInSource(ABAddressBook!, ABRecord!) -> Unmanaged<CFArray>!](abaddressbookcopyarrayofallpeopleinsource(_:_:).md)
  Returns an array of all person records from a particular source.
- [func ABAddressBookCopyArrayOfAllPeopleInSourceWithSortOrdering(ABAddressBook!, ABRecord!, ABPersonSortOrdering) -> Unmanaged<CFArray>!](abaddressbookcopyarrayofallpeopleinsourcewithsortordering(_:_:_:).md)
  Returns an array of all person records in the address book, sorted with the specified order.
- [func ABAddressBookCopyArrayOfAllSources(ABAddressBook!) -> Unmanaged<CFArray>!](abaddressbookcopyarrayofallsources(_:).md)
  Returns an array of all sources in the address book.
- [func ABAddressBookCopyDefaultSource(ABAddressBook!) -> Unmanaged<ABRecord>!](abaddressbookcopydefaultsource(_:).md)
  Returns the default source.
- [func ABAddressBookCopyLocalizedLabel(CFString!) -> Unmanaged<CFString>!](abaddressbookcopylocalizedlabel(_:).md)
  Returns a localized version of a record-property label.
- [func ABAddressBookCopyPeopleWithName(ABAddressBook!, CFString!) -> Unmanaged<CFArray>!](abaddressbookcopypeoplewithname(_:_:).md)
  Performs a prefix search on the composite names of people in an address book and returns an array of persons that match the search criteria.
- [func ABAddressBookCreate() -> Unmanaged<ABAddressBook>!](abaddressbookcreate().md)
  Creates a new address book object with data from the Address Book database.
- [func ABAddressBookCreateWithOptions(CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ABAddressBook>!](abaddressbookcreatewithoptions(_:_:).md)
  Creates a new address book object with data from the Address Book database.
- [func ABAddressBookGetAuthorizationStatus() -> ABAuthorizationStatus](abaddressbookgetauthorizationstatus().md)
  Returns the authorization status of your app for accessing address book data.
- [func ABAddressBookGetGroupCount(ABAddressBook!) -> CFIndex](abaddressbookgetgroupcount(_:).md)
  Returns the number of groups in an address book.
- [func ABAddressBookGetGroupWithRecordID(ABAddressBook!, ABRecordID) -> Unmanaged<ABRecord>!](abaddressbookgetgroupwithrecordid(_:_:).md)
  Returns the group with a given record ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivaluegetcount(_:))*