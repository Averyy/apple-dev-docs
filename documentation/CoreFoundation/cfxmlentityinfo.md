# CFXMLEntityInfo

**Framework**: Core Foundation  
**Kind**: struct

Contains information describing an XML entity.

**Availability**:
- macOS ?+

## Declaration

```swift
struct CFXMLEntityInfo
```

#### Overview

A pointer to this structure is included in the CFXMLNode object passed to your application when the parser encounters an entity declaration. Use the [`CFXMLNodeGetInfoPtr`](cfxmlnodegetinfoptr.md) function to obtain a pointer to this structure.

## Topics

### Initializers
- [init()](cfxmlentityinfo/init.md)
- [init(entityType: CFXMLEntityTypeCode, replacementText: Unmanaged<CFString>!, entityID: CFXMLExternalID, notationName: Unmanaged<CFString>!)](cfxmlentityinfo/init(entitytype:replacementtext:entityid:notationname:).md)
### Instance Properties
- [var entityID: CFXMLExternalID](cfxmlentityinfo/entityid.md)
  `entityID.systemID` will be `NULL` if `entityType` is internal.
- [var entityType: CFXMLEntityTypeCode](cfxmlentityinfo/entitytype.md)
  The entity type code.
- [var notationName: Unmanaged<CFString>!](cfxmlentityinfo/notationname.md)
  `NULL` if `entityType` is parsed.
- [var replacementText: Unmanaged<CFString>!](cfxmlentityinfo/replacementtext.md)
  `NULL` if `entityType` is external or unparsed, otherwise the text that the entity should be replaced with.

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
- [struct CFXMLEntityReferenceInfo](cfxmlentityreferenceinfo.md)
  Contains information describing an XML entity reference.
- [struct CFXMLExternalID](cfxmlexternalid.md)
  Contains the system and public IDs for an external entity reference.
- [struct CFXMLNotationInfo](cfxmlnotationinfo.md)
  Contains the external ID of the notation.
- [struct CFXMLProcessingInstructionInfo](cfxmlprocessinginstructioninfo.md)
  Contains the text of the processing instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlentityinfo)*