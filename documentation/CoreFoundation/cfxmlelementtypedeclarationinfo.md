# CFXMLElementTypeDeclarationInfo

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

Contains a description of the element type.

**Availability**:
- macOS

## Declaration

```swift
struct CFXMLElementTypeDeclarationInfo
```

```c
typedef struct { ... } CFXMLElementTypeDeclarationInfo;
```

#### Overview

A pointer to this structure is included in the CFXMLNode passed to your application when the parser encounters and element type declaration. Use the [`CFXMLNodeGetInfoPtr`](./cfxmlnodegetinfoptr.md) function to obtain a pointer to this structure.

## Topics

### Initializers
- [init()](./cfxmlelementtypedeclarationinfo/init%28%29.md)
- [init(contentDescription: Unmanaged<CFString>!)](./cfxmlelementtypedeclarationinfo/init%28contentdescription%29.md)
### Instance Properties
- [var contentDescription: Unmanaged<CFString>!](./cfxmlelementtypedeclarationinfo/contentdescription.md)
  A textual description of the element type.

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
- [struct CFXMLEntityInfo](./cfxmlentityinfo.md)
  Contains information describing an XML entity.
- [struct CFXMLEntityReferenceInfo](./cfxmlentityreferenceinfo.md)
  Contains information describing an XML entity reference.
- [struct CFXMLExternalID](./cfxmlexternalid.md)
  Contains the system and public IDs for an external entity reference.
- [struct CFXMLNotationInfo](./cfxmlnotationinfo.md)
  Contains the external ID of the notation.
- [struct CFXMLProcessingInstructionInfo](./cfxmlprocessinginstructioninfo.md)
  Contains the text of the processing instruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlelementtypedeclarationinfo)*