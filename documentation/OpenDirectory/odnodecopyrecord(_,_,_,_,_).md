# ODNodeCopyRecord(_:_:_:_:_:)

**Framework**: Open Directory  
**Kind**: func  
**Role**: Function

Returns a reference to a record of a node.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func ODNodeCopyRecord(_ node: ODNodeRef!, _ recordType: String!, _ recordName: CFString!, _ attributes: CFTypeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODRecordRef>!
```

```c
extern ODRecordRefODNodeCopyRecord(ODNodeRef node, ODRecordType recordType, CFStringRef recordName, CFTypeRef attributes, CFErrorRef*error);
```

## Return Value

A reference to a specified record of `inNode`.

## Parameters

- `node`: The node.
- `recordType`: The type of the record.
- `recordName`: The name of the record.
- `attributes`: An array of directory attributes to be copied in addition to the record. Can be `NULL`.
- `error`: An error reference for error details. Can be `NULL`.

## See Also

### Related Documentation
- [Record Types](./record-types.md)
  Types of Open Directory records.
- [General Attribute Types](./general-attribute-types.md)
  Types of Open Directory attributes.
### Working with Nodes
- [func ODNodeCopyDetails(ODNodeRef!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](./odnodecopydetails%28_,_,_%29.md)
  Returns a dictionary containing details about a node.
- [func ODNodeCopySubnodeNames(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](./odnodecopysubnodenames%28_,_%29.md)
  Returns the names of subnodes for a given node.
- [func ODNodeCopySupportedAttributes(ODNodeRef!, String!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](./odnodecopysupportedattributes%28_,_,_%29.md)
  Returns an array of attribute types supported by a given node.
- [func ODNodeCopySupportedRecordTypes(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](./odnodecopysupportedrecordtypes%28_,_%29.md)
  Returns an array of the record types supported by a given node.
- [func ODNodeCopyUnreachableSubnodeNames(ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFArray>!](./odnodecopyunreachablesubnodenames%28_,_%29.md)
  Returns an array of the subnodes of a given node that are currently unreachable.
- [func ODNodeCreateCopy(CFAllocator!, ODNodeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!](./odnodecreatecopy%28_,_,_%29.md)
  Returns a copy of an existing node.
- [func ODNodeCreateRecord(ODNodeRef!, String!, CFString!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODRecordRef>!](./odnodecreaterecord%28_,_,_,_,_%29.md)
  Creates a record in a specified node with specified properties.
- [func ODNodeCreateWithName(CFAllocator!, ODSessionRef!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!](./odnodecreatewithname%28_,_,_,_%29.md)
  Returns a new node created with a specified name.
- [func ODNodeCreateWithNodeType(CFAllocator!, ODSessionRef!, ODNodeType, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!](./odnodecreatewithnodetype%28_,_,_,_%29.md)
  Returns a new node created with a specified type.
- [func ODNodeCustomCall(ODNodeRef!, CFIndex, CFData!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> CFData!](./odnodecustomcall%28_,_,_,_%29.md)
  Returns the result of a custom call to a node.
- [func ODNodeGetName(ODNodeRef!) -> Unmanaged<CFString>!](./odnodegetname%28_%29.md)
  Returns the name of a node.
- [func ODNodeGetTypeID() -> CFTypeID](./odnodegettypeid%28%29.md)
  Returns the type ID for an Open Directory node.
- [func ODNodeSetCredentials(ODNodeRef!, String!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnodesetcredentials%28_,_,_,_,_%29.md)
  Sets credentials for interacting with a node.
- [func ODNodeSetCredentialsExtended(ODNodeRef!, String!, String!, CFArray!, UnsafeMutablePointer<Unmanaged<CFArray>?>!, UnsafeMutablePointer<Unmanaged<ODContextRef>?>!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./odnodesetcredentialsextended%28_,_,_,_,_,_,_%29.md)
  Sets credentials for interacting with a node using a specified authentication method.
- [ODNodeSetCredentialsUsingKerberosCache](./odnodesetcredentialsusingkerberoscache.md)
  Sets credentials for interacting with a node with the Kerberos cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnodecopyrecord(_:_:_:_:_:))*