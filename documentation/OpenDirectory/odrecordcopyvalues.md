# ODRecordCopyValues(_:_:_:)

**Framework**: Open Directory  
**Kind**: func

Returns the value of a single attribute of a record.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func ODRecordCopyValues(_ record: ODRecordRef!, _ attribute: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!
```

#### Return Value

The value of the requested attribute, or `NULL` if the attribute doesn’t exist.

#### Discussion

If the requested attribute has not been fetched before, it is fetched in order to return its value. If the record has been fetched before, internal storage is consulted instead of the directory.

## Parameters

- `record`: The record.
- `attribute`: The attribute.
- `error`: An error reference for error details. Can be  .

## See Also

- [func ODRecordAddMember(ODRecordRef!, ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordaddmember(_:_:_:).md)
  Adds a record as a member of a group record.
- [func ODRecordAddValue(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordaddvalue(_:_:_:_:).md)
  Adds a value to an attribute of a record.
- [func ODRecordChangePassword(ODRecordRef!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordchangepassword(_:_:_:_:).md)
  Changes the password of a record.
- [func ODRecordContainsMember(ODRecordRef!, ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordcontainsmember(_:_:_:).md)
  Returns whether a group record contains a given record.
- [func ODRecordCopyDetails(ODRecordRef!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](odrecordcopydetails(_:_:_:).md)
  Returns the values of a record’s attributes.
- [func ODRecordDelete(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecorddelete(_:_:).md)
  Deletes a record from a node and invalidates the record.
- [func ODRecordGetRecordName(ODRecordRef!) -> Unmanaged<CFString>!](odrecordgetrecordname(_:).md)
  Returns the official name of a record.
- [func ODRecordGetRecordType(ODRecordRef!) -> Unmanaged<CFString>!](odrecordgetrecordtype(_:).md)
  Returns the type of a record.
- [func ODRecordGetTypeID() -> CFTypeID](odrecordgettypeid().md)
  Returns the type ID for a record.
- [func ODRecordRemoveMember(ODRecordRef!, ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordremovemember(_:_:_:).md)
  Removes a record as a member from a specified group record.
- [func ODRecordRemoveValue(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordremovevalue(_:_:_:_:).md)
  Removes a value from a record’s attribute.
- [func ODRecordSetNodeCredentials(ODRecordRef!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordsetnodecredentials(_:_:_:_:).md)
  Sets node authentication credentials for a given record.
- [func ODRecordSetNodeCredentialsExtended(ODRecordRef!, String!, String!, CFArray!, UnsafeMutablePointer<Unmanaged<CFArray>?>!, UnsafeMutablePointer<Unmanaged<ODContext>?>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordsetnodecredentialsextended(_:_:_:_:_:_:_:).md)
  Sets node authentication credentials for a record using a specified authentication method.
- [func ODRecordSetValue(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordsetvalue(_:_:_:_:).md)
  Sets one or more attribute values of a record.
- [func ODRecordSynchronize(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordsynchronize(_:_:).md)
  Synchronizes a record with the directory to get current data and commit changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecordcopyvalues(_:_:_:))*