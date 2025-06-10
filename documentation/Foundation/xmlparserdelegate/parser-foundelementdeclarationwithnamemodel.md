# parser(_:foundElementDeclarationWithName:model:)

**Framework**: Foundation  
**Kind**: method

Sent by a parser object to its delegate when it encounters a declaration of an element with a given model.

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
optional func parser(_ parser: XMLParser, foundElementDeclarationWithName elementName: String, model: String)
```

## Parameters

- `parser`: An   object parsing XML.
- `elementName`: A string that is the name of an element.
- `model`: A string that specifies a model for  .

## See Also

- [func parser(XMLParser, didStartElement: String, namespaceURI: String?, qualifiedName: String?, attributes: [String : String])](xmlparserdelegate/parser(_:didstartelement:namespaceuri:qualifiedname:attributes:).md)
  Sent by a parser object to its delegate when it encounters a start tag for a given element.
- [func parser(XMLParser, foundAttributeDeclarationWithName: String, forElement: String, type: String?, defaultValue: String?)](xmlparserdelegate/parser(_:foundattributedeclarationwithname:forelement:type:defaultvalue:).md)
  Sent by a parser object to its delegate when it encounters a declaration of an attribute that is associated with a specific element.
- [func parser(XMLParser, foundExternalEntityDeclarationWithName: String, publicID: String?, systemID: String?)](xmlparserdelegate/parser(_:foundexternalentitydeclarationwithname:publicid:systemid:).md)
  Sent by a parser object to its delegate when it encounters an external entity declaration.
- [func parser(XMLParser, foundInternalEntityDeclarationWithName: String, value: String?)](xmlparserdelegate/parser(_:foundinternalentitydeclarationwithname:value:).md)
  Sent by a parser object to the delegate when it encounters an internal entity declaration.
- [func parser(XMLParser, foundUnparsedEntityDeclarationWithName: String, publicID: String?, systemID: String?, notationName: String?)](xmlparserdelegate/parser(_:foundunparsedentitydeclarationwithname:publicid:systemid:notationname:).md)
  Sent by a parser object to its delegate when it encounters an unparsed entity declaration.
- [func parser(XMLParser, foundNotationDeclarationWithName: String, publicID: String?, systemID: String?)](xmlparserdelegate/parser(_:foundnotationdeclarationwithname:publicid:systemid:).md)
  Sent by a parser object to its delegate when it encounters a notation declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparserdelegate/parser(_:foundelementdeclarationwithname:model:))*