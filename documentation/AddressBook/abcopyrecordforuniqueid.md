# ABCopyRecordForUniqueId(_:_:)

**Framework**: Address Book  
**Kind**: func

Returns the record that matches the given unique ID.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABCopyRecordForUniqueId(_ addressBook: ABAddressBookRef!, _ uniqueId: CFString!) -> Unmanaged<ABRecordRef>!
```

#### Return Value

The record that matches the given unique ID. If no record matches `uniqueId`, the function returns `NULL`. You are responsible for releasing this object.

## Parameters

- `addressBook`: The address book for the logged-in user.
- `uniqueId`: A unique ID for the record. If this is  , this function raises an exception.

## See Also

- [func ABAddRecord(ABAddressBookRef!, ABRecordRef!) -> Bool](abaddrecord(_:_:).md)
  Adds a record of the specified type to the Address Book database.
- [func ABCopyRecordTypeFromUniqueId(ABAddressBookRef!, CFString!) -> Unmanaged<CFString>!](abcopyrecordtypefromuniqueid(_:_:).md)
  Returns the type name of the record that matches a given unique ID.
- [func ABCreateFormattedAddressFromDictionary(ABAddressBookRef!, CFDictionary!) -> Unmanaged<CFString>!](abcreateformattedaddressfromdictionary(_:_:).md)
  Returns a string containing the formatted address.
- [func ABRecordCopyRecordType(ABRecordRef!) -> Unmanaged<CFString>!](abrecordcopyrecordtype(_:).md)
  Returns the type of the given record.
- [func ABRecordCopyUniqueId(ABRecordRef!) -> Unmanaged<CFString>!](abrecordcopyuniqueid(_:).md)
  Returns the unique ID of the receiver.
- [func ABRecordCopyValue(ABRecord!, ABPropertyID) -> Unmanaged<CFTypeRef>!](abrecordcopyvalue(_:_:).md)
  Returns the value of the given property.
- [func ABRecordCreateCopy(ABRecordRef!) -> Unmanaged<ABRecordRef>!](abrecordcreatecopy(_:).md)
  Returns a copy of the given record.
- [func ABRecordIsReadOnly(ABRecordRef!) -> Bool](abrecordisreadonly(_:).md)
  Returns whether or not the record is read-only.
- [func ABRecordRemoveValue(ABRecord!, ABPropertyID, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abrecordremovevalue(_:_:).md)
  Removes the value of the given property.
- [func ABRecordSetValue(ABRecord!, ABPropertyID, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](abrecordsetvalue(_:_:_:).md)
  Sets the value of a given property for a record.
- [func ABRemoveRecord(ABAddressBookRef!, ABRecordRef!) -> Bool](abremoverecord(_:_:).md)
  Removes the specified record from the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abcopyrecordforuniqueid(_:_:))*