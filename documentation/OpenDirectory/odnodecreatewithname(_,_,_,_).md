# ODNodeCreateWithName(_:_:_:_:)

**Framework**: Open Directory  
**Kind**: func  
**Role**: Function

Returns a new node created with a specified name.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func ODNodeCreateWithName(_ allocator: CFAllocator!, _ session: ODSessionRef!, _ nodeName: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<ODNodeRef>!
```

```c
extern ODNodeRefODNodeCreateWithName(CFAllocatorRef allocator, ODSessionRef session, CFStringRef nodeName, CFErrorRef*error);
```

#### Return Value

The created node.

## Parameters

- `allocator`: The memory allocator to use. If `NULL`, the default allocator is used.
- `session`: The session to create the node in.
- `nodeName`: The name of the node.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnodecreatewithname(_:_:_:_:))*