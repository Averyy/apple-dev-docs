# XMLDTDNode.DTDKind.general

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

Identifies a general entity declaration.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
case general
```

```c
NSXMLEntityGeneralKind
```

## See Also

### Enumeration Cases
- [XMLDTDNode.DTDKind.cdataAttribute](./cdataattribute.md)
  Identifies an attribute-list declaration with a `CDATA` (character data) value type.
- [XMLDTDNode.DTDKind.entitiesAttribute](./entitiesattribute.md)
  Identifies an attribute-list declaration with an `ENTITIES` value type (refers to multiple unparsed entities declared elsewhere in document).
- [XMLDTDNode.DTDKind.entityAttribute](./entityattribute.md)
  Identifies an attribute-list declaration with an `ENTITY` value type (refers to unparsed entity declared in document).
- [XMLDTDNode.DTDKind.enumerationAttribute](./enumerationattribute.md)
  Identifies an attribute-list declaration with an enumeration value type (list of all possible values).
- [XMLDTDNode.DTDKind.idAttribute](./idattribute.md)
  Identifies an attribute-list declaration with an `ID` value type (per-document unique element name).
- [XMLDTDNode.DTDKind.idRefAttribute](./idrefattribute.md)
  Identifies an attribute-list declaration with an `IDREF` value type (refers to element `ID` type).
- [XMLDTDNode.DTDKind.idRefsAttribute](./idrefsattribute.md)
  Identifies an attribute-list declaration with an `IDREFS` value type (refers to multiple elements of `ID` type).
- [XMLDTDNode.DTDKind.nmTokenAttribute](./nmtokenattribute.md)
  Identifies an attribute-list declaration with a `NMTOKEN` value type (name token).
- [XMLDTDNode.DTDKind.nmTokensAttribute](./nmtokensattribute.md)
  Identifies an attribute-list declaration with a `NMTOKENS` value type (multiple name tokens)
- [XMLDTDNode.DTDKind.notationAttribute](./notationattribute.md)
  Identifies an attribute-list declaration with a `NOTATION` value type (name of declared notation).
- [XMLDTDNode.DTDKind.anyDeclaration](./anydeclaration.md)
  Identifies an `ANY` element declaration.
- [XMLDTDNode.DTDKind.elementDeclaration](./elementdeclaration.md)
  Identifies a declaration of an element with child elements.
- [XMLDTDNode.DTDKind.emptyDeclaration](./emptydeclaration.md)
  Identifies a declaration (`EMPTY`) of an empty element.
- [XMLDTDNode.DTDKind.mixedDeclaration](./mixeddeclaration.md)
  Identifies a declaration of an element with mixed content (`(#PCDATA | child)`).
- [XMLDTDNode.DTDKind.undefinedDeclaration](./undefineddeclaration.md)
  Identifies an undefined element declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtdnode/dtdkind-swift.enum/general)*