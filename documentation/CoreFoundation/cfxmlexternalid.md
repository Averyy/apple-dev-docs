# CFXMLExternalID

**Framework**: Core Foundation  
**Kind**: struct

Contains the system and public IDs for an external entity reference.

**Availability**:
- macOS ?+

## Declaration

```swift
struct CFXMLExternalID
```

#### Overview

This structure is part of the definition of the [`CFXMLDocumentTypeInfo`](cfxmldocumenttypeinfo.md), [`CFXMLNotationInfo`](cfxmlnotationinfo.md), and [`CFXMLEntityInfo`](cfxmlentityinfo.md) structures.

## Topics

### Initializers
- [init()](cfxmlexternalid/init.md)
- [init(systemID: Unmanaged<CFURL>!, publicID: Unmanaged<CFString>!)](cfxmlexternalid/init(systemid:publicid:).md)
### Instance Properties
- [var publicID: Unmanaged<CFString>!](cfxmlexternalid/publicid.md)
  The publicID string.
- [var systemID: Unmanaged<CFURL>!](cfxmlexternalid/systemid.md)
  The systemID URL.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

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
- [struct CFXMLNotationInfo](cfxmlnotationinfo.md)
  Contains the external ID of the notation.
- [struct CFXMLProcessingInstructionInfo](cfxmlprocessinginstructioninfo.md)
  Contains the text of the processing instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlexternalid)*