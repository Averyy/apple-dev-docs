# ABRecordSetValue(_:_:_:_:)

**Framework**: Address Book  
**Kind**: func

Sets the value of a given property for a record.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
func ABRecordSetValue(_ record: ABRecord!, _ property: ABPropertyID, _ value: CFTypeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

#### Return Value

If `property` isa multi-value list property, this method checks to see if the valuesin the multi-value list are the same type. If the multi-value list containsmixed types, this method returns `false`.Returns `true` if successful, `false` otherwise.

## Parameters

- `record`: The record you wish to modify.
- `property`: The property whose value you wish to set. May be a pre-defined or program-defined property. See   for a list of properties all records have, and specific ABRecord derived opaque types for any additional properties. If  , this function raises an exception.
- `value`: The new value for   in  . If   or not the correct type, this function raises an exception.

## See Also

- [func ABAddRecord(ABAddressBookRef!, ABRecordRef!) -> Bool](abaddrecord(_:_:).md)
  Adds a record of the specified type to the Address Book database.
- [func ABCopyRecordForUniqueId(ABAddressBookRef!, CFString!) -> Unmanaged<ABRecordRef>!](abcopyrecordforuniqueid(_:_:).md)
  Returns the record that matches the given unique ID.
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
- [func ABRemoveRecord(ABAddressBookRef!, ABRecordRef!) -> Bool](abremoverecord(_:_:).md)
  Removes the specified record from the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecordsetvalue(_:_:_:))*