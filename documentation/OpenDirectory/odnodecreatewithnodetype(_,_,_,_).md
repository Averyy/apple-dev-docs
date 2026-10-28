# ODNodeCreateWithNodeType(_:_:_:_:)

**Framework**: Open Directory  
**Kind**: func  
**Role**: Function

Returns a new node created with a specified type.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func ODNodeCreateWithNodeType(_ allocator: CFAllocator!, _ session: ODSessionRef!, _ nodeType: ODNodeType, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!
```

```c
extern ODNodeRefODNodeCreateWithNodeType(CFAllocatorRef allocator, ODSessionRef session, ODNodeType nodeType, CFErrorRef*error);
```

## Return Value

The created node.

## Parameters

- `allocator`: The memory allocator to use. If `NULL`, the default allocator is used.
- `session`: The session to create the node in.
- `nodeType`: The type of the node.
- `error`: An error reference for error details. Can be `NULL`.

## See Also

### Working with Nodes
- [func ODNodeCopyDetails(ODNodeRef!, CFArray!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFDictionary>!](./odnodecopydetails%28_,_,_%29.md)
  Returns a dictionary containing details about a node.
- [func ODNodeCopyRecord(ODNodeRef!, String!, CFString!, CFTypeRef!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODRecordRef>!](./odnodecopyrecord%28_,_,_,_,_%29.md)
  Returns a reference to a record of a node.
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

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnodecreatewithnodetype(_:_:_:_:))*