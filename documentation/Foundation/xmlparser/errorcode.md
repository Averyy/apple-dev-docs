# XMLParser.ErrorCode

**Framework**: Foundation  
**Kind**: enum

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

## Topics

### Constants
- [XMLParser.ErrorCode.internalError](xmlparser/errorcode/internalerror.md)
  The parser object encountered an internal error.
- [XMLParser.ErrorCode.outOfMemoryError](xmlparser/errorcode/outofmemoryerror.md)
  The parser object ran out of memory.
- [XMLParser.ErrorCode.documentStartError](xmlparser/errorcode/documentstarterror.md)
  The parser object is unable to start parsing.
- [XMLParser.ErrorCode.emptyDocumentError](xmlparser/errorcode/emptydocumenterror.md)
  The document is empty.
- [XMLParser.ErrorCode.prematureDocumentEndError](xmlparser/errorcode/prematuredocumentenderror.md)
  The document ended unexpectedly.
- [XMLParser.ErrorCode.invalidHexCharacterRefError](xmlparser/errorcode/invalidhexcharacterreferror.md)
  Invalid hexadecimal character reference encountered.
- [XMLParser.ErrorCode.invalidDecimalCharacterRefError](xmlparser/errorcode/invaliddecimalcharacterreferror.md)
  Invalid decimal character reference encountered.
- [XMLParser.ErrorCode.invalidCharacterRefError](xmlparser/errorcode/invalidcharacterreferror.md)
  Invalid character reference encountered.
- [XMLParser.ErrorCode.invalidCharacterError](xmlparser/errorcode/invalidcharactererror.md)
  Invalid character encountered.
- [XMLParser.ErrorCode.characterRefAtEOFError](xmlparser/errorcode/characterrefateoferror.md)
  Target of character reference cannot be found.
- [XMLParser.ErrorCode.characterRefInPrologError](xmlparser/errorcode/characterrefinprologerror.md)
  Invalid character found in the prolog.
- [XMLParser.ErrorCode.characterRefInEpilogError](xmlparser/errorcode/characterrefinepilogerror.md)
  Invalid character found in the epilog.
- [XMLParser.ErrorCode.characterRefInDTDError](xmlparser/errorcode/characterrefindtderror.md)
  Invalid character encountered in the DTD.
- [XMLParser.ErrorCode.entityRefAtEOFError](xmlparser/errorcode/entityrefateoferror.md)
  Target of entity reference is not found.
- [XMLParser.ErrorCode.entityRefInPrologError](xmlparser/errorcode/entityrefinprologerror.md)
  Invalid entity reference found in the prolog.
- [XMLParser.ErrorCode.entityRefInEpilogError](xmlparser/errorcode/entityrefinepilogerror.md)
  Invalid entity reference found in the epilog.
- [XMLParser.ErrorCode.entityRefInDTDError](xmlparser/errorcode/entityrefindtderror.md)
  Invalid entity reference found in the DTD.
- [XMLParser.ErrorCode.parsedEntityRefAtEOFError](xmlparser/errorcode/parsedentityrefateoferror.md)
  Target of parsed entity reference is not found.
- [XMLParser.ErrorCode.parsedEntityRefInPrologError](xmlparser/errorcode/parsedentityrefinprologerror.md)
  Target of parsed entity reference is not found in prolog.
- [XMLParser.ErrorCode.parsedEntityRefInEpilogError](xmlparser/errorcode/parsedentityrefinepilogerror.md)
  Target of parsed entity reference is not found in epilog.
- [XMLParser.ErrorCode.parsedEntityRefInInternalSubsetError](xmlparser/errorcode/parsedentityrefininternalsubseterror.md)
  Target of parsed entity reference is not found in internal subset.
- [XMLParser.ErrorCode.entityReferenceWithoutNameError](xmlparser/errorcode/entityreferencewithoutnameerror.md)
  Entity reference is without name.
- [XMLParser.ErrorCode.entityReferenceMissingSemiError](xmlparser/errorcode/entityreferencemissingsemierror.md)
  Entity reference is missing semicolon.
- [XMLParser.ErrorCode.parsedEntityRefNoNameError](xmlparser/errorcode/parsedentityrefnonameerror.md)
  Parsed entity reference is without an entity name.
- [XMLParser.ErrorCode.parsedEntityRefMissingSemiError](xmlparser/errorcode/parsedentityrefmissingsemierror.md)
  Parsed entity reference is missing semicolon.
- [XMLParser.ErrorCode.undeclaredEntityError](xmlparser/errorcode/undeclaredentityerror.md)
  Entity is not declared.
- [XMLParser.ErrorCode.unparsedEntityError](xmlparser/errorcode/unparsedentityerror.md)
  Cannot parse entity.
- [XMLParser.ErrorCode.entityIsExternalError](xmlparser/errorcode/entityisexternalerror.md)
  Cannot parse external entity.
- [XMLParser.ErrorCode.entityIsParameterError](xmlparser/errorcode/entityisparametererror.md)
  Entity is a parameter.
- [XMLParser.ErrorCode.unknownEncodingError](xmlparser/errorcode/unknownencodingerror.md)
  Document encoding is unknown.
- [XMLParser.ErrorCode.encodingNotSupportedError](xmlparser/errorcode/encodingnotsupportederror.md)
  Document encoding is not supported.
- [XMLParser.ErrorCode.stringNotStartedError](xmlparser/errorcode/stringnotstartederror.md)
  String is not started.
- [XMLParser.ErrorCode.stringNotClosedError](xmlparser/errorcode/stringnotclosederror.md)
  String is not closed.
- [XMLParser.ErrorCode.namespaceDeclarationError](xmlparser/errorcode/namespacedeclarationerror.md)
  Invalid namespace declaration encountered.
- [XMLParser.ErrorCode.entityNotStartedError](xmlparser/errorcode/entitynotstartederror.md)
  Entity is not started.
- [XMLParser.ErrorCode.entityNotFinishedError](xmlparser/errorcode/entitynotfinishederror.md)
  Entity is not finished.
- [XMLParser.ErrorCode.lessThanSymbolInAttributeError](xmlparser/errorcode/lessthansymbolinattributeerror.md)
  Angle bracket is used in attribute.
- [XMLParser.ErrorCode.attributeNotStartedError](xmlparser/errorcode/attributenotstartederror.md)
  Attribute is not started.
- [XMLParser.ErrorCode.attributeNotFinishedError](xmlparser/errorcode/attributenotfinishederror.md)
  Attribute is not finished.
- [XMLParser.ErrorCode.attributeHasNoValueError](xmlparser/errorcode/attributehasnovalueerror.md)
  Attribute doesn’t contain a value.
- [XMLParser.ErrorCode.attributeRedefinedError](xmlparser/errorcode/attributeredefinederror.md)
  Attribute is redefined.
- [XMLParser.ErrorCode.literalNotStartedError](xmlparser/errorcode/literalnotstartederror.md)
  Literal is not started.
- [XMLParser.ErrorCode.literalNotFinishedError](xmlparser/errorcode/literalnotfinishederror.md)
  Literal is not finished.
- [XMLParser.ErrorCode.commentNotFinishedError](xmlparser/errorcode/commentnotfinishederror.md)
  Comment is not finished.
- [XMLParser.ErrorCode.processingInstructionNotStartedError](xmlparser/errorcode/processinginstructionnotstartederror.md)
  Processing instruction is not started.
- [XMLParser.ErrorCode.processingInstructionNotFinishedError](xmlparser/errorcode/processinginstructionnotfinishederror.md)
  Processing instruction is not finished.
- [XMLParser.ErrorCode.notationNotStartedError](xmlparser/errorcode/notationnotstartederror.md)
  Notation is not started.
- [XMLParser.ErrorCode.notationNotFinishedError](xmlparser/errorcode/notationnotfinishederror.md)
  Notation is not finished.
- [XMLParser.ErrorCode.attributeListNotStartedError](xmlparser/errorcode/attributelistnotstartederror.md)
  Attribute list is not started.
- [XMLParser.ErrorCode.attributeListNotFinishedError](xmlparser/errorcode/attributelistnotfinishederror.md)
  Attribute list is not finished.
- [XMLParser.ErrorCode.mixedContentDeclNotStartedError](xmlparser/errorcode/mixedcontentdeclnotstartederror.md)
  Mixed content declaration is not started.
- [XMLParser.ErrorCode.mixedContentDeclNotFinishedError](xmlparser/errorcode/mixedcontentdeclnotfinishederror.md)
  Mixed content declaration is not finished.
- [XMLParser.ErrorCode.elementContentDeclNotStartedError](xmlparser/errorcode/elementcontentdeclnotstartederror.md)
  Element content declaration is not started.
- [XMLParser.ErrorCode.elementContentDeclNotFinishedError](xmlparser/errorcode/elementcontentdeclnotfinishederror.md)
  Element content declaration is not finished.
- [XMLParser.ErrorCode.xmlDeclNotStartedError](xmlparser/errorcode/xmldeclnotstartederror.md)
  XML declaration is not started.
- [XMLParser.ErrorCode.xmlDeclNotFinishedError](xmlparser/errorcode/xmldeclnotfinishederror.md)
  XML declaration is not finished.
- [XMLParser.ErrorCode.conditionalSectionNotStartedError](xmlparser/errorcode/conditionalsectionnotstartederror.md)
  Conditional section is not started.
- [XMLParser.ErrorCode.conditionalSectionNotFinishedError](xmlparser/errorcode/conditionalsectionnotfinishederror.md)
  Conditional section is not finished.
- [XMLParser.ErrorCode.externalSubsetNotFinishedError](xmlparser/errorcode/externalsubsetnotfinishederror.md)
  External subset is not finished.
- [XMLParser.ErrorCode.doctypeDeclNotFinishedError](xmlparser/errorcode/doctypedeclnotfinishederror.md)
  Document type declaration is not finished.
- [XMLParser.ErrorCode.misplacedCDATAEndStringError](xmlparser/errorcode/misplacedcdataendstringerror.md)
  Misplaced CDATA end string.
- [XMLParser.ErrorCode.cdataNotFinishedError](xmlparser/errorcode/cdatanotfinishederror.md)
  CDATA block is not finished.
- [XMLParser.ErrorCode.misplacedXMLDeclarationError](xmlparser/errorcode/misplacedxmldeclarationerror.md)
  Misplaced XML declaration.
- [XMLParser.ErrorCode.spaceRequiredError](xmlparser/errorcode/spacerequirederror.md)
  Space is required.
- [XMLParser.ErrorCode.separatorRequiredError](xmlparser/errorcode/separatorrequirederror.md)
  Separator is required.
- [XMLParser.ErrorCode.nmtokenRequiredError](xmlparser/errorcode/nmtokenrequirederror.md)
  Name token is required.
- [XMLParser.ErrorCode.nameRequiredError](xmlparser/errorcode/namerequirederror.md)
  Name is required.
- [XMLParser.ErrorCode.pcdataRequiredError](xmlparser/errorcode/pcdatarequirederror.md)
  CDATA is required.
- [XMLParser.ErrorCode.uriRequiredError](xmlparser/errorcode/urirequirederror.md)
  URI is required.
- [XMLParser.ErrorCode.publicIdentifierRequiredError](xmlparser/errorcode/publicidentifierrequirederror.md)
  Public identifier is required.
- [XMLParser.ErrorCode.ltRequiredError](xmlparser/errorcode/ltrequirederror.md)
  Left angle bracket is required.
- [XMLParser.ErrorCode.gtRequiredError](xmlparser/errorcode/gtrequirederror.md)
  Right angle bracket is required.
- [XMLParser.ErrorCode.ltSlashRequiredError](xmlparser/errorcode/ltslashrequirederror.md)
  Left angle bracket slash is required.
- [XMLParser.ErrorCode.equalExpectedError](xmlparser/errorcode/equalexpectederror.md)
  Equal sign expected.
- [XMLParser.ErrorCode.tagNameMismatchError](xmlparser/errorcode/tagnamemismatcherror.md)
  Tag name mismatch.
- [XMLParser.ErrorCode.unfinishedTagError](xmlparser/errorcode/unfinishedtagerror.md)
  Unfinished tag found.
- [XMLParser.ErrorCode.standaloneValueError](xmlparser/errorcode/standalonevalueerror.md)
  Standalone value found.
- [XMLParser.ErrorCode.invalidEncodingNameError](xmlparser/errorcode/invalidencodingnameerror.md)
  Invalid encoding name found.
- [XMLParser.ErrorCode.commentContainsDoubleHyphenError](xmlparser/errorcode/commentcontainsdoublehyphenerror.md)
  Comment contains double hyphen.
- [XMLParser.ErrorCode.invalidEncodingError](xmlparser/errorcode/invalidencodingerror.md)
  Invalid encoding.
- [XMLParser.ErrorCode.externalStandaloneEntityError](xmlparser/errorcode/externalstandaloneentityerror.md)
  External standalone entity.
- [XMLParser.ErrorCode.invalidConditionalSectionError](xmlparser/errorcode/invalidconditionalsectionerror.md)
  Invalid conditional section.
- [XMLParser.ErrorCode.entityValueRequiredError](xmlparser/errorcode/entityvaluerequirederror.md)
  Entity value is required.
- [XMLParser.ErrorCode.notWellBalancedError](xmlparser/errorcode/notwellbalancederror.md)
  Document is not well balanced.
- [XMLParser.ErrorCode.extraContentError](xmlparser/errorcode/extracontenterror.md)
  Error in content found.
- [XMLParser.ErrorCode.invalidCharacterInEntityError](xmlparser/errorcode/invalidcharacterinentityerror.md)
  Invalid character in entity found.
- [XMLParser.ErrorCode.parsedEntityRefInInternalError](xmlparser/errorcode/parsedentityrefininternalerror.md)
  Internal error in parsed entity reference found.
- [XMLParser.ErrorCode.entityRefLoopError](xmlparser/errorcode/entityreflooperror.md)
  Entity reference loop encountered.
- [XMLParser.ErrorCode.entityBoundaryError](xmlparser/errorcode/entityboundaryerror.md)
  Entity boundary error.
- [XMLParser.ErrorCode.invalidURIError](xmlparser/errorcode/invalidurierror.md)
  Invalid URI specified.
- [XMLParser.ErrorCode.uriFragmentError](xmlparser/errorcode/urifragmenterror.md)
  URI fragment.
- [XMLParser.ErrorCode.noDTDError](xmlparser/errorcode/nodtderror.md)
  Missing DTD.
- [XMLParser.ErrorCode.delegateAbortedParseError](xmlparser/errorcode/delegateabortedparseerror.md)
  Delegate aborted parse.
### Initializers
- [init?(rawValue: Int)](xmlparser/errorcode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [XMLParser.ExternalEntityResolvingPolicy](xmlparser/externalentityresolvingpolicy-swift.enum.md)
- [class let errorDomain: String](xmlparser/errordomain.md)
  Indicates an error in XML parsing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser/errorcode)*