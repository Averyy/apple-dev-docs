# ODRecordSetNodeCredentialsUsingKerberosCache

**Framework**: Open Directory  
**Kind**: func  
**Role**: Function

Sets credentials for interacting with a record’s node with the Kerberos cache.

**Availability**:
- Mac Catalyst
- macOS 10.6+ - Deprecated in 10.7

## Declaration

```c
extern bool ODRecordSetNodeCredentialsUsingKerberosCache(ODRecordRef record, CFStringRef cacheName, CFErrorRef*error);
```

## Return Value

`true` if the credentials are successfully set; otherwise, `false`.

## Discussion

If you want to set credentials for all references to a node, use [`ODNodeSetCredentialsUsingKerberosCache`](./odnodesetcredentialsusingkerberoscache.md) instead.

## Parameters

- `record`: The record.
- `cacheName`: The name of the Kerberos cache to use. Can be `NULL`. By default, the currently active Kerberos cache is used.
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
- [ODRecordCopyPasswordPolicy](./odrecordcopypasswordpolicy.md)
  Returns the password policies of a record.
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
- [func ODRecordSetNodeCredentials(ODRecordRef!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordsetnodecredentials%28_,_,_,_%29.md)
  Sets node authentication credentials for a given record.
- [func ODRecordSetNodeCredentialsExtended(ODRecordRef!, String!, String!, CFArray!, UnsafeMutablePointer<Unmanaged<CFArray>?>!, UnsafeMutablePointer<Unmanaged<ODContextRef>?>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odrecordsetnodecredentialsextended%28_,_,_,_,_,_,_%29.md)
  Sets node authentication credentials for a record using a specified authentication method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecordsetnodecredentialsusingkerberoscache)*