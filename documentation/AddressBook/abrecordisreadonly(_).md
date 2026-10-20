# ABRecordIsReadOnly(_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Returns whether or not the record is read-only.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func ABRecordIsReadOnly(_ record: ABRecordRef!) -> Bool
```

```c
extern bool ABRecordIsReadOnly(ABRecordRef record);
```

#### Return Value

`true` ifrecord is read-only, `false` otherwise.

## Parameters

- `record`: The record you wish to check.

## See Also

### Records
- [func ABAddRecord(ABAddressBookRef!, ABRecordRef!) -> Bool](./abaddrecord%28_,_%29.md)
  Adds a record of the specified type to the Address Book database.
- [func ABCopyRecordForUniqueId(ABAddressBookRef!, CFString!) -> Unmanaged<ABRecordRef>!](./abcopyrecordforuniqueid%28_,_%29.md)
  Returns the record that matches the given unique ID.
- [func ABCopyRecordTypeFromUniqueId(ABAddressBookRef!, CFString!) -> Unmanaged<CFString>!](./abcopyrecordtypefromuniqueid%28_,_%29.md)
  Returns the type name of the record that matches a given unique ID.
- [func ABCreateFormattedAddressFromDictionary(ABAddressBookRef!, CFDictionary!) -> Unmanaged<CFString>!](./abcreateformattedaddressfromdictionary%28_,_%29.md)
  Returns a string containing the formatted address.
- [func ABRecordCopyRecordType(ABRecordRef!) -> Unmanaged<CFString>!](./abrecordcopyrecordtype%28_%29.md)
  Returns the type of the given record.
- [func ABRecordCopyUniqueId(ABRecordRef!) -> Unmanaged<CFString>!](./abrecordcopyuniqueid%28_%29.md)
  Returns the unique ID of the receiver.
- [func ABRecordCopyValue(ABRecord!, ABPropertyID) -> Unmanaged<CFTypeRef>!](./abrecordcopyvalue%28_,_%29.md)
  Returns the value of the given property.
- [func ABRecordCreateCopy(ABRecordRef!) -> Unmanaged<ABRecordRef>!](./abrecordcreatecopy%28_%29.md)
  Returns a copy of the given record.
- [func ABRecordRemoveValue(ABRecord!, ABPropertyID, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./abrecordremovevalue%28_,_,_%29.md)
  Removes the value of the given property.
- [func ABRecordSetValue(ABRecord!, ABPropertyID, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./abrecordsetvalue%28_,_,_,_%29.md)
  Sets the value of a given property for a record.
- [func ABRemoveRecord(ABAddressBookRef!, ABRecordRef!) -> Bool](./abremoverecord%28_,_%29.md)
  Removes the specified record from the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecordisreadonly(_:))*