# XMLDTDNode.DTDKind

**Framework**: Foundation  
**Kind**: enum

The type defined for the constants that specify the kind and subkind of DTD declaration represented by an `NSXMLDTDNode` object. You set the DTD-node kind using the doc:nsxmldtdnode/1806486-setdtdkind method.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum DTDKind
```

## Topics

### Enumeration Cases
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
- [XMLDTDNode.DTDKind.mixedDeclaration](xmldtdnode/dtdkind-swift.enum/mixeddeclaration.md)
  Identifies a declaration of an element with mixed content (`(#PCDATA | child)`).
- [XMLDTDNode.DTDKind.undefinedDeclaration](xmldtdnode/dtdkind-swift.enum/undefineddeclaration.md)
  Identifies an undefined element declaration.
- [XMLDTDNode.DTDKind.general](xmldtdnode/dtdkind-swift.enum/general.md)
  Identifies a general entity declaration.
- [XMLDTDNode.DTDKind.parameter](xmldtdnode/dtdkind-swift.enum/parameter.md)
  Identifies a parameter entity declaration.
- [XMLDTDNode.DTDKind.parsed](xmldtdnode/dtdkind-swift.enum/parsed.md)
  Identifies a parsed entity declaration.
- [XMLDTDNode.DTDKind.predefined](xmldtdnode/dtdkind-swift.enum/predefined.md)
  Identifies a predefined entity declaration.
- [XMLDTDNode.DTDKind.unparsed](xmldtdnode/dtdkind-swift.enum/unparsed.md)
  Identifies an unparsed entity declaration.
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
- [XMLDTDNode.DTDKind.mixedDeclaration](xmldtdnode/dtdkind-swift.enum/mixeddeclaration.md)
  Identifies a declaration of an element with mixed content (`(#PCDATA | child)`).
- [XMLDTDNode.DTDKind.undefinedDeclaration](xmldtdnode/dtdkind-swift.enum/undefineddeclaration.md)
  Identifies an undefined element declaration.
- [XMLDTDNode.DTDKind.general](xmldtdnode/dtdkind-swift.enum/general.md)
  Identifies a general entity declaration.
- [XMLDTDNode.DTDKind.parameter](xmldtdnode/dtdkind-swift.enum/parameter.md)
  Identifies a parameter entity declaration.
- [XMLDTDNode.DTDKind.parsed](xmldtdnode/dtdkind-swift.enum/parsed.md)
  Identifies a parsed entity declaration.
- [XMLDTDNode.DTDKind.predefined](xmldtdnode/dtdkind-swift.enum/predefined.md)
  Identifies a predefined entity declaration.
- [XMLDTDNode.DTDKind.unparsed](xmldtdnode/dtdkind-swift.enum/unparsed.md)
  Identifies an unparsed entity declaration.
### Initializers
- [init?(rawValue: UInt)](xmldtdnode/dtdkind-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [DTD Node Kind Constants](dtd_node_kind_constants.md)
  Constants that specify the kind and subkind of DTD declaration represented by an `NSXMLDTDNode` object. You set the DTD-node kind using the doc:nsxmldtdnode/1806486-setdtdkind method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtdnode/dtdkind-swift.enum)*