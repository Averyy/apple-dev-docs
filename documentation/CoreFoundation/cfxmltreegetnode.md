# CFXMLTreeGetNode

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the node of a CFXMLTree object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
extern CFXMLNodeRefCFXMLTreeGetNode(CFXMLTreeRef xmlTree);
```

## Return Value

The node of `xmlTree`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `xmlTree`: The CFXMLTree object whose node you wish to obtain.

## See Also

### CFXMLTree Miscellaneous Functions
- [func CFXMLCreateStringByEscapingEntities(CFAllocator!, CFString!, CFDictionary!) -> CFString!](./cfxmlcreatestringbyescapingentities%28_,_,_%29.md)
  Given a CFString object containing XML source with unescaped entities, returns a string with specified XML entities escaped.
- [func CFXMLCreateStringByUnescapingEntities(CFAllocator!, CFString!, CFDictionary!) -> CFString!](./cfxmlcreatestringbyunescapingentities%28_,_,_%29.md)
  Given a CFString object containing XML source with escaped entities, returns a string with specified XML entities unescaped.
- [CFXMLTreeCreateFromData](./cfxmltreecreatefromdata.md)
  Parses the given XML data and returns the resulting CFXMLTree object.
- [CFXMLTreeCreateFromDataWithError](./cfxmltreecreatefromdatawitherror.md)
  Parses the given XML data and returns the resulting CFXMLTree object and any error information.
- [CFXMLTreeCreateWithDataFromURL](./cfxmltreecreatewithdatafromurl.md)
  Creates a new CFXMLTree object by loading the data to be parsed directly from a data source.
- [CFXMLTreeCreateWithNode](./cfxmltreecreatewithnode.md)
  Creates a childless, parentless CFXMLTree object node for a CFXMLNode object.
- [CFXMLTreeCreateXMLData](./cfxmltreecreatexmldata.md)
  Generates an XML document from a CFXMLTree object which is ready to be written to permanent storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmltreegetnode)*