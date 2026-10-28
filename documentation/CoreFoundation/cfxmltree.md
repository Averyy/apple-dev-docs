# CFXMLTree

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias CFXMLTree = CFTree
```

```c
typedef CFTreeRef CFXMLTreeRef;
```

## Overview

A CFXMLTree object is simply a CFTree object whose context data is known to be a CFXMLNode object. CFXMLTree is derived from CFTree—you can pass CFXMLTree objects in all the CFTree functions. As such, a CFXMLTree object can be used to represent an entire XML document; the CFTree object provides the tree structure of the document, while the CFXMLNode objects identify and describe the nodes of the tree. An XML document can be parsed to a CFXMLTree object, and a CFXMLTree object can generate the data for the equivalent XML document. This opaque type is expected to be used in conjunction with CFXMLParser and CFXMLNode objects.

## Topics

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
- [CFXMLTreeGetNode](./cfxmltreegetnode.md)
  Returns the node of a CFXMLTree object.
### Constants
- [Error Dictionary Keys](./error-dictionary-keys.md)
  The keys used in an error dictionary returned by some functions to provide more information about XML parse errors.

## See Also

### Related Documentation
- [XML Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFXML/CFXML.html#//apple_ref/doc/uid/10000138i)
### Opaque Types
- [class CFAllocator](./cfallocator.md)
- [class CFArray](./cfarray.md)
- [class CFAttributedString](./cfattributedstring.md)
- [class CFBag](./cfbag.md)
- [class CFBinaryHeap](./cfbinaryheap.md)
- [class CFBitVector](./cfbitvector.md)
- [class CFBoolean](./cfboolean.md)
- [class CFBundle](./cfbundle.md)
- [class CFCalendar](./cfcalendar.md)
- [class CFCharacterSet](./cfcharacterset.md)
- [class CFData](./cfdata.md)
- [class CFDate](./cfdate.md)
- [class CFDateFormatter](./cfdateformatter.md)
- [class CFDictionary](./cfdictionary.md)
- [class CFError](./cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmltree)*