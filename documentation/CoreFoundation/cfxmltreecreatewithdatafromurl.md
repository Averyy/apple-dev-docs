# CFXMLTreeCreateWithDataFromURL

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a new CFXMLTree object by loading the data to be parsed directly from a data source.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
extern CFXMLTreeRefCFXMLTreeCreateWithDataFromURL(CFAllocatorRef allocator, CFURLRef dataSource, CFOptionFlags parseOptions, CFIndex versionOfNodes);
```

## Return Value

A new CFXMLTree object containing the data from the specified XML data source. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `dataSource`: The URL from which the XML data is obtained. The URL is used to resolve any relative references found in XML Data. Pass `NULL` if a valid URL is unavailable.
- `parseOptions`: Flags which control how the XML data will be parsed. See [`CFXMLParserOptions`](./cfxmlparseroptions.md) for the list of available options.
- `versionOfNodes`: Determines which version of CFXMLNode objects are produced by the parser.

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
- [CFXMLTreeCreateWithNode](./cfxmltreecreatewithnode.md)
  Creates a childless, parentless CFXMLTree object node for a CFXMLNode object.
- [CFXMLTreeCreateXMLData](./cfxmltreecreatexmldata.md)
  Generates an XML document from a CFXMLTree object which is ready to be written to permanent storage.
- [CFXMLTreeGetNode](./cfxmltreegetnode.md)
  Returns the node of a CFXMLTree object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmltreecreatewithdatafromurl)*