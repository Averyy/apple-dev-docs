# ODRecordRemoveValue(_:_:_:_:)

**Framework**: Open Directory  
**Kind**: func  
**Role**: Function

Removes a value from a record’s attribute.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func ODRecordRemoveValue(_ record: ODRecordRef!, _ attribute: String!, _ value: CFTypeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

```c
extern bool ODRecordRemoveValue(ODRecordRef record, ODAttributeType attribute, CFTypeRef value, CFErrorRef*error);
```

#### Return Value

`true` if `inValue` is successfully removed from `inAttribute`; otherwise, `false`.

#### Discussion

If `inValue` does not exist, `true` is returned and no error is set.

## Parameters

- `record`: The record.
- `attribute`: The attribute.
- `value`: The value to remove.
- `error`: An error reference for error details. Can be `NULL`.

## See Also

### Working with Records
- [func ODRecordAddMember(ODRecordRef!, ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordaddmember%28_,_,_%29.md)
  Adds a record as a member of a group record.
- [func ODRecordAddValue(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordaddvalue%28_,_,_,_%29.md)
  Adds a value to an attribute of a record.
- [func ODRecordChangePassword(ODRecordRef!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordchangepassword%28_,_,_,_%29.md)
  Changes the password of a record.
- [func ODRecordContainsMember(ODRecordRef!, ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordcontainsmember%28_,_,_%29.md)
  Returns whether a group record contains a given record.
- [func ODRecordCopyDetails(ODRecordRef!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](./odrecordcopydetails%28_,_,_%29.md)
  Returns the values of a record’s attributes.
- [func ODRecordCopyValues(ODRecordRef!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](./odrecordcopyvalues%28_,_,_%29.md)
  Returns the value of a single attribute of a record.
- [func ODRecordDelete(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecorddelete%28_,_%29.md)
  Deletes a record from a node and invalidates the record.
- [func ODRecordGetRecordName(ODRecordRef!) -> Unmanaged<CFString>!](./odrecordgetrecordname%28_%29.md)
  Returns the official name of a record.
- [func ODRecordGetRecordType(ODRecordRef!) -> Unmanaged<CFString>!](./odrecordgetrecordtype%28_%29.md)
  Returns the type of a record.
- [func ODRecordGetTypeID() -> CFTypeID](./odrecordgettypeid%28%29.md)
  Returns the type ID for a record.
- [func ODRecordRemoveMember(ODRecordRef!, ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordremovemember%28_,_,_%29.md)
  Removes a record as a member from a specified group record.
- [func ODRecordSetNodeCredentials(ODRecordRef!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordsetnodecredentials%28_,_,_,_%29.md)
  Sets node authentication credentials for a given record.
- [func ODRecordSetNodeCredentialsExtended(ODRecordRef!, String!, String!, CFArray!, UnsafeMutablePointer<Unmanaged<CFArray>?>!, UnsafeMutablePointer<Unmanaged<ODContextRef>?>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordsetnodecredentialsextended%28_,_,_,_,_,_,_%29.md)
  Sets node authentication credentials for a record using a specified authentication method.
- [func ODRecordSetValue(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordsetvalue%28_,_,_,_%29.md)
  Sets one or more attribute values of a record.
- [func ODRecordSynchronize(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordsynchronize%28_,_%29.md)
  Synchronizes a record with the directory to get current data and commit changes.
- [ODRecordCopyPasswordPolicy](./odrecordcopypasswordpolicy.md)
  Returns the password policies of a record.
- [ODRecordSetNodeCredentialsUsingKerberosCache](./odrecordsetnodecredentialsusingkerberoscache.md)
  Sets credentials for interacting with a record’s node with the Kerberos cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecordremovevalue(_:_:_:_:))*