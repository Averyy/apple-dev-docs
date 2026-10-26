# ODNodeSetCredentialsExtended(_:_:_:_:_:_:_:)

**Framework**: Open Directory  
**Kind**: func  
**Role**: Function

Sets credentials for interacting with a node using a specified authentication method.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func ODNodeSetCredentialsExtended(_ node: ODNodeRef!, _ recordType: String!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>!, _ outContext: UnsafeMutablePointer<Unmanaged<ODContextRef>?>!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

```c
extern bool ODNodeSetCredentialsExtended(ODNodeRef node, ODRecordType recordType, ODAuthenticationType authType, CFArrayRef authItems, CFArrayRef*outAuthItems, ODContextRef*outContext, CFErrorRef*error);
```

#### Return Value

`true` if no error occurs; otherwise, `false`.

#### Discussion

If this function fails, the previous credentials for the node are used.

This function sets credentials for all references to the node. If you only want to set credentials for a single record referencing the node, use [`ODRecordSetNodeCredentialsExtended(_:_:_:_:_:_:_:)`](./odrecordsetnodecredentialsextended%28_,_,_,_,_,_,_%29.md) instead.

## Parameters

- `node`: The node.
- `recordType`: The record type that uses the credentials. Can be `NULL`. The default value is `kODRecordTypeUsers`.
- `authType`: The type of authentication to use.
- `authItems`: An array of `CFString` or `CFData` objects to be used in the authentication process.
- `outAuthItems`: An array of `CFData` objects returned from the authentication process, if any are returned; `NULL` otherwise.
- `outContext`: The proper context if the authentication attempt requires a context; `NULL` otherwise. If not `NULL`, then more calls must be made with the Context to continue the authentication.
- `error`: An error reference for error details. Can be `NULL`.

## See Also

### Related Documentation
- [Record Types](./record-types.md)
  Types of Open Directory records.
- [Authentication Types](./authentication-types.md)
  Types of authentication available in Open Directory.
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
- [ODNodeSetCredentialsUsingKerberosCache](./odnodesetcredentialsusingkerberoscache.md)
  Sets credentials for interacting with a node with the Kerberos cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnodesetcredentialsextended(_:_:_:_:_:_:_:))*