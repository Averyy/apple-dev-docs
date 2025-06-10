# parser(_:parseErrorOccurred:)

**Framework**: Foundation  
**Kind**: method

Sent by a parser object to its delegate when it encounters a fatal error.

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
optional func parser(_ parser: XMLParser, parseErrorOccurred parseError: any Error)
```

#### Discussion

When this method is invoked, parsing is stopped. For further information about the error, you can query `parseError` or you can send the `parser` a [`parserError`](xmlparser/parsererror.md) message. You can also send the parser [`lineNumber`](xmlparser/linenumber.md) and [`columnNumber`](xmlparser/columnnumber.md) messages to further isolate where the error occurred. Typically you implement this method to display information about the error to the user.

## Parameters

- `parser`: A parser object.
- `parseError`: An   object describing the parsing error that occurred.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparserdelegate/parser(_:parseerroroccurred:))*