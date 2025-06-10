# parser(_:foundUnparsedEntityDeclarationWithName:publicID:systemID:notationName:)

**Framework**: Foundation  
**Kind**: method

Sent by a parser object to its delegate when it encounters an unparsed entity declaration.

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
optional func parser(_ parser: XMLParser, foundUnparsedEntityDeclarationWithName name: String, publicID: String?, systemID: String?, notationName: String?)
```

## Parameters

- `parser`: An   object parsing XML.
- `name`: A string that is the name of the unparsed entity in the declaration.
- `publicID`: A string specifying the public ID associated with the entity  .
- `systemID`: A string specifying the system ID associated with the entity  .
- `notationName`: A string specifying a notation of the declaration of entity  .

## See Also

- [func parser(XMLParser, resolveExternalEntityName: String, systemID: String?) -> Data?](xmlparserdelegate/parser(_:resolveexternalentityname:systemid:).md)
  Sent by a parser object to its delegate when it encounters a given external entity with a specific system ID.
- [func parser(XMLParser, foundAttributeDeclarationWithName: String, forElement: String, type: String?, defaultValue: String?)](xmlparserdelegate/parser(_:foundattributedeclarationwithname:forelement:type:defaultvalue:).md)
  Sent by a parser object to its delegate when it encounters a declaration of an attribute that is associated with a specific element.
- [func parser(XMLParser, foundElementDeclarationWithName: String, model: String)](xmlparserdelegate/parser(_:foundelementdeclarationwithname:model:).md)
  Sent by a parser object to its delegate when it encounters a declaration of an element with a given model.
- [func parser(XMLParser, foundExternalEntityDeclarationWithName: String, publicID: String?, systemID: String?)](xmlparserdelegate/parser(_:foundexternalentitydeclarationwithname:publicid:systemid:).md)
  Sent by a parser object to its delegate when it encounters an external entity declaration.
- [func parser(XMLParser, foundInternalEntityDeclarationWithName: String, value: String?)](xmlparserdelegate/parser(_:foundinternalentitydeclarationwithname:value:).md)
  Sent by a parser object to the delegate when it encounters an internal entity declaration.
- [func parser(XMLParser, foundNotationDeclarationWithName: String, publicID: String?, systemID: String?)](xmlparserdelegate/parser(_:foundnotationdeclarationwithname:publicid:systemid:).md)
  Sent by a parser object to its delegate when it encounters a notation declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparserdelegate/parser(_:foundunparsedentitydeclarationwithname:publicid:systemid:notationname:))*