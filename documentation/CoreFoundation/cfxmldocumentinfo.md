# CFXMLDocumentInfo

**Framework**: Core Foundation  
**Kind**: struct

Contains the source URL and text encoding information for the XML document.

**Availability**:
- macOS ?+

## Declaration

```swift
struct CFXMLDocumentInfo
```

#### Overview

A pointer to this structure is included in the CFXMLNode object passed to your application when the parser encounters the XML declaration. Use the [`CFXMLNodeGetInfoPtr`](cfxmlnodegetinfoptr.md) function to obtain the pointer.

## Topics

### Initializers
- [init()](cfxmldocumentinfo/init.md)
- [init(sourceURL: Unmanaged<CFURL>!, encoding: CFStringEncoding)](cfxmldocumentinfo/init(sourceurl:encoding:).md)
### Instance Properties
- [var encoding: CFStringEncoding](cfxmldocumentinfo/encoding.md)
  The text encoding of the XML document.
- [var sourceURL: Unmanaged<CFURL>!](cfxmldocumentinfo/sourceurl.md)
  The source URL of the XML document.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct CFXMLAttributeDeclarationInfo](cfxmlattributedeclarationinfo.md)
  Contains information about an element attribute definition.
- [struct CFXMLAttributeListDeclarationInfo](cfxmlattributelistdeclarationinfo.md)
  Contains a list of the attributes associated with an element.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmldocumentinfo)*