# CFXMLNotationInfo

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

Contains the external ID of the notation.

**Availability**:
- macOS

## Declaration

```swift
struct CFXMLNotationInfo
```

```c
typedef struct { ... } CFXMLNotationInfo;
```

## Overview

A pointer to this structure is included in the CFXMLNode object passed to your application when the parser encounters a notation element. Use the [`CFXMLNodeGetInfoPtr`](./cfxmlnodegetinfoptr.md) function to obtain a pointer to this structure.

## Topics

### Initializers
- [init()](./cfxmlnotationinfo/init%28%29.md)
- [init(externalID: CFXMLExternalID)](./cfxmlnotationinfo/init%28externalid%29.md)
### Instance Properties
- [var externalID: CFXMLExternalID](./cfxmlnotationinfo/externalid.md)
  The external ID of the notation.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Data Types
- [struct CFXMLAttributeDeclarationInfo](./cfxmlattributedeclarationinfo.md)
  Contains information about an element attribute definition.
- [struct CFXMLAttributeListDeclarationInfo](./cfxmlattributelistdeclarationinfo.md)
  Contains a list of the attributes associated with an element.
- [struct CFXMLDocumentInfo](./cfxmldocumentinfo.md)
  Contains the source URL and text encoding information for the XML document.
- [struct CFXMLDocumentTypeInfo](./cfxmldocumenttypeinfo.md)
  Contains the external ID of the DTD.
- [struct CFXMLElementInfo](./cfxmlelementinfo.md)
  Contains a list of element attributes packaged as CFDictionary key/value pairs.
- [struct CFXMLElementTypeDeclarationInfo](./cfxmlelementtypedeclarationinfo.md)
  Contains a description of the element type.
- [struct CFXMLEntityInfo](./cfxmlentityinfo.md)
  Contains information describing an XML entity.
- [struct CFXMLEntityReferenceInfo](./cfxmlentityreferenceinfo.md)
  Contains information describing an XML entity reference.
- [struct CFXMLExternalID](./cfxmlexternalid.md)
  Contains the system and public IDs for an external entity reference.
- [struct CFXMLProcessingInstructionInfo](./cfxmlprocessinginstructioninfo.md)
  Contains the text of the processing instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlnotationinfo)*