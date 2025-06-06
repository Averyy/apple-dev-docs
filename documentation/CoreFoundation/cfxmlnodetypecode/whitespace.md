# CFXMLNodeTypeCode.whitespace

**Framework**: Core Foundation  
**Kind**: case

Indicates white space where the data string is the text of the white space and the additional information is `NULL`.

**Availability**:
- macOS ?+

## Declaration

```swift
case whitespace
```

## See Also

- [CFXMLNodeTypeCode.document](cfxmlnodetypecode/document.md)
  Indicates a document where the data string is `NULL` and the additional information is a pointer to a [`CFXMLDocumentInfo`](cfxmldocumentinfo.md) structure.
- [CFXMLNodeTypeCode.element](cfxmlnodetypecode/element.md)
  Indicates an element where the data string is the name of the tag and the additional information is a pointer to a [`CFXMLElementInfo`](cfxmlelementinfo.md) structure.
- [CFXMLNodeTypeCode.attribute](cfxmlnodetypecode/attribute.md)
  Currently not used.
- [CFXMLNodeTypeCode.processingInstruction](cfxmlnodetypecode/processinginstruction.md)
  Indicates a processing instruction where the data string is the name of the target and the additional information is a pointer to a [`CFXMLProcessingInstructionInfo`](cfxmlprocessinginstructioninfo.md) structure.
- [CFXMLNodeTypeCode.comment](cfxmlnodetypecode/comment.md)
  Indicates a comment section where the data string is the text of the comment and the additional information is `NULL`.
- [CFXMLNodeTypeCode.text](cfxmlnodetypecode/text.md)
  Indicates a text section where the data string is the text’s contents and the additional information is `NULL`.
- [CFXMLNodeTypeCode.cdataSection](cfxmlnodetypecode/cdatasection.md)
  Indicates a CDATA section where the data string is the text of the CDATA and the additional information is `NULL`.
- [CFXMLNodeTypeCode.documentFragment](cfxmlnodetypecode/documentfragment.md)
  Currently not used.
- [CFXMLNodeTypeCode.entity](cfxmlnodetypecode/entity.md)
  Indicates an entity where the data string is the name of the entity and the additional information is a pointer to a [`CFXMLEntityInfo`](cfxmlentityinfo.md) structure.
- [CFXMLNodeTypeCode.entityReference](cfxmlnodetypecode/entityreference.md)
  Indicates an entity reference where the data string is the name of the referenced entity and the additional information is a pointer to a [`CFXMLEntityReferenceInfo`](cfxmlentityreferenceinfo.md) structure.
- [CFXMLNodeTypeCode.documentType](cfxmlnodetypecode/documenttype.md)
  Indicates a document type where the data string is the name given to the top-level element and the additional information is a pointer to a [`CFXMLDocumentTypeInfo`](cfxmldocumenttypeinfo.md) structure.
- [CFXMLNodeTypeCode.notation](cfxmlnodetypecode/notation.md)
  Indicates a notation where the data string is the notation name and the additional information is a pointer to a [`CFXMLNotationInfo`](cfxmlnotationinfo.md) structure.
- [CFXMLNodeTypeCode.elementTypeDeclaration](cfxmlnodetypecode/elementtypedeclaration.md)
  Indicates an element type declaration where the data string is the tag name and the additional information is a pointer to a [`CFXMLElementTypeDeclarationInfo`](cfxmlelementtypedeclarationinfo.md) structure.
- [CFXMLNodeTypeCode.attributeListDeclaration](cfxmlnodetypecode/attributelistdeclaration.md)
  Indicates an attribute list declaration where the data string is the tag name and the additional information is a pointer to a [`CFXMLAttributeListDeclarationInfo`](cfxmlattributelistdeclarationinfo.md) structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlnodetypecode/whitespace)*