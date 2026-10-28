# CFXMLTreeCreateFromData

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Parses the given XML data and returns the resulting CFXMLTree object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
extern CFXMLTreeRefCFXMLTreeCreateFromData(CFAllocatorRef allocator, CFDataRef xmlData, CFURLRef dataSource, CFOptionFlags parseOptions, CFIndex versionOfNodes);
```

## Return Value

A new CFXMLTree object containing the data from the specified XML document. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function represents the high-level interface to the XML parser. This single function creates a parser for the specified XML data using the specified options. The parser creates and returns a CFXMLTree object that you can examine and modify with the CFTree functions or obtain the node using the [`CFXMLTreeGetNode`](./cfxmltreegetnode.md) function and examine its attributes using CFXMLNode functions.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `xmlData`: The XML data you wish to parse.
- `dataSource`: The URL from which the XML data was obtained. The URL is used to resolve any relative references found in `xmlData`. Pass `NULL` if a valid URL is unavailable.
- `parseOptions`: Flags which control how the XML data will be parsed. See [`CFXMLParserOptions`](./cfxmlparseroptions.md) for the list of available options.
- `versionOfNodes`: Determines which version of CFXMLNode objects are produced by the parser.

## See Also

### CFXMLTree Miscellaneous Functions
- [func CFXMLCreateStringByEscapingEntities(CFAllocator!, CFString!, CFDictionary!) -> CFString!](./cfxmlcreatestringbyescapingentities%28_,_,_%29.md)
  Given a CFString object containing XML source with unescaped entities, returns a string with specified XML entities escaped.
- [func CFXMLCreateStringByUnescapingEntities(CFAllocator!, CFString!, CFDictionary!) -> CFString!](./cfxmlcreatestringbyunescapingentities%28_,_,_%29.md)
  Given a CFString object containing XML source with escaped entities, returns a string with specified XML entities unescaped.
- [CFXMLTreeCreateFromDataWithError](./cfxmltreecreatefromdatawitherror.md)
  Parses the given XML data and returns the resulting CFXMLTree object and any error information.
- [CFXMLTreeCreateWithDataFromURL](./cfxmltreecreatewithdatafromurl.md)
  Creates a new CFXMLTree object by loading the data to be parsed directly from a data source.
- [CFXMLTreeCreateWithNode](./cfxmltreecreatewithnode.md)
  Creates a childless, parentless CFXMLTree object node for a CFXMLNode object.
- [CFXMLTreeCreateXMLData](./cfxmltreecreatexmldata.md)
  Generates an XML document from a CFXMLTree object which is ready to be written to permanent storage.
- [CFXMLTreeGetNode](./cfxmltreegetnode.md)
  Returns the node of a CFXMLTree object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmltreecreatefromdata)*