# CFXMLNodeGetTypeCode

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the XML structure type code for a CFXMLNode object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
extern CFXMLNodeTypeCode CFXMLNodeGetTypeCode(CFXMLNodeRef node);
```

#### Return Value

The type code for `node`.

## Parameters

- `node`: The CFXMLNode object to examine.

## See Also

### CFXMLNode Miscellaneous Functions
- [CFXMLNodeCreate](./cfxmlnodecreate.md)
  Creates a new CFXMLNode.
- [CFXMLNodeCreateCopy](./cfxmlnodecreatecopy.md)
  Creates a copy of a CFXMLNode object.
- [CFXMLNodeGetInfoPtr](./cfxmlnodegetinfoptr.md)
  Returns the additional information pointer of a CFXMLNode object.
- [CFXMLNodeGetString](./cfxmlnodegetstring.md)
  Returns the data string from a CFXMLNode.
- [CFXMLNodeGetTypeID](./cfxmlnodegettypeid.md)
  Returns the type identifier code for the CFXMLNode opaque type.
- [CFXMLNodeGetVersion](./cfxmlnodegetversion.md)
  Returns the version number for a CFXMLNode object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlnodegettypecode)*