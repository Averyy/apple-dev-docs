# ABMultiValueAddValueAndLabel(_:_:_:_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Adds a value and its corresponding label to a multivalue property.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: use [NSMutableArray addObject:[CNLabeledValue labeledValueWithLabel:value:]]

## Declaration

```swift
func ABMultiValueAddValueAndLabel(_ multiValue: ABMutableMultiValue!, _ value: CFTypeRef!, _ label: CFString!, _ outIdentifier: UnsafeMutablePointer<ABMultiValueIdentifier>!) -> Bool
```

```c
extern bool ABMultiValueAddValueAndLabel(ABMutableMultiValueRef multiValue, CFTypeRef value, CFStringRef label, ABMultiValueIdentifier *outIdentifier);
```

## Return Value

`true` when value is added to multiValue successfully, `false` otherwise.

## Discussion

This function performs no type checking. It allows the addition of values whose type does not match the type declared for `multiValue`.

## Parameters

- `multiValue`: The multivalue property to add `value` and `label` to.
- `value`: The value to add to `multiValue`.
- `label`: The label for `value`.
- `outIdentifier`: The address at which to place the identifier of the added value. Pass `NULL` to ignore the identifier.

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

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalueaddvalueandlabel(_:_:_:_:))*