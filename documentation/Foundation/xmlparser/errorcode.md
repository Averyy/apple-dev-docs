# XMLParser.ErrorCode

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

The following error codes are defined by `NSXMLParser`. For error codes not listed here, see the `<libxml/xmlerror.h>` header file.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum ErrorCode
```

```c
enum NSXMLParserError : NSInteger;
```

## Topics

### Constants
- [XMLParser.ErrorCode.internalError](./errorcode/internalerror.md)
  The parser object encountered an internal error.
- [XMLParser.ErrorCode.outOfMemoryError](./errorcode/outofmemoryerror.md)
  The parser object ran out of memory.
- [XMLParser.ErrorCode.documentStartError](./errorcode/documentstarterror.md)
  The parser object is unable to start parsing.
- [XMLParser.ErrorCode.emptyDocumentError](./errorcode/emptydocumenterror.md)
  The document is empty.
- [XMLParser.ErrorCode.prematureDocumentEndError](./errorcode/prematuredocumentenderror.md)
  The document ended unexpectedly.
- [XMLParser.ErrorCode.invalidHexCharacterRefError](./errorcode/invalidhexcharacterreferror.md)
  Invalid hexadecimal character reference encountered.
- [XMLParser.ErrorCode.invalidDecimalCharacterRefError](./errorcode/invaliddecimalcharacterreferror.md)
  Invalid decimal character reference encountered.
- [XMLParser.ErrorCode.invalidCharacterRefError](./errorcode/invalidcharacterreferror.md)
  Invalid character reference encountered.
- [XMLParser.ErrorCode.invalidCharacterError](./errorcode/invalidcharactererror.md)
  Invalid character encountered.
- [XMLParser.ErrorCode.characterRefAtEOFError](./errorcode/characterrefateoferror.md)
  Target of character reference cannot be found.
- [XMLParser.ErrorCode.characterRefInPrologError](./errorcode/characterrefinprologerror.md)
  Invalid character found in the prolog.
- [XMLParser.ErrorCode.characterRefInEpilogError](./errorcode/characterrefinepilogerror.md)
  Invalid character found in the epilog.
- [XMLParser.ErrorCode.characterRefInDTDError](./errorcode/characterrefindtderror.md)
  Invalid character encountered in the DTD.
- [XMLParser.ErrorCode.entityRefAtEOFError](./errorcode/entityrefateoferror.md)
  Target of entity reference is not found.
- [XMLParser.ErrorCode.entityRefInPrologError](./errorcode/entityrefinprologerror.md)
  Invalid entity reference found in the prolog.
- [XMLParser.ErrorCode.entityRefInEpilogError](./errorcode/entityrefinepilogerror.md)
  Invalid entity reference found in the epilog.
- [XMLParser.ErrorCode.entityRefInDTDError](./errorcode/entityrefindtderror.md)
  Invalid entity reference found in the DTD.
- [XMLParser.ErrorCode.parsedEntityRefAtEOFError](./errorcode/parsedentityrefateoferror.md)
  Target of parsed entity reference is not found.
- [XMLParser.ErrorCode.parsedEntityRefInPrologError](./errorcode/parsedentityrefinprologerror.md)
  Target of parsed entity reference is not found in prolog.
- [XMLParser.ErrorCode.parsedEntityRefInEpilogError](./errorcode/parsedentityrefinepilogerror.md)
  Target of parsed entity reference is not found in epilog.
- [XMLParser.ErrorCode.parsedEntityRefInInternalSubsetError](./errorcode/parsedentityrefininternalsubseterror.md)
  Target of parsed entity reference is not found in internal subset.
- [XMLParser.ErrorCode.entityReferenceWithoutNameError](./errorcode/entityreferencewithoutnameerror.md)
  Entity reference is without name.
- [XMLParser.ErrorCode.entityReferenceMissingSemiError](./errorcode/entityreferencemissingsemierror.md)
  Entity reference is missing semicolon.
- [XMLParser.ErrorCode.parsedEntityRefNoNameError](./errorcode/parsedentityrefnonameerror.md)
  Parsed entity reference is without an entity name.
- [XMLParser.ErrorCode.parsedEntityRefMissingSemiError](./errorcode/parsedentityrefmissingsemierror.md)
  Parsed entity reference is missing semicolon.
- [XMLParser.ErrorCode.undeclaredEntityError](./errorcode/undeclaredentityerror.md)
  Entity is not declared.
- [XMLParser.ErrorCode.unparsedEntityError](./errorcode/unparsedentityerror.md)
  Cannot parse entity.
- [XMLParser.ErrorCode.entityIsExternalError](./errorcode/entityisexternalerror.md)
  Cannot parse external entity.
- [XMLParser.ErrorCode.entityIsParameterError](./errorcode/entityisparametererror.md)
  Entity is a parameter.
- [XMLParser.ErrorCode.unknownEncodingError](./errorcode/unknownencodingerror.md)
  Document encoding is unknown.
- [XMLParser.ErrorCode.encodingNotSupportedError](./errorcode/encodingnotsupportederror.md)
  Document encoding is not supported.
- [XMLParser.ErrorCode.stringNotStartedError](./errorcode/stringnotstartederror.md)
  String is not started.
- [XMLParser.ErrorCode.stringNotClosedError](./errorcode/stringnotclosederror.md)
  String is not closed.
- [XMLParser.ErrorCode.namespaceDeclarationError](./errorcode/namespacedeclarationerror.md)
  Invalid namespace declaration encountered.
- [XMLParser.ErrorCode.entityNotStartedError](./errorcode/entitynotstartederror.md)
  Entity is not started.
- [XMLParser.ErrorCode.entityNotFinishedError](./errorcode/entitynotfinishederror.md)
  Entity is not finished.
- [XMLParser.ErrorCode.lessThanSymbolInAttributeError](./errorcode/lessthansymbolinattributeerror.md)
  Angle bracket is used in attribute.
- [XMLParser.ErrorCode.attributeNotStartedError](./errorcode/attributenotstartederror.md)
  Attribute is not started.
- [XMLParser.ErrorCode.attributeNotFinishedError](./errorcode/attributenotfinishederror.md)
  Attribute is not finished.
- [XMLParser.ErrorCode.attributeHasNoValueError](./errorcode/attributehasnovalueerror.md)
  Attribute doesn’t contain a value.
- [XMLParser.ErrorCode.attributeRedefinedError](./errorcode/attributeredefinederror.md)
  Attribute is redefined.
- [XMLParser.ErrorCode.literalNotStartedError](./errorcode/literalnotstartederror.md)
  Literal is not started.
- [XMLParser.ErrorCode.literalNotFinishedError](./errorcode/literalnotfinishederror.md)
  Literal is not finished.
- [XMLParser.ErrorCode.commentNotFinishedError](./errorcode/commentnotfinishederror.md)
  Comment is not finished.
- [XMLParser.ErrorCode.processingInstructionNotStartedError](./errorcode/processinginstructionnotstartederror.md)
  Processing instruction is not started.
- [XMLParser.ErrorCode.processingInstructionNotFinishedError](./errorcode/processinginstructionnotfinishederror.md)
  Processing instruction is not finished.
- [XMLParser.ErrorCode.notationNotStartedError](./errorcode/notationnotstartederror.md)
  Notation is not started.
- [XMLParser.ErrorCode.notationNotFinishedError](./errorcode/notationnotfinishederror.md)
  Notation is not finished.
- [XMLParser.ErrorCode.attributeListNotStartedError](./errorcode/attributelistnotstartederror.md)
  Attribute list is not started.
- [XMLParser.ErrorCode.attributeListNotFinishedError](./errorcode/attributelistnotfinishederror.md)
  Attribute list is not finished.
- [XMLParser.ErrorCode.mixedContentDeclNotStartedError](./errorcode/mixedcontentdeclnotstartederror.md)
  Mixed content declaration is not started.
- [XMLParser.ErrorCode.mixedContentDeclNotFinishedError](./errorcode/mixedcontentdeclnotfinishederror.md)
  Mixed content declaration is not finished.
- [XMLParser.ErrorCode.elementContentDeclNotStartedError](./errorcode/elementcontentdeclnotstartederror.md)
  Element content declaration is not started.
- [XMLParser.ErrorCode.elementContentDeclNotFinishedError](./errorcode/elementcontentdeclnotfinishederror.md)
  Element content declaration is not finished.
- [XMLParser.ErrorCode.xmlDeclNotStartedError](./errorcode/xmldeclnotstartederror.md)
  XML declaration is not started.
- [XMLParser.ErrorCode.xmlDeclNotFinishedError](./errorcode/xmldeclnotfinishederror.md)
  XML declaration is not finished.
- [XMLParser.ErrorCode.conditionalSectionNotStartedError](./errorcode/conditionalsectionnotstartederror.md)
  Conditional section is not started.
- [XMLParser.ErrorCode.conditionalSectionNotFinishedError](./errorcode/conditionalsectionnotfinishederror.md)
  Conditional section is not finished.
- [XMLParser.ErrorCode.externalSubsetNotFinishedError](./errorcode/externalsubsetnotfinishederror.md)
  External subset is not finished.
- [XMLParser.ErrorCode.doctypeDeclNotFinishedError](./errorcode/doctypedeclnotfinishederror.md)
  Document type declaration is not finished.
- [XMLParser.ErrorCode.misplacedCDATAEndStringError](./errorcode/misplacedcdataendstringerror.md)
  Misplaced CDATA end string.
- [XMLParser.ErrorCode.cdataNotFinishedError](./errorcode/cdatanotfinishederror.md)
  CDATA block is not finished.
- [XMLParser.ErrorCode.misplacedXMLDeclarationError](./errorcode/misplacedxmldeclarationerror.md)
  Misplaced XML declaration.
- [XMLParser.ErrorCode.spaceRequiredError](./errorcode/spacerequirederror.md)
  Space is required.
- [XMLParser.ErrorCode.separatorRequiredError](./errorcode/separatorrequirederror.md)
  Separator is required.
- [XMLParser.ErrorCode.nmtokenRequiredError](./errorcode/nmtokenrequirederror.md)
  Name token is required.
- [XMLParser.ErrorCode.nameRequiredError](./errorcode/namerequirederror.md)
  Name is required.
- [XMLParser.ErrorCode.pcdataRequiredError](./errorcode/pcdatarequirederror.md)
  CDATA is required.
- [XMLParser.ErrorCode.uriRequiredError](./errorcode/urirequirederror.md)
  URI is required.
- [XMLParser.ErrorCode.publicIdentifierRequiredError](./errorcode/publicidentifierrequirederror.md)
  Public identifier is required.
- [XMLParser.ErrorCode.ltRequiredError](./errorcode/ltrequirederror.md)
  Left angle bracket is required.
- [XMLParser.ErrorCode.gtRequiredError](./errorcode/gtrequirederror.md)
  Right angle bracket is required.
- [XMLParser.ErrorCode.ltSlashRequiredError](./errorcode/ltslashrequirederror.md)
  Left angle bracket slash is required.
- [XMLParser.ErrorCode.equalExpectedError](./errorcode/equalexpectederror.md)
  Equal sign expected.
- [XMLParser.ErrorCode.tagNameMismatchError](./errorcode/tagnamemismatcherror.md)
  Tag name mismatch.
- [XMLParser.ErrorCode.unfinishedTagError](./errorcode/unfinishedtagerror.md)
  Unfinished tag found.
- [XMLParser.ErrorCode.standaloneValueError](./errorcode/standalonevalueerror.md)
  Standalone value found.
- [XMLParser.ErrorCode.invalidEncodingNameError](./errorcode/invalidencodingnameerror.md)
  Invalid encoding name found.
- [XMLParser.ErrorCode.commentContainsDoubleHyphenError](./errorcode/commentcontainsdoublehyphenerror.md)
  Comment contains double hyphen.
- [XMLParser.ErrorCode.invalidEncodingError](./errorcode/invalidencodingerror.md)
  Invalid encoding.
- [XMLParser.ErrorCode.externalStandaloneEntityError](./errorcode/externalstandaloneentityerror.md)
  External standalone entity.
- [XMLParser.ErrorCode.invalidConditionalSectionError](./errorcode/invalidconditionalsectionerror.md)
  Invalid conditional section.
- [XMLParser.ErrorCode.entityValueRequiredError](./errorcode/entityvaluerequirederror.md)
  Entity value is required.
- [XMLParser.ErrorCode.notWellBalancedError](./errorcode/notwellbalancederror.md)
  Document is not well balanced.
- [XMLParser.ErrorCode.extraContentError](./errorcode/extracontenterror.md)
  Error in content found.
- [XMLParser.ErrorCode.invalidCharacterInEntityError](./errorcode/invalidcharacterinentityerror.md)
  Invalid character in entity found.
- [XMLParser.ErrorCode.parsedEntityRefInInternalError](./errorcode/parsedentityrefininternalerror.md)
  Internal error in parsed entity reference found.
- [XMLParser.ErrorCode.entityRefLoopError](./errorcode/entityreflooperror.md)
  Entity reference loop encountered.
- [XMLParser.ErrorCode.entityBoundaryError](./errorcode/entityboundaryerror.md)
  Entity boundary error.
- [XMLParser.ErrorCode.invalidURIError](./errorcode/invalidurierror.md)
  Invalid URI specified.
- [XMLParser.ErrorCode.uriFragmentError](./errorcode/urifragmenterror.md)
  URI fragment.
- [XMLParser.ErrorCode.noDTDError](./errorcode/nodtderror.md)
  Missing DTD.
- [XMLParser.ErrorCode.delegateAbortedParseError](./errorcode/delegateabortedparseerror.md)
  Delegate aborted parse.
### Initializers
- [init?(rawValue: Int)](./errorcode/init%28rawvalue%29.md)

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
- [XMLParser.ExternalEntityResolvingPolicy](./externalentityresolvingpolicy-swift.enum.md)
  Defines the external entity resolving policy used by an `NSXMLParser` instance.
- [class let errorDomain: String](./errordomain.md)
  Indicates an error in XML parsing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/errorcode)*