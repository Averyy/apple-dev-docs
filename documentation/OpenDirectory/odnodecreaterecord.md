# ODNodeCreateRecord(_:_:_:_:_:)

**Framework**: Open Directory  
**Kind**: func

Creates a record in a specified node with specified properties.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func ODNodeCreateRecord(_ node: ODNodeRef!, _ recordType: String!, _ recordName: CFString!, _ attributeDict: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODRecordRef>!
```

#### Return Value

The created record.

#### Discussion

The keys in `inAttributes` can be of type `CFStringRef` or one of the `ODRecordType` constants. The values in `inAttributes` must be of type `CFArrayRef`, containing elements of type `CFStringRef` or `CFDataRef`.

If any of the attributes in `inAttributes` fails to be set, the record is deleted and `outError` is set.

## Parameters

- `node`: The node.
- `recordType`: The record’s type.
- `recordName`: The record’s name.
- `attributeDict`: A dictionary of key-value pairs representing attributes for the record. Can be  .
- `error`: An error reference for error details. Can be  .

## See Also

- [Record Types](record-types.md)
  Types of Open Directory records.
- [General Attribute Types](general-attribute-types.md)
  Types of Open Directory attributes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnodecreaterecord(_:_:_:_:_:))*