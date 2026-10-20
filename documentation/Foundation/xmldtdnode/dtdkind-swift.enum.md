# XMLDTDNode.DTDKind

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

The type defined for the constants that specify the kind and subkind of DTD declaration represented by an `NSXMLDTDNode` object. You set the DTD-node kind using the doc:nsxmldtdnode/1806486-setdtdkind method.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum DTDKind
```

```c
enum NSXMLDTDNodeKind : NSUInteger;
```

## Topics

### Enumeration Cases
- [XMLDTDNode.DTDKind.cdataAttribute](./dtdkind-swift.enum/cdataattribute.md)
  Identifies an attribute-list declaration with a `CDATA` (character data) value type.
- [XMLDTDNode.DTDKind.entitiesAttribute](./dtdkind-swift.enum/entitiesattribute.md)
  Identifies an attribute-list declaration with an `ENTITIES` value type (refers to multiple unparsed entities declared elsewhere in document).
- [XMLDTDNode.DTDKind.entityAttribute](./dtdkind-swift.enum/entityattribute.md)
  Identifies an attribute-list declaration with an `ENTITY` value type (refers to unparsed entity declared in document).
- [XMLDTDNode.DTDKind.enumerationAttribute](./dtdkind-swift.enum/enumerationattribute.md)
  Identifies an attribute-list declaration with an enumeration value type (list of all possible values).
- [XMLDTDNode.DTDKind.idAttribute](./dtdkind-swift.enum/idattribute.md)
  Identifies an attribute-list declaration with an `ID` value type (per-document unique element name).
- [XMLDTDNode.DTDKind.idRefAttribute](./dtdkind-swift.enum/idrefattribute.md)
  Identifies an attribute-list declaration with an `IDREF` value type (refers to element `ID` type).
- [XMLDTDNode.DTDKind.idRefsAttribute](./dtdkind-swift.enum/idrefsattribute.md)
  Identifies an attribute-list declaration with an `IDREFS` value type (refers to multiple elements of `ID` type).
- [XMLDTDNode.DTDKind.nmTokenAttribute](./dtdkind-swift.enum/nmtokenattribute.md)
  Identifies an attribute-list declaration with a `NMTOKEN` value type (name token).
- [XMLDTDNode.DTDKind.nmTokensAttribute](./dtdkind-swift.enum/nmtokensattribute.md)
  Identifies an attribute-list declaration with a `NMTOKENS` value type (multiple name tokens)
- [XMLDTDNode.DTDKind.notationAttribute](./dtdkind-swift.enum/notationattribute.md)
  Identifies an attribute-list declaration with a `NOTATION` value type (name of declared notation).
- [XMLDTDNode.DTDKind.anyDeclaration](./dtdkind-swift.enum/anydeclaration.md)
  Identifies an `ANY` element declaration.
- [XMLDTDNode.DTDKind.elementDeclaration](./dtdkind-swift.enum/elementdeclaration.md)
  Identifies a declaration of an element with child elements.
- [XMLDTDNode.DTDKind.emptyDeclaration](./dtdkind-swift.enum/emptydeclaration.md)
  Identifies a declaration (`EMPTY`) of an empty element.
- [XMLDTDNode.DTDKind.mixedDeclaration](./dtdkind-swift.enum/mixeddeclaration.md)
  Identifies a declaration of an element with mixed content (`(#PCDATA | child)`).
- [XMLDTDNode.DTDKind.undefinedDeclaration](./dtdkind-swift.enum/undefineddeclaration.md)
  Identifies an undefined element declaration.
- [XMLDTDNode.DTDKind.general](./dtdkind-swift.enum/general.md)
  Identifies a general entity declaration.
- [XMLDTDNode.DTDKind.parameter](./dtdkind-swift.enum/parameter.md)
  Identifies a parameter entity declaration.
- [XMLDTDNode.DTDKind.parsed](./dtdkind-swift.enum/parsed.md)
  Identifies a parsed entity declaration.
- [XMLDTDNode.DTDKind.predefined](./dtdkind-swift.enum/predefined.md)
  Identifies a predefined entity declaration.
- [XMLDTDNode.DTDKind.unparsed](./dtdkind-swift.enum/unparsed.md)
  Identifies an unparsed entity declaration.
### Initializers
- [init?(rawValue: UInt)](./dtdkind-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [DTD Node Kind Constants](../dtd_node_kind_constants.md)
  Constants that specify the kind and subkind of DTD declaration represented by an `NSXMLDTDNode` object. You set the DTD-node kind using the doc:nsxmldtdnode/1806486-setdtdkind method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtdnode/dtdkind-swift.enum)*