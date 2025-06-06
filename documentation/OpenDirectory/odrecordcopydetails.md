# ODRecordCopyDetails(_:_:_:)

**Framework**: Open Directory  
**Kind**: func

Returns the values of a record’s attributes.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func ODRecordCopyDetails(_ record: ODRecordRef!, _ attributes: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!
```

#### Return Value

The attribute values of the record.

#### Discussion

The returned values are of type `CFString` or `CFData`, depending on the type of attribute. If `inAttributes` is not `NULL` and a requested attribute has not been fetched before, it is fetched in order to return its value.

## Parameters

- `record`: The record.
- `attributes`: An array of attributes to return values for. Elements are of type   or  . If  , all currently fetched values are returned.
- `error`: An error reference for error details. Can be  .

## See Also

- [General Attribute Types](general-attribute-types.md)
  Types of Open Directory attributes.
- [func ODRecordAddMember(ODRecordRef!, ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordaddmember(_:_:_:).md)
  Adds a record as a member of a group record.
- [func ODRecordAddValue(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordaddvalue(_:_:_:_:).md)
  Adds a value to an attribute of a record.
- [func ODRecordChangePassword(ODRecordRef!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordchangepassword(_:_:_:_:).md)
  Changes the password of a record.
- [func ODRecordContainsMember(ODRecordRef!, ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordcontainsmember(_:_:_:).md)
  Returns whether a group record contains a given record.
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
- [func ODRecordSetNodeCredentialsExtended(ODRecordRef!, String!, String!, CFArray!, UnsafeMutablePointer<Unmanaged<CFArray>?>!, UnsafeMutablePointer<Unmanaged<ODContext>?>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordsetnodecredentialsextended(_:_:_:_:_:_:_:).md)
  Sets node authentication credentials for a record using a specified authentication method.
- [func ODRecordSetValue(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordsetvalue(_:_:_:_:).md)
  Sets one or more attribute values of a record.
- [func ODRecordSynchronize(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odrecordsynchronize(_:_:).md)
  Synchronizes a record with the directory to get current data and commit changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecordcopydetails(_:_:_:))*