# ODNodeCopySupportedAttributes(_:_:_:)

**Framework**: Open Directory  
**Kind**: func

Returns an array of attribute types supported by a given node.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func ODNodeCopySupportedAttributes(_ node: ODNodeRef!, _ recordType: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!
```

#### Return Value

An array of supported attribute types.

#### Discussion

If `inRecordType` is `NULL`, this function returns all attribute types supported by all record types of the node; otherwise, only attribute types specific to `inRecordType` are returned.

## Parameters

- `node`: The node.
- `recordType`: The record type to list supported attribute types for. Can be  .
- `error`: An error reference for error details. Can be  .

## See Also

- [Record Types](record-types.md)
  Types of Open Directory records.
- [func ODNodeCopyDetails(ODNodeRef!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](odnodecopydetails(_:_:_:).md)
  Returns a dictionary containing details about a node.
- [func ODNodeCopyRecord(ODNodeRef!, String!, CFString!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODRecordRef>!](odnodecopyrecord(_:_:_:_:_:).md)
  Returns a reference to a record of a node.
- [func ODNodeCopySubnodeNames(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](odnodecopysubnodenames(_:_:).md)
  Returns the names of subnodes for a given node.
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
- [func ODNodeSetCredentialsExtended(ODNodeRef!, String!, String!, CFArray!, UnsafeMutablePointer<Unmanaged<CFArray>?>!, UnsafeMutablePointer<Unmanaged<ODContext>?>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](odnodesetcredentialsextended(_:_:_:_:_:_:_:).md)
  Sets credentials for interacting with a node using a specified authentication method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnodecopysupportedattributes(_:_:_:))*