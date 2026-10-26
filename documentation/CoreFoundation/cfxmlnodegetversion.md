# CFXMLNodeGetVersion

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the version number for a CFXMLNode object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
extern CFIndex CFXMLNodeGetVersion(CFXMLNodeRef node);
```

#### Return Value

The version number of `node`.

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
- [CFXMLNodeGetTypeCode](./cfxmlnodegettypecode.md)
  Returns the XML structure type code for a CFXMLNode object.
- [CFXMLNodeGetTypeID](./cfxmlnodegettypeid.md)
  Returns the type identifier code for the CFXMLNode opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlnodegetversion)*