# CFXMLAttributeDeclarationInfo

**Framework**: Core Foundation  
**Kind**: struct

Contains information about an element attribute definition.

**Availability**:
- macOS ?+

## Declaration

```swift
struct CFXMLAttributeDeclarationInfo
```

#### Overview

This structure is part of the definition of the [`CFXMLAttributeListDeclarationInfo`](cfxmlattributelistdeclarationinfo.md) structure.

## Topics

### Initializers
- [init()](cfxmlattributedeclarationinfo/init.md)
- [init(attributeName: Unmanaged<CFString>!, typeString: Unmanaged<CFString>!, defaultString: Unmanaged<CFString>!)](cfxmlattributedeclarationinfo/init(attributename:typestring:defaultstring:).md)
### Instance Properties
- [var attributeName: Unmanaged<CFString>!](cfxmlattributedeclarationinfo/attributename.md)
  The name of the attribute.
- [var defaultString: Unmanaged<CFString>!](cfxmlattributedeclarationinfo/defaultstring.md)
  The attribute’s default value.
- [var typeString: Unmanaged<CFString>!](cfxmlattributedeclarationinfo/typestring.md)
  Describes the declaration of a single attribute.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlattributedeclarationinfo)*