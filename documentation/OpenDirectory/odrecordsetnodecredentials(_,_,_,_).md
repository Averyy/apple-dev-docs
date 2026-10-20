# ODRecordSetNodeCredentials(_:_:_:_:)

**Framework**: Open Directory  
**Kind**: func  
**Role**: Function

Sets node authentication credentials for a given record.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func ODRecordSetNodeCredentials(_ record: ODRecordRef!, _ username: CFString!, _ password: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

```c
extern bool ODRecordSetNodeCredentials(ODRecordRef record, CFStringRef username, CFStringRef password, CFErrorRef*error);
```

#### Return Value

`true` if the credentials are successfully set; otherwise, `false`.

#### Discussion

If you want to set credentials for all references to a node, use [`ODNodeSetCredentials(_:_:_:_:_:)`](./odnodesetcredentials%28_,_,_,_,_%29.md) instead.

If this function fails, the previous credentials are used.

## Parameters

- `record`: The record.
- `username`: The username to use to authenticate with the node.
- `password`: The password to use to authenticate with the node.
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
- [func ODRecordRemoveValue(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordremovevalue%28_,_,_,_%29.md)
  Removes a value from a record’s attribute.
- [func ODRecordSetNodeCredentialsExtended(ODRecordRef!, String!, String!, CFArray!, UnsafeMutablePointer<Unmanaged<CFArray>?>!, UnsafeMutablePointer<Unmanaged<ODContextRef>?>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordsetnodecredentialsextended%28_,_,_,_,_,_,_%29.md)
  Sets node authentication credentials for a record using a specified authentication method.
- [func ODRecordSetValue(ODRecordRef!, String!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordsetvalue%28_,_,_,_%29.md)
  Sets one or more attribute values of a record.
- [func ODRecordSynchronize(ODRecordRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordsynchronize%28_,_%29.md)
  Synchronizes a record with the directory to get current data and commit changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecordsetnodecredentials(_:_:_:_:))*