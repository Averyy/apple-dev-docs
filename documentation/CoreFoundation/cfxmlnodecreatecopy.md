# CFXMLNodeCreateCopy

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a copy of a CFXMLNode object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
extern CFXMLNodeRefCFXMLNodeCreateCopy(CFAllocatorRef alloc, CFXMLNodeRef origNode);
```

## Return Value

A new CFXMLNode object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `origNode`: The node to copy. Do not pass `NULL`.

## See Also

### CFXMLNode Miscellaneous Functions
- [CFXMLNodeCreate](./cfxmlnodecreate.md)
  Creates a new CFXMLNode.
- [CFXMLNodeGetInfoPtr](./cfxmlnodegetinfoptr.md)
  Returns the additional information pointer of a CFXMLNode object.
- [CFXMLNodeGetString](./cfxmlnodegetstring.md)
  Returns the data string from a CFXMLNode.
- [CFXMLNodeGetTypeCode](./cfxmlnodegettypecode.md)
  Returns the XML structure type code for a CFXMLNode object.
- [CFXMLNodeGetTypeID](./cfxmlnodegettypeid.md)
  Returns the type identifier code for the CFXMLNode opaque type.
- [CFXMLNodeGetVersion](./cfxmlnodegetversion.md)
  Returns the version number for a CFXMLNode object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlnodecreatecopy)*