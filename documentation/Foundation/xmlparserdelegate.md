# XMLParserDelegate

**Framework**: Foundation  
**Kind**: protocol

The interface an XML parser uses to inform its delegate about the content of the parsed document.

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
protocol XMLParserDelegate : NSObjectProtocol
```

## Topics

### Handling XML
- [func parserDidStartDocument(XMLParser)](xmlparserdelegate/parserdidstartdocument(_:).md)
  Sent by the parser object to the delegate when it begins parsing a document.
- [func parserDidEndDocument(XMLParser)](xmlparserdelegate/parserdidenddocument(_:).md)
  Sent by the parser object to the delegate when it has successfully completed parsing.
- [func parser(XMLParser, didStartElement: String, namespaceURI: String?, qualifiedName: String?, attributes: [String : String])](xmlparserdelegate/parser(_:didstartelement:namespaceuri:qualifiedname:attributes:).md)
  Sent by a parser object to its delegate when it encounters a start tag for a given element.
- [func parser(XMLParser, didEndElement: String, namespaceURI: String?, qualifiedName: String?)](xmlparserdelegate/parser(_:didendelement:namespaceuri:qualifiedname:).md)
  Sent by a parser object to its delegate when it encounters an end tag for a specific element.
- [func parser(XMLParser, didStartMappingPrefix: String, toURI: String)](xmlparserdelegate/parser(_:didstartmappingprefix:touri:).md)
  Sent by a parser object to its delegate the first time it encounters a given namespace prefix, which is mapped to a URI.
- [func parser(XMLParser, didEndMappingPrefix: String)](xmlparserdelegate/parser(_:didendmappingprefix:).md)
  Sent by a parser object to its delegate when a given namespace prefix goes out of scope.
- [func parser(XMLParser, resolveExternalEntityName: String, systemID: String?) -> Data?](xmlparserdelegate/parser(_:resolveexternalentityname:systemid:).md)
  Sent by a parser object to its delegate when it encounters a given external entity with a specific system ID.
- [func parser(XMLParser, parseErrorOccurred: any Error)](xmlparserdelegate/parser(_:parseerroroccurred:).md)
  Sent by a parser object to its delegate when it encounters a fatal error.
- [func parser(XMLParser, validationErrorOccurred: any Error)](xmlparserdelegate/parser(_:validationerroroccurred:).md)
  Sent by a parser object to its delegate when it encounters a fatal validation error. `NSXMLParser` currently does not invoke this method and does not perform validation.
- [func parser(XMLParser, foundCharacters: String)](xmlparserdelegate/parser(_:foundcharacters:).md)
  Sent by a parser object to provide its delegate with a string representing all or part of the characters of the current element.
- [func parser(XMLParser, foundIgnorableWhitespace: String)](xmlparserdelegate/parser(_:foundignorablewhitespace:).md)
  Reported by a parser object to provide its delegate with a string representing all or part of the ignorable whitespace characters of the current element.
- [func parser(XMLParser, foundProcessingInstructionWithTarget: String, data: String?)](xmlparserdelegate/parser(_:foundprocessinginstructionwithtarget:data:).md)
  Sent by a parser object to its delegate when it encounters a processing instruction.
- [func parser(XMLParser, foundComment: String)](xmlparserdelegate/parser(_:foundcomment:).md)
  Sent by a parser object to its delegate when it encounters a comment in the XML.
- [func parser(XMLParser, foundCDATA: Data)](xmlparserdelegate/parser(_:foundcdata:).md)
  Sent by a parser object to its delegate when it encounters a CDATA block.
### Handling the DTD
- [func parser(XMLParser, foundAttributeDeclarationWithName: String, forElement: String, type: String?, defaultValue: String?)](xmlparserdelegate/parser(_:foundattributedeclarationwithname:forelement:type:defaultvalue:).md)
  Sent by a parser object to its delegate when it encounters a declaration of an attribute that is associated with a specific element.
- [func parser(XMLParser, foundElementDeclarationWithName: String, model: String)](xmlparserdelegate/parser(_:foundelementdeclarationwithname:model:).md)
  Sent by a parser object to its delegate when it encounters a declaration of an element with a given model.
- [func parser(XMLParser, foundExternalEntityDeclarationWithName: String, publicID: String?, systemID: String?)](xmlparserdelegate/parser(_:foundexternalentitydeclarationwithname:publicid:systemid:).md)
  Sent by a parser object to its delegate when it encounters an external entity declaration.
- [func parser(XMLParser, foundInternalEntityDeclarationWithName: String, value: String?)](xmlparserdelegate/parser(_:foundinternalentitydeclarationwithname:value:).md)
  Sent by a parser object to the delegate when it encounters an internal entity declaration.
- [func parser(XMLParser, foundUnparsedEntityDeclarationWithName: String, publicID: String?, systemID: String?, notationName: String?)](xmlparserdelegate/parser(_:foundunparsedentitydeclarationwithname:publicid:systemid:notationname:).md)
  Sent by a parser object to its delegate when it encounters an unparsed entity declaration.
- [func parser(XMLParser, foundNotationDeclarationWithName: String, publicID: String?, systemID: String?)](xmlparserdelegate/parser(_:foundnotationdeclarationwithname:publicid:systemid:).md)
  Sent by a parser object to its delegate when it encounters a notation declaration.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class XMLParser](xmlparser.md)
  An event driven parser of XML documents (including DTD declarations).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparserdelegate)*