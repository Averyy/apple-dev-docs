# ABRecordCopyRecordType(_:)

**Framework**: Address Book  
**Kind**: func

Returns the type of the given record.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABRecordCopyRecordType(_ record: ABRecordRef!) -> Unmanaged<CFString>!
```

#### Return Value

The type of `record`,one of the `kAB...RecordType` constants.You are responsible for releasing this object.

## Parameters

- `record`: The record whose type you wish to obtain.

## See Also

- [func ABAddRecord(ABAddressBookRef!, ABRecordRef!) -> Bool](abaddrecord(_:_:).md)
  Adds a record of the specified type to the Address Book database.
- [func ABCopyRecordForUniqueId(ABAddressBookRef!, CFString!) -> Unmanaged<ABRecordRef>!](abcopyrecordforuniqueid(_:_:).md)
  Returns the record that matches the given unique ID.
- [func ABCopyRecordTypeFromUniqueId(ABAddressBookRef!, CFString!) -> Unmanaged<CFString>!](abcopyrecordtypefromuniqueid(_:_:).md)
  Returns the type name of the record that matches a given unique ID.
- [func ABCreateFormattedAddressFromDictionary(ABAddressBookRef!, CFDictionary!) -> Unmanaged<CFString>!](abcreateformattedaddressfromdictionary(_:_:).md)
  Returns a string containing the formatted address.
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

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecordcopyrecordtype(_:))*