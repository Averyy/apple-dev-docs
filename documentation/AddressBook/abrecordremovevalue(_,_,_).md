# ABRecordRemoveValue(_:_:_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Removes the value of the given property.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS

> **Deprecated**: use CN mutable object's properties, setting to @, @[], or nil

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
func ABRecordRemoveValue(_ record: ABRecord!, _ property: ABPropertyID, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

*macOS*

```swift
func ABRecordRemoveValue(_ record: ABRecordRef!, _ property: CFString!) -> Bool
```

*iOS, iPadOS, Mac Catalyst*

```c
extern bool ABRecordRemoveValue(ABRecordRef record, ABPropertyID property, CFErrorRef*error);
```

*macOS*

```c
extern bool ABRecordRemoveValue(ABRecordRef record, CFStringRef property);
```

## Return Value

The value for `property` in `record`.The type of the returned value depends on the property type (see PropertyTypes for a list of possible property types). You are responsiblefor releasing this object.

## Parameters

- `record`: The record whose value you wish to remove.
- `property`: The property name in `record` whose value you wish to remove. May be a pre-defined or program-defined property. See `Common Properties` for a list of properties all records have, and specific ABRecord derived opaque types for any additional properties.

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
- [func ABRecordSetValue(ABRecord!, ABPropertyID, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./abrecordsetvalue%28_,_,_,_%29.md)
  Sets the value of a given property for a record.
- [func ABRemoveRecord(ABAddressBookRef!, ABRecordRef!) -> Bool](./abremoverecord%28_,_%29.md)
  Removes the specified record from the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecordremovevalue(_:_:_:))*