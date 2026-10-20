# parser(_:didEndElement:namespaceURI:qualifiedName:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent by a parser object to its delegate when it encounters an end tag for a specific element.

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
optional func parser(_ parser: XMLParser, didEndElement elementName: String, namespaceURI: String?, qualifiedName qName: String?)
```

```objc
- (void) parser:(NSXMLParser *) parser didEndElement:(NSString *) elementName namespaceURI:(NSString *) namespaceURI qualifiedName:(NSString *) qName;
```

## Parameters

- `parser`: A parser object.
- `elementName`: A string that is the name of an element (in its end tag).
- `namespaceURI`: If namespace processing is turned on, contains the URI for the current namespace as a string object.
- `qName`: If namespace processing is turned on, contains the qualified name for the current namespace as a string object.

## See Also

### Related Documentation
- [var shouldProcessNamespaces: Bool](../xmlparser/shouldprocessnamespaces.md)
  A Boolean value that determines whether the parser reports the namespaces and qualified names of elements.
### Handling XML
- [func parserDidStartDocument(XMLParser)](./parserdidstartdocument%28_%29.md)
  Sent by the parser object to the delegate when it begins parsing a document.
- [func parserDidEndDocument(XMLParser)](./parserdidenddocument%28_%29.md)
  Sent by the parser object to the delegate when it has successfully completed parsing.
- [func parser(XMLParser, didStartElement: String, namespaceURI: String?, qualifiedName: String?, attributes: [String : String])](./parser%28_,didstartelement,namespaceuri,qualifiedname,attributes%29.md)
  Sent by a parser object to its delegate when it encounters a start tag for a given element.
- [func parser(XMLParser, didStartMappingPrefix: String, toURI: String)](./parser%28_,didstartmappingprefix,touri%29.md)
  Sent by a parser object to its delegate the first time it encounters a given namespace prefix, which is mapped to a URI.
- [func parser(XMLParser, didEndMappingPrefix: String)](./parser%28_,didendmappingprefix%29.md)
  Sent by a parser object to its delegate when a given namespace prefix goes out of scope.
- [func parser(XMLParser, resolveExternalEntityName: String, systemID: String?) -> Data?](./parser%28_,resolveexternalentityname,systemid%29.md)
  Sent by a parser object to its delegate when it encounters a given external entity with a specific system ID.
- [func parser(XMLParser, parseErrorOccurred: any Error)](./parser%28_,parseerroroccurred%29.md)
  Sent by a parser object to its delegate when it encounters a fatal error.
- [func parser(XMLParser, validationErrorOccurred: any Error)](./parser%28_,validationerroroccurred%29.md)
  Sent by a parser object to its delegate when it encounters a fatal validation error. `NSXMLParser` currently does not invoke this method and does not perform validation.
- [func parser(XMLParser, foundCharacters: String)](./parser%28_,foundcharacters%29.md)
  Sent by a parser object to provide its delegate with a string representing all or part of the characters of the current element.
- [func parser(XMLParser, foundIgnorableWhitespace: String)](./parser%28_,foundignorablewhitespace%29.md)
  Reported by a parser object to provide its delegate with a string representing all or part of the ignorable whitespace characters of the current element.
- [func parser(XMLParser, foundProcessingInstructionWithTarget: String, data: String?)](./parser%28_,foundprocessinginstructionwithtarget,data%29.md)
  Sent by a parser object to its delegate when it encounters a processing instruction.
- [func parser(XMLParser, foundComment: String)](./parser%28_,foundcomment%29.md)
  Sent by a parser object to its delegate when it encounters a comment in the XML.
- [func parser(XMLParser, foundCDATA: Data)](./parser%28_,foundcdata%29.md)
  Sent by a parser object to its delegate when it encounters a CDATA block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparserdelegate/parser(_:didendelement:namespaceuri:qualifiedname:))*