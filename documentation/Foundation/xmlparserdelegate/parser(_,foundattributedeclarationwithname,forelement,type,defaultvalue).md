# parser(_:foundAttributeDeclarationWithName:forElement:type:defaultValue:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent by a parser object to its delegate when it encounters a declaration of an attribute that is associated with a specific element.

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
optional func parser(_ parser: XMLParser, foundAttributeDeclarationWithName attributeName: String, forElement elementName: String, type: String?, defaultValue: String?)
```

```objc
- (void) parser:(NSXMLParser *) parser foundAttributeDeclarationWithName:(NSString *) attributeName forElement:(NSString *) elementName type:(NSString *) type defaultValue:(NSString *) defaultValue;
```

## Parameters

- `parser`: An `NSXMLParser` object parsing XML.
- `attributeName`: A string that is the name of an attribute.
- `elementName`: A string that is the name of an element that has the attribute `attributeName`.
- `type`: A string, such as “ENTITY”, “NOTATION”, or “ID”, that indicates the type of the attribute.
- `defaultValue`: A string that specifies the default value of the attribute.

## See Also

### Related Documentation
- [func parser(XMLParser, didStartElement: String, namespaceURI: String?, qualifiedName: String?, attributes: [String : String])](./parser%28_,didstartelement,namespaceuri,qualifiedname,attributes%29.md)
  Sent by a parser object to its delegate when it encounters a start tag for a given element.
### Handling the DTD
- [func parser(XMLParser, foundElementDeclarationWithName: String, model: String)](./parser%28_,foundelementdeclarationwithname,model%29.md)
  Sent by a parser object to its delegate when it encounters a declaration of an element with a given model.
- [func parser(XMLParser, foundExternalEntityDeclarationWithName: String, publicID: String?, systemID: String?)](./parser%28_,foundexternalentitydeclarationwithname,publicid,systemid%29.md)
  Sent by a parser object to its delegate when it encounters an external entity declaration.
- [func parser(XMLParser, foundInternalEntityDeclarationWithName: String, value: String?)](./parser%28_,foundinternalentitydeclarationwithname,value%29.md)
  Sent by a parser object to the delegate when it encounters an internal entity declaration.
- [func parser(XMLParser, foundUnparsedEntityDeclarationWithName: String, publicID: String?, systemID: String?, notationName: String?)](./parser%28_,foundunparsedentitydeclarationwithname,publicid,systemid,notationname%29.md)
  Sent by a parser object to its delegate when it encounters an unparsed entity declaration.
- [func parser(XMLParser, foundNotationDeclarationWithName: String, publicID: String?, systemID: String?)](./parser%28_,foundnotationdeclarationwithname,publicid,systemid%29.md)
  Sent by a parser object to its delegate when it encounters a notation declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparserdelegate/parser(_:foundattributedeclarationwithname:forelement:type:defaultvalue:))*