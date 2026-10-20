# CFXMLProcessingInstructionInfo

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

Contains the text of the processing instruction.

**Availability**:
- macOS

## Declaration

```swift
struct CFXMLProcessingInstructionInfo
```

```c
typedef struct { ... } CFXMLProcessingInstructionInfo;
```

#### Overview

A pointer to this structure is included in the CFXMLNode object passed to your application when the parser encounters a processing instruction. Use the [`CFXMLNodeGetInfoPtr`](./cfxmlnodegetinfoptr.md) function to obtain the pointer.

## Topics

### Initializers
- [init()](./cfxmlprocessinginstructioninfo/init%28%29.md)
- [init(dataString: Unmanaged<CFString>!)](./cfxmlprocessinginstructioninfo/init%28datastring%29.md)
### Instance Properties
- [var dataString: Unmanaged<CFString>!](./cfxmlprocessinginstructioninfo/datastring.md)
  The text of the processing instruction.

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
- [struct CFXMLNotationInfo](./cfxmlnotationinfo.md)
  Contains the external ID of the notation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlprocessinginstructioninfo)*