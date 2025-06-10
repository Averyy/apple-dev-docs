# XMLDTDNode.DTDKind.mixedDeclaration

**Framework**: Foundation  
**Kind**: case

Identifies a declaration of an element with mixed content (`(#PCDATA | child)`).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
case mixedDeclaration
```

## See Also

- [XMLDTDNode.DTDKind.cdataAttribute](xmldtdnode/dtdkind-swift.enum/cdataattribute.md)
  Identifies an attribute-list declaration with a `CDATA` (character data) value type.
- [XMLDTDNode.DTDKind.entitiesAttribute](xmldtdnode/dtdkind-swift.enum/entitiesattribute.md)
  Identifies an attribute-list declaration with an `ENTITIES` value type (refers to multiple unparsed entities declared elsewhere in document).
- [XMLDTDNode.DTDKind.entityAttribute](xmldtdnode/dtdkind-swift.enum/entityattribute.md)
  Identifies an attribute-list declaration with an `ENTITY` value type (refers to unparsed entity declared in document).
- [XMLDTDNode.DTDKind.enumerationAttribute](xmldtdnode/dtdkind-swift.enum/enumerationattribute.md)
  Identifies an attribute-list declaration with an enumeration value type (list of all possible values).
- [XMLDTDNode.DTDKind.idAttribute](xmldtdnode/dtdkind-swift.enum/idattribute.md)
  Identifies an attribute-list declaration with an `ID` value type (per-document unique element name).
- [XMLDTDNode.DTDKind.idRefAttribute](xmldtdnode/dtdkind-swift.enum/idrefattribute.md)
  Identifies an attribute-list declaration with an `IDREF` value type (refers to element `ID` type).
- [XMLDTDNode.DTDKind.idRefsAttribute](xmldtdnode/dtdkind-swift.enum/idrefsattribute.md)
  Identifies an attribute-list declaration with an `IDREFS` value type (refers to multiple elements of `ID` type).
- [XMLDTDNode.DTDKind.nmTokenAttribute](xmldtdnode/dtdkind-swift.enum/nmtokenattribute.md)
  Identifies an attribute-list declaration with a `NMTOKEN` value type (name token).
- [XMLDTDNode.DTDKind.nmTokensAttribute](xmldtdnode/dtdkind-swift.enum/nmtokensattribute.md)
  Identifies an attribute-list declaration with a `NMTOKENS` value type (multiple name tokens)
- [XMLDTDNode.DTDKind.notationAttribute](xmldtdnode/dtdkind-swift.enum/notationattribute.md)
  Identifies an attribute-list declaration with a `NOTATION` value type (name of declared notation).
- [XMLDTDNode.DTDKind.anyDeclaration](xmldtdnode/dtdkind-swift.enum/anydeclaration.md)
  Identifies an `ANY` element declaration.
- [XMLDTDNode.DTDKind.elementDeclaration](xmldtdnode/dtdkind-swift.enum/elementdeclaration.md)
  Identifies a declaration of an element with child elements.
- [XMLDTDNode.DTDKind.emptyDeclaration](xmldtdnode/dtdkind-swift.enum/emptydeclaration.md)
  Identifies a declaration (`EMPTY`) of an empty element.
- [XMLDTDNode.DTDKind.undefinedDeclaration](xmldtdnode/dtdkind-swift.enum/undefineddeclaration.md)
  Identifies an undefined element declaration.
- [XMLDTDNode.DTDKind.general](xmldtdnode/dtdkind-swift.enum/general.md)
  Identifies a general entity declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtdnode/dtdkind-swift.enum/mixeddeclaration)*