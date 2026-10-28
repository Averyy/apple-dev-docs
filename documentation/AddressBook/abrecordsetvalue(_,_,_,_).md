# ABRecordSetValue(_:_:_:_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Sets the value of a given property for a record.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS

> **Deprecated**: use CN mutable object's properties

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
func ABRecordSetValue(_ record: ABRecord!, _ property: ABPropertyID, _ value: CFTypeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

*macOS*

```swift
func ABRecordSetValue(_ record: ABRecordRef!, _ property: CFString!, _ value: CFTypeRef!) -> Bool
```

*iOS, iPadOS, Mac Catalyst*

```c
extern bool ABRecordSetValue(ABRecordRef record, ABPropertyID property, CFTypeRef value, CFErrorRef*error);
```

*macOS*

```c
extern bool ABRecordSetValue(ABRecordRef record, CFStringRef property, CFTypeRef value);
```

## Return Value

If `property` isa multi-value list property, this method checks to see if the valuesin the multi-value list are the same type. If the multi-value list containsmixed types, this method returns `false`.Returns `true` if successful, `false` otherwise.

## Parameters

- `record`: The record you wish to modify.
- `property`: The property whose value you wish to set. May be a pre-defined or program-defined property. See `Common Properties` for a list of properties all records have, and specific ABRecord derived opaque types for any additional properties. If `NULL`, this function raises an exception.
- `value`: The new value for `property` in `record`. If `NULL` or not the correct type, this function raises an exception.

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
- [func ABRecordIsReadOnly(ABRecordRef!) -> Bool](./abrecordisreadonly%28_%29.md)
  Returns whether or not the record is read-only.
- [func ABRecordRemoveValue(ABRecord!, ABPropertyID, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./abrecordremovevalue%28_,_,_%29.md)
  Removes the value of the given property.
- [func ABRemoveRecord(ABAddressBookRef!, ABRecordRef!) -> Bool](./abremoverecord%28_,_%29.md)
  Removes the specified record from the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecordsetvalue(_:_:_:_:))*