# CFXMLTreeCreateXMLData

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Generates an XML document from a CFXMLTree object which is ready to be written to permanent storage.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
extern CFDataRefCFXMLTreeCreateXMLData(CFAllocatorRef allocator, CFXMLTreeRef xmlTree);
```

#### Return Value

The XML data. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function will *not* regenerate entity references replaced at the parse time (except those required for syntactic correctness). If you need this you must manually walk the tree and re-insert any entity references that should appear in the final output file.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `xmlTree`: The CFXMLTree object you wish to convert to an XML document.

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
- [CFXMLTreeGetNode](./cfxmltreegetnode.md)
  Returns the node of a CFXMLTree object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmltreecreatexmldata)*