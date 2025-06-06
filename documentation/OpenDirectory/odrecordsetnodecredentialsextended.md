# ODRecordSetNodeCredentialsExtended(_:_:_:_:_:_:_:)

**Framework**: Open Directory  
**Kind**: func

Sets node authentication credentials for a record using a specified authentication method.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func ODRecordSetNodeCredentialsExtended(_ record: ODRecordRef!, _ recordType: String!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>!, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

#### Return Value

`true` if no error occurs; otherwise, `false`.

#### Discussion

If you want to set credentials for all references to a node, use [`ODNodeSetCredentialsExtended(_:_:_:_:_:_:_:)`](odnodesetcredentialsextended(_:_:_:_:_:_:_:).md) instead.

## Parameters

- `record`: The record.
- `recordType`: The record type that uses the credentials. Can be  . The default value is  .
- `authType`: The type of authentication to use.
- `authItems`: An array of   or   objects to be used in the authentication process.
- `outAuthItems`: An array of   objects returned from the authentication process, if any are returned;   otherwise.
- `outContext`: The proper context if the authentication attempt requires a context;   otherwise. If not  , then more calls must be made with the Context to continue the authentication.
- `error`: An error reference for error details. Can be  .

## See Also

- [Record Types](record-types.md)
  Types of Open Directory records.
- [Authentication Types](authentication-types.md)
  Types of authentication available in Open Directory.
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
- [func ODRecordCopyValues(ODRecordRef!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](odrecordcopyvalues(_:_:_:).md)
  Returns the value of a single attribute of a record.
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
- [func ODRecordSetValue(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordsetvalue(_:_:_:_:).md)
  Sets one or more attribute values of a record.
- [func ODRecordSynchronize(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordsynchronize(_:_:).md)
  Synchronizes a record with the directory to get current data and commit changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecordsetnodecredentialsextended(_:_:_:_:_:_:_:))*