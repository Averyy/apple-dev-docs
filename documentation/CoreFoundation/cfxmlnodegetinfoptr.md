# CFXMLNodeGetInfoPtr

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the additional information pointer of a CFXMLNode object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
extern const void *CFXMLNodeGetInfoPtr(CFXMLNodeRef node);
```

## Return Value

A pointer to a structure containing additional information. The CFXMLNode version together with the node’s type determines the expected structure. See [`CFXMLNodeTypeCode`](./cfxmlnodetypecode.md) for information about the possible structures returned. If the returned value is a Core Foundation object, ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `node`: The CFXMLNode object to examine.

## See Also

### CFXMLNode Miscellaneous Functions
- [CFXMLNodeCreate](./cfxmlnodecreate.md)
  Creates a new CFXMLNode.
- [CFXMLNodeCreateCopy](./cfxmlnodecreatecopy.md)
  Creates a copy of a CFXMLNode object.
- [CFXMLNodeGetString](./cfxmlnodegetstring.md)
  Returns the data string from a CFXMLNode.
- [CFXMLNodeGetTypeCode](./cfxmlnodegettypecode.md)
  Returns the XML structure type code for a CFXMLNode object.
- [CFXMLNodeGetTypeID](./cfxmlnodegettypeid.md)
  Returns the type identifier code for the CFXMLNode opaque type.
- [CFXMLNodeGetVersion](./cfxmlnodegetversion.md)
  Returns the version number for a CFXMLNode object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlnodegetinfoptr)*