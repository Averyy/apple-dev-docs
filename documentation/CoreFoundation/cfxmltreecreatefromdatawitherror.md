# CFXMLTreeCreateFromDataWithError

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Parses the given XML data and returns the resulting CFXMLTree object and any error information.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
extern CFXMLTreeRefCFXMLTreeCreateFromDataWithError(CFAllocatorRef allocator, CFDataRef xmlData, CFURLRef dataSource, CFOptionFlags parseOptions, CFIndex versionOfNodes, CFDictionaryRef*errorDict);
```

#### Return Value

A new CFXMLTree object containing the data from the specified XML document. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

Use this function instead of [`CFXMLTreeCreateFromData`](./cfxmltreecreatefromdata.md) if you need access to XML parsing errors.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `xmlData`: The XML data you wish to parse.
- `dataSource`: The URL from which the XML data was obtained. The URL is used to resolve any relative references found in `xmlData`. Pass `NULL` if a valid URL is unavailable.
- `parseOptions`: Flags which control how the XML data will be parsed. See [`CFXMLParserOptions`](./cfxmlparseroptions.md) for the list of available options.
- `versionOfNodes`: Determines which version of CFXMLNode objects are produced by the parser. The current version is 1.
- `errorDict`: Upon return, if an error occurs contains a CFDictionary object that describes the error. If no errors occur, this parameter is not changed. Pass `NULL` if you don’t want error information. See [Error Dictionary Keys](./error-dictionary-keys.md) for a description of the key-value pairs in this dictionary. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### CFXMLTree Miscellaneous Functions
- [func CFXMLCreateStringByEscapingEntities(CFAllocator!, CFString!, CFDictionary!) -> CFString!](./cfxmlcreatestringbyescapingentities%28_,_,_%29.md)
  Given a CFString object containing XML source with unescaped entities, returns a string with specified XML entities escaped.
- [func CFXMLCreateStringByUnescapingEntities(CFAllocator!, CFString!, CFDictionary!) -> CFString!](./cfxmlcreatestringbyunescapingentities%28_,_,_%29.md)
  Given a CFString object containing XML source with escaped entities, returns a string with specified XML entities unescaped.
- [CFXMLTreeCreateFromData](./cfxmltreecreatefromdata.md)
  Parses the given XML data and returns the resulting CFXMLTree object.
- [CFXMLTreeCreateWithDataFromURL](./cfxmltreecreatewithdatafromurl.md)
  Creates a new CFXMLTree object by loading the data to be parsed directly from a data source.
- [CFXMLTreeCreateWithNode](./cfxmltreecreatewithnode.md)
  Creates a childless, parentless CFXMLTree object node for a CFXMLNode object.
- [CFXMLTreeCreateXMLData](./cfxmltreecreatexmldata.md)
  Generates an XML document from a CFXMLTree object which is ready to be written to permanent storage.
- [CFXMLTreeGetNode](./cfxmltreegetnode.md)
  Returns the node of a CFXMLTree object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmltreecreatefromdatawitherror)*