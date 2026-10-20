# CFXMLNodeTypeCode.attribute

**Framework**: Core Foundation  
**Kind**: case  
**Role**: Case

Currently not used.

**Availability**:
- macOS

## Declaration

```swift
case attribute
```

```c
kCFXMLNodeTypeAttribute
```

## See Also

### Constants
- [CFXMLNodeTypeCode.document](./document.md)
  Indicates a document where the data string is `NULL` and the additional information is a pointer to a [`CFXMLDocumentInfo`](../cfxmldocumentinfo.md) structure.
- [CFXMLNodeTypeCode.element](./element.md)
  Indicates an element where the data string is the name of the tag and the additional information is a pointer to a [`CFXMLElementInfo`](../cfxmlelementinfo.md) structure.
- [CFXMLNodeTypeCode.processingInstruction](./processinginstruction.md)
  Indicates a processing instruction where the data string is the name of the target and the additional information is a pointer to a [`CFXMLProcessingInstructionInfo`](../cfxmlprocessinginstructioninfo.md) structure.
- [CFXMLNodeTypeCode.comment](./comment.md)
  Indicates a comment section where the data string is the text of the comment and the additional information is `NULL`.
- [CFXMLNodeTypeCode.text](./text.md)
  Indicates a text section where the data string is the text’s contents and the additional information is `NULL`.
- [CFXMLNodeTypeCode.cdataSection](./cdatasection.md)
  Indicates a CDATA section where the data string is the text of the CDATA and the additional information is `NULL`.
- [CFXMLNodeTypeCode.documentFragment](./documentfragment.md)
  Currently not used.
- [CFXMLNodeTypeCode.entity](./entity.md)
  Indicates an entity where the data string is the name of the entity and the additional information is a pointer to a [`CFXMLEntityInfo`](../cfxmlentityinfo.md) structure.
- [CFXMLNodeTypeCode.entityReference](./entityreference.md)
  Indicates an entity reference where the data string is the name of the referenced entity and the additional information is a pointer to a [`CFXMLEntityReferenceInfo`](../cfxmlentityreferenceinfo.md) structure.
- [CFXMLNodeTypeCode.documentType](./documenttype.md)
  Indicates a document type where the data string is the name given to the top-level element and the additional information is a pointer to a [`CFXMLDocumentTypeInfo`](../cfxmldocumenttypeinfo.md) structure.
- [CFXMLNodeTypeCode.whitespace](./whitespace.md)
  Indicates white space where the data string is the text of the white space and the additional information is `NULL`.
- [CFXMLNodeTypeCode.notation](./notation.md)
  Indicates a notation where the data string is the notation name and the additional information is a pointer to a [`CFXMLNotationInfo`](../cfxmlnotationinfo.md) structure.
- [CFXMLNodeTypeCode.elementTypeDeclaration](./elementtypedeclaration.md)
  Indicates an element type declaration where the data string is the tag name and the additional information is a pointer to a [`CFXMLElementTypeDeclarationInfo`](../cfxmlelementtypedeclarationinfo.md) structure.
- [CFXMLNodeTypeCode.attributeListDeclaration](./attributelistdeclaration.md)
  Indicates an attribute list declaration where the data string is the tag name and the additional information is a pointer to a [`CFXMLAttributeListDeclarationInfo`](../cfxmlattributelistdeclarationinfo.md) structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlnodetypecode/attribute)*