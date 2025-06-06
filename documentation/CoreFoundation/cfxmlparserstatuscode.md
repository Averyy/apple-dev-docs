# CFXMLParserStatusCode

**Framework**: Core Foundation  
**Kind**: struct

The various status and error flags that can be returned by the parser.

**Availability**:
- macOS ?+

## Declaration

```swift
struct CFXMLParserStatusCode
```

#### Overview

Parser status is determined by calling the [`CFXMLParserGetStatusCode`](cfxmlparsergetstatuscode.md) function. The parser reports errors to your application by invoking the [`CFXMLParserHandleErrorCallBack`](cfxmlparserhandleerrorcallback.md) function.

## Topics

### Constants
- [static var statusParseNotBegun: CFXMLParserStatusCode](cfxmlparserstatuscode/statusparsenotbegun.md)
  Indicates the parser has not begun.
- [static var statusParseInProgress: CFXMLParserStatusCode](cfxmlparserstatuscode/statusparseinprogress.md)
  Indicates the parser is in progress.
- [static var errorUnexpectedEOF: CFXMLParserStatusCode](cfxmlparserstatuscode/errorunexpectedeof.md)
  Indicates an unexpected EOF occurred.
- [static var errorUnknownEncoding: CFXMLParserStatusCode](cfxmlparserstatuscode/errorunknownencoding.md)
  Indicates an unknown encoding error.
- [static var errorEncodingConversionFailure: CFXMLParserStatusCode](cfxmlparserstatuscode/errorencodingconversionfailure.md)
  Indicates an encoding conversion error.
- [static var errorMalformedProcessingInstruction: CFXMLParserStatusCode](cfxmlparserstatuscode/errormalformedprocessinginstruction.md)
  Indicates a malformed processing instruction.
- [static var errorMalformedDTD: CFXMLParserStatusCode](cfxmlparserstatuscode/errormalformeddtd.md)
  Indicates a malformed DTD.
- [static var errorMalformedName: CFXMLParserStatusCode](cfxmlparserstatuscode/errormalformedname.md)
  Indicates a malformed name.
- [static var errorMalformedCDSect: CFXMLParserStatusCode](cfxmlparserstatuscode/errormalformedcdsect.md)
  Indicates a malformed CDATA section.
- [static var errorMalformedCloseTag: CFXMLParserStatusCode](cfxmlparserstatuscode/errormalformedclosetag.md)
  Indicates a malformed close tag.
- [static var errorMalformedStartTag: CFXMLParserStatusCode](cfxmlparserstatuscode/errormalformedstarttag.md)
  Indicates a malformed start tag.
- [static var errorMalformedDocument: CFXMLParserStatusCode](cfxmlparserstatuscode/errormalformeddocument.md)
  Indicates a malformed document.
- [static var errorElementlessDocument: CFXMLParserStatusCode](cfxmlparserstatuscode/errorelementlessdocument.md)
  Indicates a document containing no elements.
- [static var errorMalformedComment: CFXMLParserStatusCode](cfxmlparserstatuscode/errormalformedcomment.md)
  Indicates a malformed comment.
- [static var errorMalformedCharacterReference: CFXMLParserStatusCode](cfxmlparserstatuscode/errormalformedcharacterreference.md)
  Indicates a malformed character reference.
- [static var errorMalformedParsedCharacterData: CFXMLParserStatusCode](cfxmlparserstatuscode/errormalformedparsedcharacterdata.md)
  Indicates malformed character data.
- [static var errorNoData: CFXMLParserStatusCode](cfxmlparserstatuscode/errornodata.md)
  Indicates a no data error.
### Initializers
- [init(rawValue: CFIndex)](cfxmlparserstatuscode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct CFXMLParserOptions](cfxmlparseroptions.md)
  Options you can use to control the parser’s treatment of an XML document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparserstatuscode)*