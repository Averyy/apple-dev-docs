# CFXMLEntityReferenceInfo

**Framework**: Core Foundation  
**Kind**: struct

Contains information describing an XML entity reference.

**Availability**:
- macOS ?+

## Declaration

```swift
struct CFXMLEntityReferenceInfo
```

#### Overview

A pointer to this structure is included in the CFXMLNode object passed to your application when the parser encounters an entity reference. Use the [`CFXMLNodeGetInfoPtr`](cfxmlnodegetinfoptr.md) function to obtain the pointer.

## Topics

### Initializers
- [init()](cfxmlentityreferenceinfo/init.md)
- [init(entityType: CFXMLEntityTypeCode)](cfxmlentityreferenceinfo/init(entitytype:).md)
### Instance Properties
- [var entityType: CFXMLEntityTypeCode](cfxmlentityreferenceinfo/entitytype.md)
  The entity type code.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

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
- [struct CFXMLExternalID](cfxmlexternalid.md)
  Contains the system and public IDs for an external entity reference.
- [struct CFXMLNotationInfo](cfxmlnotationinfo.md)
  Contains the external ID of the notation.
- [struct CFXMLProcessingInstructionInfo](cfxmlprocessinginstructioninfo.md)
  Contains the text of the processing instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlentityreferenceinfo)*