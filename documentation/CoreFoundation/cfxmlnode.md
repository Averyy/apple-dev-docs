# CFXMLNode

**Framework**: Core Foundation  
**Kind**: class

**Availability**:
- macOS ?+

## Declaration

```swift
class CFXMLNode
```

#### Overview

A CFXMLNode object describes an individual XML construct—like a tag, or a comment, or a string of character data. CFXMLNode is intended to be used with the CFXMLParser and CFXMLTree opaque types.

Each CFXMLNode object contains three main pieces of information—the node’s type, the data string, and a pointer to an additional information data structure. A CFXMLNode object’s type is one of the enumerations described in [`CFXMLNodeTypeCode`](cfxmlnodetypecode.md). The data string is always a CFString object; the meaning of the string is dependent on the node’s type. The format of the additional data is also dependent on the node’s type; in general, there is a custom structure for each type that requires additional data. See [`CFXMLNodeTypeCode`](cfxmlnodetypecode.md) for the mapping from a node type to meaning of the data string, and structure of the additional information. Note that these structures are versioned and may change as the parser changes. The current version can always be identified by the [`kCFXMLNodeCurrentVersion`](kcfxmlnodecurrentversion.md) constant; earlier versions can be identified and used by passing earlier values for the version number (although the older structures would have been removed from the header).

You create a CFXMLNode object using one of the create or copy functions. Use the [`CFXMLNodeGetTypeCode`](cfxmlnodegettypecode.md), [`CFXMLNodeGetString`](cfxmlnodegetstring.md), and [`CFXMLNodeGetInfoPtr`](cfxmlnodegetinfoptr.md) functions to get the node type, data string, and additional information respectively. Use the [`CFXMLNodeGetVersion`](cfxmlnodegetversion.md) function to get a node’s version number.

## Topics

### Data Types
- [struct CFXMLAttributeDeclarationInfo](cfxmlattributedeclarationinfo.md)
  Contains information about an element attribute definition.
- [struct CFXMLAttributeListDeclarationInfo](cfxmlattributelistdeclarationinfo.md)
  Contains a list of the attributes associated with an element.
- [struct CFXMLDocumentInfo](cfxmldocumentinfo.md)
  Contains the source URL and text encoding information for the XML document.
- [struct CFXMLDocumentTypeInfo](cfxmldocumenttypeinfo.md)
  Contains the external ID of the DTD.
- [struct CFXMLElementInfo](cfxmlelementinfo.md)
  Contains a list of element attributes packaged as CFDictionary key/value pairs.
- [struct CFXMLElementTypeDeclarationInfo](cfxmlelementtypedeclarationinfo.md)
  Contains a description of the element type.
- [struct CFXMLEntityInfo](cfxmlentityinfo.md)
  Contains information describing an XML entity.
- [struct CFXMLEntityReferenceInfo](cfxmlentityreferenceinfo.md)
  Contains information describing an XML entity reference.
- [struct CFXMLExternalID](cfxmlexternalid.md)
  Contains the system and public IDs for an external entity reference.
- [struct CFXMLNotationInfo](cfxmlnotationinfo.md)
  Contains the external ID of the notation.
- [struct CFXMLProcessingInstructionInfo](cfxmlprocessinginstructioninfo.md)
  Contains the text of the processing instruction.
### Constants
- [enum CFXMLEntityTypeCode](cfxmlentitytypecode.md)
  The entity type identification codes that the parser uses to describe XML entities.
- [Node Current Version](1443311-node-current-version.md)
  The version of a CFXMLNode object.
- [enum CFXMLNodeTypeCode](cfxmlnodetypecode.md)
  The various XML data type identification codes that the parser uses to describe XML structures.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [XML Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFXML/CFXML.html#//apple_ref/doc/uid/10000138i)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlnode)*