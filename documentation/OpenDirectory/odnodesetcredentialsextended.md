# ODNodeSetCredentialsExtended(_:_:_:_:_:_:_:)

**Framework**: Open Directory  
**Kind**: func

Sets credentials for interacting with a node using a specified authentication method.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func ODNodeSetCredentialsExtended(_ node: ODNodeRef!, _ recordType: String!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>!, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

#### Return Value

`true` if no error occurs; otherwise, `false`.

#### Discussion

If this function fails, the previous credentials for the node are used.

This function sets credentials for all references to the node. If you only want to set credentials for a single record referencing the node, use [`ODRecordSetNodeCredentialsExtended(_:_:_:_:_:_:_:)`](odrecordsetnodecredentialsextended(_:_:_:_:_:_:_:).md) instead.

## Parameters

- `node`: The node.
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
- [func ODNodeCopyDetails(ODNodeRef!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](odnodecopydetails(_:_:_:).md)
  Returns a dictionary containing details about a node.
- [func ODNodeCopyRecord(ODNodeRef!, String!, CFString!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODRecordRef>!](odnodecopyrecord(_:_:_:_:_:).md)
  Returns a reference to a record of a node.
- [func ODNodeCopySubnodeNames(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](odnodecopysubnodenames(_:_:).md)
  Returns the names of subnodes for a given node.
- [func ODNodeCopySupportedAttributes(ODNodeRef!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](odnodecopysupportedattributes(_:_:_:).md)
  Returns an array of attribute types supported by a given node.
- [func ODNodeCopySupportedRecordTypes(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](odnodecopysupportedrecordtypes(_:_:).md)
  Returns an array of the record types supported by a given node.
- [func ODNodeCopyUnreachableSubnodeNames(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](odnodecopyunreachablesubnodenames(_:_:).md)
  Returns an array of the subnodes of a given node that are currently unreachable.
- [func ODNodeCreateCopy(CFAllocator!, ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!](odnodecreatecopy(_:_:_:).md)
  Returns a copy of an existing node.
- [func ODNodeCreateRecord(ODNodeRef!, String!, CFString!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODRecordRef>!](odnodecreaterecord(_:_:_:_:_:).md)
  Creates a record in a specified node with specified properties.
- [func ODNodeCreateWithName(CFAllocator!, ODSessionRef!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!](odnodecreatewithname(_:_:_:_:).md)
  Returns a new node created with a specified name.
- [func ODNodeCreateWithNodeType(CFAllocator!, ODSessionRef!, ODNodeType, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!](odnodecreatewithnodetype(_:_:_:_:).md)
  Returns a new node created with a specified type.
- [func ODNodeCustomCall(ODNodeRef!, CFIndex, CFData!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFData!](odnodecustomcall(_:_:_:_:).md)
  Returns the result of a custom call to a node.
- [func ODNodeGetName(ODNodeRef!) -> Unmanaged<CFString>!](odnodegetname(_:).md)
  Returns the name of a node.
- [func ODNodeGetTypeID() -> CFTypeID](odnodegettypeid().md)
  Returns the type ID for an Open Directory node.
- [func ODNodeSetCredentials(ODNodeRef!, String!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnodesetcredentials(_:_:_:_:_:).md)
  Sets credentials for interacting with a node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnodesetcredentialsextended(_:_:_:_:_:_:_:))*