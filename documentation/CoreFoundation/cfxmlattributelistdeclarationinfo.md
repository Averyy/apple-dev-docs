# CFXMLAttributeListDeclarationInfo

**Framework**: Core Foundation  
**Kind**: struct

Contains a list of the attributes associated with an element.

**Availability**:
- macOS ?+

## Declaration

```swift
struct CFXMLAttributeListDeclarationInfo
```

#### Overview

A pointer to this structure is included in the CFXMLNode object passed to your application when the parser encounters an attribute declaration in the DTD. Use the [`CFXMLNodeGetInfoPtr`](cfxmlnodegetinfoptr.md) function to obtain the pointer to this structure.

## Topics

### Initializers
- [init()](cfxmlattributelistdeclarationinfo/init.md)
- [init(numberOfAttributes: CFIndex, attributes: UnsafeMutablePointer<CFXMLAttributeDeclarationInfo>!)](cfxmlattributelistdeclarationinfo/init(numberofattributes:attributes:).md)
### Instance Properties
- [var attributes: UnsafeMutablePointer<CFXMLAttributeDeclarationInfo>!](cfxmlattributelistdeclarationinfo/attributes.md)
  A C array of attributes.
- [var numberOfAttributes: CFIndex](cfxmlattributelistdeclarationinfo/numberofattributes.md)
  The number of attributes in the array.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct CFXMLAttributeDeclarationInfo](cfxmlattributedeclarationinfo.md)
  Contains information about an element attribute definition.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlattributelistdeclarationinfo)*