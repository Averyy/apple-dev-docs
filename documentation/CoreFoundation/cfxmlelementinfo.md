# CFXMLElementInfo

**Framework**: Core Foundation  
**Kind**: struct

Contains a list of element attributes packaged as CFDictionary key/value pairs.

**Availability**:
- macOS ?+

## Declaration

```swift
struct CFXMLElementInfo
```

#### Overview

A pointer to this structure is included in the CFXMLNode object passed to your application when the parser encounters an element containing attributes. Use the [`CFXMLNodeGetInfoPtr`](cfxmlnodegetinfoptr.md) function to obtain the pointer.

## Topics

### Initializers
- [init()](cfxmlelementinfo/init.md)
### Instance Properties
- [var attributeOrder: Unmanaged<CFArray>!](cfxmlelementinfo/attributeorder.md)
  An array specifying the order in which the attributes appeared in the XML document.
- [var attributes: Unmanaged<CFDictionary>!](cfxmlelementinfo/attributes.md)
  The dictionary of attribute values.
- [var isEmpty: DarwinBoolean](cfxmlelementinfo/isempty.md)
  A flag indicating whether the element was expressed in closed form.

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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlelementinfo)*